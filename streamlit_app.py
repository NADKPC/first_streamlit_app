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
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(myfruitlist)

