import copy
import os
import re
import json
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def insert_variables_as_properties_in_geodata(geodata, dataframe, zip_column, variable_names):
    output_geodata = copy.deepcopy(geodata)
    
    for neighborhood in output_geodata['features']:
        zipcode = neighborhood['id']
        row = dataframe[dataframe[zip_column] == zipcode]

        if not row.empty:
            variables_values = row[variable_names].values[0]  # todo: why this 0 index
            for name, value in zip(variable_names, variables_values):
                neighborhood['properties'][name] = str(value)
    
    return output_geodata

def format_template(template, variable_names):
    replaced = copy.deepcopy(template)
    for name in variable_names:
        replaced = re.sub(r'\{\}', '%{properties.' + name + '}', replaced, count=1)
    return replaced

def load_geodata(geodata_path, id_property='zip'):
    with open(os.path.join(geodata_path)) as geojson_file:
        geodata = json.loads(geojson_file.read())
        # add id feature for choroplethmapbox
        for feature in geodata['features']:
            feature['id'] = feature['properties'][id_property]
        return geodata

def get_center_coordinates(geodata):
    # get neighborhoods latitudes and longitudes
    centers = []
    for area in geodata['features']:
        area_coords = np.array(area['geometry']['coordinates'][0][0])
        longitudes = area_coords[:, 0]
        latitudes = area_coords[:, 1]
        centers.append([0.5 * (longitudes.min() + longitudes.max()), 0.5 * (latitudes.min() + latitudes.max())])
    centers = np.array(centers)
    return centers[:, 0].mean(), centers[:, 1].mean()

def plot_map(title, geodata_path, dataframe, zip_column, value_column, template, mapbox_access_token):
    '''
    title: plot title
    
    geodata_path: path to the geojson file
    
    dataframe: Dataframe with columns: 
      - zip (column name specified in zip_column),
      - value plotted as color of the neighborhood (column name specified in value_column)
      - any other additional column will be used as a variable in the template (first additional column as first
      inter)
    
    zip_column: name of the column in the dataframe containing zip codes
    
    value_column: name of the column in the dataframe containig values for filling neighborhoods with colors
    template: text that will be displayed in a box over the hovered neighborhood. Any variable in the template
    should be denoted by "{}". Variables will be taken from the remaining columns of the dataframe in the order
    in which the columns appear.
    
    template: a string in a python string format (with %s in places where to put variables)
    
    title: plot title
    '''
    
    # load geodata
    geodata = load_geodata(geodata_path)
    center_longitude, center_latitude = get_center_coordinates(geodata)
    
    # prepare data
    columns = dataframe.columns.values
    variable_names = np.setdiff1d(columns, np.array([zip_column, value_column]))
    extended_geodata = insert_variables_as_properties_in_geodata(geodata, dataframe, zip_column, variable_names)
    formatted_template = format_template(template, variable_names) + '<extra></extra>'
    
    # plot
    figure = go.Figure(go.Choroplethmapbox(
        geojson=extended_geodata,
        locations=dataframe[zip_column],
        z=dataframe[value_column],
        hovertemplate=formatted_template
    ))
    figure.update_layout(
        title=title,
        font={'family': 'Arial Black'},
        mapbox_accesstoken=mapbox_access_token,
        mapbox_zoom=9.5,
        mapbox_pitch=40,
        mapbox_bearing=70,
        mapbox_center={'lat': center_latitude, 'lon': center_longitude},
    )
    figure.show()

def example_plot_map(mapbox_access_token):
    # Put your mapbox token in variable of this name
    chicago_geodata_path = 'data/chicago-zip.json'
    
    # Only to get some data for example dataframe
    chicago_geodata = load_geodata(chicago_geodata_path)
    zips = [neighborhood['properties']['zip'] for neighborhood in chicago_geodata['features']]
    
    # Create example dataframe
    df = pd.DataFrame({'zips': zips, 'values': zips, 'var1': np.arange(0, len(zips)), 'var2': np.arange(1, len(zips)+1)})
    
    # Plot map
    plot_map('Chicago Neighborhoods', chicago_geodata_path, df, 'zips', 'values', 'Some {} text {}', mapbox_access_token)