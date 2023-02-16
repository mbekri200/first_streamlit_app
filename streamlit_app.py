import streamlit
import pandas
import requests

streamlit.title('My parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🍲 Omega3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spnach & Rocket Smoothie')
streamlit.text('🍗Hard-Boiled  Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')



#put a pick list so they can pick the fruit they want to include

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruit_to_show=my_fruit_list.loc[fruits_selected]
#display the table on the page
streamlit.dataframe(fruit_to_show)

##########################"
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+"kiwi")
#streamlit.text(fruityvice_response.json())
streamlit.header("Fruityvice Fruit Advice!")

fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_normalized)

##############################
fruit_choice=steamlit.text_input('what fruit would you like information about?','Kiwi')
streamlit.write('The use entered', fruit_choice)
