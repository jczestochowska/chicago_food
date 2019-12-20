import copy
import os
import re
import json
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def insert_variables_as_properties_in_geodata(geodata, dataframe, key_property, key_column, variable_names):
    output_geodata = copy.deepcopy(geodata)
    
    for feature in output_geodata['features']:
        key = feature['properties'][key_property]
        row = dataframe[dataframe[key_column] == key]

        if not row.empty:
            variables_values = row[variable_names].values[0]
            for name, value in zip(variable_names, variables_values):
                feature['properties'][name] = str(value)
    
    return output_geodata

def format_template(template, variable_names):
    replaced = copy.deepcopy(template)
    for name in variable_names:
        replaced = re.sub(r'\{\}', '%{properties.' + name + '}', replaced, count=1)
    return replaced

def load_geodata(geodata_path, key_property):
    with open(os.path.join(geodata_path)) as geojson_file:
        geodata = json.loads(geojson_file.read())
        # add id feature for choroplethmapbox
        for feature in geodata['features']:
            feature['id'] = feature['properties'][key_property]
        return geodata

def plot_map(title, geodata_path, dataframe, key_property, key_column, value_column, template, mapbox_access_token, options):
    # unpack options
    colorscale = options['colorscale'] if 'colorscale' in options else 'Viridis'
    colorbar = options['colorbar'] if 'colorbar' in options else {}
    showscale = options['showscale'] if 'showscale' in options else True
    
    # load geodata
    geodata = load_geodata(geodata_path, key_property)
    
    # prepare data
    columns = dataframe.columns.values
    dropped_columns = set([key_column, value_column])
    variable_names = [column for column in columns if column not in dropped_columns]
    extended_geodata = insert_variables_as_properties_in_geodata(geodata, dataframe, key_property, key_column, variable_names)
    formatted_template = format_template(template, variable_names) + '<extra></extra>'
    
    # plot
    figure = go.Figure(go.Choroplethmapbox(
        geojson=extended_geodata,
        locations=dataframe[key_column],
        z=dataframe[value_column],
        hovertemplate=formatted_template,
        showscale=showscale,
        colorscale=colorscale,
        colorbar=colorbar
    ))
    figure.update_layout(
        title=title,
        font={'family': 'Arial Black'},
        mapbox_accesstoken=mapbox_access_token,
        mapbox_zoom=9,
        mapbox_pitch=0,
        mapbox_bearing=0,
        mapbox_center={'lat': 41.86, 'lon': -87.63},
        margin={'r': 0, 'l': 50, 't': 50, 'b': 0}
    )
    return figure

class MapLayer():
    def __init__(self, name, dataframe, key_column, value_column, options):
        self.name = name
        self.dataframe = dataframe
        self.key_column = key_column
        self.value_column = value_column
        self.options = options

