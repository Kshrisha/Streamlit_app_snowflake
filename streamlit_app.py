#create main python file
import streamlit
import pandas

streamlit.title('New movie play list')

streamlit.header(':calendar: Hollywood :movie_camera:')
streamlit.text('🎞️ Secret life of milley walter')
streamlit.text('🎬 Silent Voice')
streamlit.text('📹 The space between us')
streamlit.text('📽️ Upside down')

# Display the table on the page.
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.header('Healthy fruits')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)
