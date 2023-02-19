# HackNYU2023 Project: Extra Mental Health References for NYU Students

Team Members: Oona Zhou, Jade Wang, Shiva Kansagara, Brandon Chao

## Note this is the back-end portion of our Hackathon Submission

We were unable to connect our front end and back end in time. [Front End Link](http://137.184.101.56/hackathon-2023/)

## Project Description:

Track: Healthcare & Wellbeing

Our problem we set out to solve was: frustrations with NYU's student health centre in providng mental health support in a timely manner. To try to alleviate this issue for other students, we wanted to create an accessible tool that compiles other mental health resources around the NYC area. This would include tailoring to students' specific needs, location and insurance coverage. 

## Project Instructions (Linux):

Since we had used the Python module "Streamlit" to assist in creating the front-end rendering of our database, our project requires its installation.

First we need to setup a virtual envirnoment in the project folder through ```pip install pipenv``` and ```pipenv shell```.

Then we install streamlit with: ```pip install streamlit```.

Finally, run our "main_page" file in the project directory with: ```streamlit run main_page.py```

The basic instructions for installing streamlit can be found [here](https://docs.streamlit.io/library/get-started/installation) (for windows users), the final run instruction is the same as above. 

## Using the Form

For the prospective student, they would fill in the appropriate fields in the form and hit the submit button. The results would be the best match for the student's information, but currently it is default to match zipcode. 

## Mental Health Dataset Used

[Link](https://data.cityofnewyork.us/Health/Mental-Health-Service-Finder-Data/8nqg-ia7v)
