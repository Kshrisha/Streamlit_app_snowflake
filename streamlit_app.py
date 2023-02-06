#create main python file
import streamlit
import pandas

streamlit.title('New movie play list')

streamlit.header(':calendar: Hollywood :movie_camera:')
streamlit.text('🎞️ Secret life of milley walter')
streamlit.text('🎬 Silent Voice')
streamlit.text('📹 The space between us')
streamlit.text('📽️ Upside down')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
