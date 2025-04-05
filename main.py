#using this code to deploy my to do list model

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

st.title('My To Do List')
st.subheader('This is your to do list for the day. Feel free to add new tasks and check off completed ones. Ka-ching!')

canvas = pd.read_csv('canvas.csv')
today_date = st.date_input("Enter today's date:", value="today", format="YYYY/MM/DD")

for item in canvas['summary']:
    st.checkbox(item)

# for date, index, description, item in canvas.iterrows():
#     st.checkbox(item)
    # task = row['summary']
    # completed = row['Completed']
    # if st.checkbox(task, value=completed):
    #     canvas.at[index, 'Completed'] = True
    # else:
    #     canvas.at[index, 'Completed'] = False