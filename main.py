import streamlit as st
import langchain_helper

st.title("\t\tSIVANI-AI")

st.header("Your Personal Helper in Cooking")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))
print(cuisine)
if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.write("**Menu Items**")
    st.write(response['dish'].strip())


temp = st.sidebar.text_input("Enter name of a dish to get recipe and history:")
print(temp)

if temp:
    res = langchain_helper.generate_recipe(temp)
    st.write("**Recipe**")
    st.write(res['a'].strip())
    #st.write("\n\n**More about the Dish:**")
    #st.write(res['b'].strip())






