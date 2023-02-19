import streamlit as st
import dataset as ds

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.write("Welcome to the Extra Mental Health Resources \n Please input your information below.")

with st.form("user_input_form"):
   st.write("Please input your information accurately.")
   zip_code_info = st.number_input("Your zipcode:", 9999,15000, value = 10003, key = "zipcode")
   medium_preference = st.selectbox("Pick your preferred medium:", ["Virtual", "In-person"], key = "medium")
   insurance_provider = st.text_input("Type in your insurance provider's name (Leave Blank if not insured)", key = "insurance")
   issue_info = st.multiselect("What issues plague you?", ["Depression", "Anxiety", "Stress", "Dietary Concerns"], key = "issue")

   assent_checkbox_val = st.checkbox("By submitting, you agree that your information will only be used for searching for resources and will not be saved.", value=False, key = "acceptance")

   submitted = st.form_submit_button("Submit")


if submitted:
   ds.get_clinic_data(zipcode = st.session_state.zipcode);
