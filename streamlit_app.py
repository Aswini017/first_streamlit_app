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
streamlit.dataframe(my_fruit_list)
