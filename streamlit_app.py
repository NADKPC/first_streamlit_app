import streamlit

streamlit.title('my Parents new healthy Diner')

streamlit.header('breakfast menu')
streamlit.text('🥣 Meal 1')
streamlit.text('🥗 Meal 2')
streamlit.text('🐔Meal 3')
streamlit.text('🥑🍞Meal 3')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
myfruitlist=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(myfruitlist)

