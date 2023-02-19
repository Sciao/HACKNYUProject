import streamlit as st
import dataset as ds

st.markdown("All You Need for Mental Health Help")
st.sidebar.markdown("Home")

st.write("Welcome to the Extra Mental Health Resources. To be best matched with avaliable resources, please input your information below.")

with st.form("user_input_form"):
   st.write("Please fill in the following fields accurately")

   age_info = st.number_input("Please indicate your age. If you are underage, please seek assistance from your parent or legal guardian", min_value=0)

   issue_info = st.multiselect("Please select what issues you are having:", ["Depression", "Anxiety", "Stress", "Dietary Concerns"], key = "issue")

   zip_code_info = st.number_input("What is your geographic location by zipcode? (NY is in the range of 10000-15000)", 9999,15000, value = 9999, key = "zipcode")

   medium_preference = st.selectbox("Please select your preferred sesssion medium:", ["Virtual", "In-person"], key = "medium")

   insurance_provider = st.text_input("Type in your insurance provider's name (Leave Blank if not insured)", key = "insurance")

   assent_checkbox_val = st.checkbox("By submitting, you agree that your information will only be used for searching for resources and will not be saved.", value=False, key = "acceptance")
   
   submitted = st.form_submit_button("Submit")

if submitted:
   ds.get_clinic_data(zipcode = st.session_state.zipcode);
