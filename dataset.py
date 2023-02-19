import streamlit as st
import requests


@st.cache_data
def get_clinic_data(zipcode):
    url = f'https://data.cityofnewyork.us/resource/8nqg-ia7v.json?zip={zipcode}'
    response = requests.get(url)

    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Convert the response to a JSON object
        st.markdown("# Results:")

        for clinic in data:
            st.markdown(
                '<div style="border: 1px solid black; padding: 10px; border-radius: 5px;">'
                f"{clinic['name_1']}{', ' + clinic['name_2'] if 'name_2' in clinic else ''}"'<br>'
                f"{clinic['street_1']}{', ' + clinic['street_2'] if 'street_2' in clinic else ''}"'<br>'
                f"{clinic['city']}{', ' + clinic['zip']}"'<br>'
                f"{clinic['phone'] if 'phone' in clinic else ''}"'<br>'
                f"{'<a href=' + clinic['website'] + '>' + clinic['website'] + '</a >' if 'website' in clinic else ''}"
                '</div>',
                unsafe_allow_html=True
            )
            st.write("")

    else:
        print("Request failed with status code:", response.status_code)