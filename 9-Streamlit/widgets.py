import streamlit as st
import pandas as pd

st.title("Stramlit Text input")

name = st.text_input("Enter your name: ")
if name:
    st.write(f"Hello, {name}")
    
age = st.slider("Select your age:", 0,100,25)
st.write(f"Your age is {age}.")

options = ["Java", "C", "C++", "Python", "Ruby"]
choice = st.selectbox("Choose your favourite language:  ", options)
st.write(f"You selected {choice}.")

if name:
    st.write(f"Hello, {name}")
    
data = {
    "Name": ["Ujjwal", "Kaushal", "Jack", "Jill"],
    "Age": [21, 24, 25, 40],
    "City": ["India", "LA", "San" ,"Budapest"]
}

df = pd.DataFrame(data)
df.to_csv("sample_data.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a csv file: ", type = "csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)