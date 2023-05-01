import streamlit
streamlit.title('my mom new healthy diner')
streamlit.header('breakfast menu')
streamlit.text('🥣omege 3 and blueberry oatmeal')
streamlit.text('🥗kale,spinach & rocket smoothie')
streamlit.text('🐔hard_boiled free range egg')
streamlit.text('🥑🍞avacado toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.2))
# Display the table on the page
streamlit.dataframe(my_fruit_list)
