import csv
import json

import pandas as pd
import requests
import numpy as np
from bs4 import BeautifulSoup


API_KEY = "AIzaSyAjyXSklcymbkfoyRY0VifsWEG3jDIx_yY"
DATASET_FILEPATH = "/home/jczestochowska/workspace/ada/chicago_food/google_places_api_query_parameters.csv"
RESUME_FROM = 0

query_params = pd.read_csv(DATASET_FILEPATH)
query_params.iloc[RESUME_FROM:]

restaurants_csv = open("/home/jczestochowska/workspace/ada/chicago_food/restaurants.csv", 'w', newline='\n')
restaurants_writer = csv.writer(restaurants_csv, delimiter=',')
google_places_csv = open("/home/jczestochowska/workspace/ada/chicago_food/google_places.csv", 'w', newline='\n')
google_places_writer = csv.writer(google_places_csv, delimiter=',')

# writer header rows with column names
restaurants_writer.writerow(["place_id", "place_name", "latitude", "longitude", "address", "zip_code"])
google_places_writer.writerow(["place_id", "place_name", "rating", "total_number_of_ratings",
                               "price_level", "address", "city", "zip_code"])


try:
    for idx, row in query_params.iterrows():
        place_name = row["DBA Name"]
        latitude = row["Latitude"]
        longitude = row["Longitude"]
        inspections_address = row["Address"]
        zip_code = row["Zip"]
        if not np.isnan(zip_code):
            zip_code = int(zip_code)
        # set default chicago coordinates
        if np.isnan(latitude):
            latitude = 41.8781
        elif np.isnan(longitude):
            longitude = -87.6298

        # get place id using name and coordinates from chicago inspections
        place_id_response = requests.get(
            f"https://maps.googleapis.com/maps/api/place/findplacefromtext/json?key={API_KEY}&input={place_name}&inputtype=textquery&locationbias=point:{latitude},{longitude}")
        place_id_json = json.loads(place_id_response.text)

        if place_id_response.status_code != 200:
            print(f"Got status code: {place_id_response.status_code} for querying place id, place name: {place_name}")
        elif len(place_id_json['candidates']) == 0:
            print(f"No such place in google places API {place_name}")
        else:
            # we use only the first candidate
            place_id = place_id_json['candidates'][0]['place_id']

            # get place details using id from previous step
            place_details = requests.get(
                f"https://maps.googleapis.com/maps/api/place/details/json?key={API_KEY}&place_id={place_id}&fields=name,adr_address,rating,user_ratings_total,price_level"
            )

            if place_details.status_code != 200:
                print(f"Got status code {place_details.status_code} for place id: {place_id}, place name: {place_name}")
            else:
                place_details = json.loads(place_details.text)['result']
                # address value is an html snippet
                html_address = place_details['adr_address']
                soup = BeautifulSoup(html_address, 'html.parser')
                address_fields = [s.string.lower() for s in
                                  soup.find_all('span', {'class': ['street-address', 'locality', 'postal-code']})]

                restaurants_writer.writerow([place_id, place_name, latitude, longitude, inspections_address, zip_code])
                google_places_writer.writerow([place_id,
                                               place_details.get('name', '').lower(),
                                               place_details.get('rating', np.nan),
                                               place_details.get('user_ratings_total', np.nan),
                                               place_details.get('price_level', np.nan),
                                               *address_fields])
                print(f"Added new row {idx}, {place_name}, {place_id}")
except Exception:
    print("=======Something went wrong=======")
    google_places_csv.close()
    restaurants_csv.close()

google_places_csv.close()
restaurants_csv.close()