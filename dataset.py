import streamlit as st
import requests


@st.cache_data
def get_clinic_data(zipcode):
    url = f'https://data.cityofnewyork.us/resource/8nqg-ia7v.json?zip={zipcode}'
    response = requests.get(url)

    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert the response to a JSON object

        for clinic in data:
            st.write(f"{clinic['name_1']} {', ' + clinic['name_2'] if 'name_2' in clinic else ''}")
            st.write(f"{clinic['street_1']} {', ' + clinic['street_2'] if 'street_2' in clinic else ''}")
            st.write(f"{clinic['city']} {', ' + clinic['zip']}")
            st.write(f"{clinic['phone'] if 'phone' in clinic else ''} {', ' + clinic['website'] if 'website' in clinic else ''}")

    else:
        print("Request failed with status code:", response.status_code)


get_clinic_data('10010')