# Implementation based on: https://plot.ly/~empet/15237/choroplethmapbox-with-dropdown-menu/#/
def plot_maps(title, geodata_path, key_property, layers, template, mapbox_access_token, options):    
    # load geodata
    geodata = load_geodata(geodata_path, key_property)
    
    data = []
    for layer in layers:
        # extract variables
        dataframe = layer.dataframe
        key_column = layer.key_column
        value_column = layer.value_column
        # unpack options
        colorscale = layer.options['colorscale'] if 'colorscale' in options else 'Viridis'
        colorbar = layer.options['colorbar'] if 'colorbar' in options else {}
        showscale = layer.options['showscale'] if 'showscale' in options else True
        
        # prepare data
        columns = dataframe.columns.values
        dropped_columns = set([key_column, value_column])
        variable_names = [column for column in columns if column not in dropped_columns]
        extended_geodata = insert_variables_as_properties_in_geodata(geodata, dataframe, key_property, key_column, variable_names)
        formatted_template = format_template(template, variable_names) + '<extra></extra>'
    
        # plot
        figure = go.Figure()
        data.append(go.Choroplethmapbox(
            geojson=extended_geodata,
            locations=dataframe[key_column],
            z=dataframe[value_column],
            hovertemplate=formatted_template,
            showscale=showscale,
            colorscale=colorscale,
            colorbar=colorbar,
            visible=False
        ))
    
    # mark first layer as visible
    data[0]['visible'] = True
    
    # create layout
    layout = go.Layout(
        title=title,
        font={'family': 'Arial Black'},
        mapbox_accesstoken=mapbox_access_token,
        mapbox_zoom=9,
        mapbox_pitch=0,
        mapbox_bearing=0,
        mapbox_center={'lat': 41.86, 'lon': -87.63},
        margin={'r': 0, 'l': 50, 't': 50, 'b': 0}
        
    )
    
    # create layers visibility lists
    visibilities = []
    template_visibility = np.zeros((len(layers),)).astype(bool)
    for i in range(len(layers)):
        visibility = list(np.copy(template_visibility))
        visibility[i] = True
        visibilities.append(visibility)
    
    # create menu buttons
    buttons = []
    for i, layer in enumerate(layers):
        buttons.append({
            'args': ['visible', visibilities[i]],
            'label': layer.name,
            'method': 'restyle'
        })
    
    # update layout adding menu
    layout.update(
        updatemenus=[{
            'x': 0.95,
            'y': 0.95,
            'yanchor': 'top',
            'buttons': buttons
        }]
    )
    
    figure = go.Figure(data=data, layout=layout)
    return figure

def plot_maps_sliders(title, geodata_path, key_property, layers, template, mapbox_access_token, options):    
    # load geodata
    geodata = load_geodata(geodata_path, key_property)
    
    data = []
    for layer in layers:
        # extract variables
        dataframe = layer.dataframe
        key_column = layer.key_column
        value_column = layer.value_column
        # unpack options
        colorscale = layer.options['colorscale'] if 'colorscale' in options else 'Viridis'
        colorbar = layer.options['colorbar'] if 'colorbar' in options else {}
        showscale = layer.options['showscale'] if 'showscale' in options else True
        
        # prepare data
        columns = dataframe.columns.values
        dropped_columns = set([key_column, value_column])
        variable_names = [column for column in columns if column not in dropped_columns]
        extended_geodata = insert_variables_as_properties_in_geodata(geodata, dataframe, key_property, key_column, variable_names)
        formatted_template = format_template(template, variable_names) + '<extra></extra>'
    
        # plot
        figure = go.Figure()
        data.append(go.Choroplethmapbox(
            geojson=extended_geodata,
            locations=dataframe[key_column],
            z=dataframe[value_column],
            hovertemplate=formatted_template,
            showscale=showscale,
            colorscale=colorscale,
            colorbar=colorbar,
            visible=False
        ))
    
    # mark first layer as visible
    data[0]['visible'] = True
    
    # create layout
    layout = go.Layout(
        title=title,
        font={'family': 'Arial Black'},
        mapbox_accesstoken=mapbox_access_token,
        mapbox_zoom=9,
        mapbox_pitch=0,
        mapbox_bearing=0,
        mapbox_center={'lat': 41.86, 'lon': -87.63},
        margin={'r': 0, 'l': 50, 't': 50, 'b': 0}
        
    )
    
    # create layers visibility lists
    visibilities = []
    template_visibility = np.zeros((len(layers),)).astype(bool)
    for i in range(len(layers)):
        visibility = list(np.copy(template_visibility))
        visibility[i] = True
        visibilities.append(visibility)
    
    # Create and add slider
    steps = []
    for i, layer in enumerate(layers):
        step = {
            'method': 'restyle',
            'args': ['visible', visibilities[i]],
            'label': layer.name
        }
        steps.append(step)

    sliders = [{
        'active': 0,
        'currentvalue': {'prefix': 'Year: '},
        'pad': {'t': 50},
        'steps': steps
    }]

    layout.update(
        sliders=sliders
    )
    
    figure = go.Figure(data=data, layout=layout)
    return figure