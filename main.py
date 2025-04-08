#using this code to deploy my to do list model
#import libraries
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import random

#date input for the user to select the date
# st.write("Please select the date for your tasks:")
today_date = st.date_input("Today's date:", value="today", format="MM/DD/YYYY")
today_date = pd.to_datetime(today_date)


#top important intros
st.title('My To Do List')
st.subheader('This is your to do list for the day. Ka-ching!')
st.write("When you're done, click the 'Save' button to save your progress for next time.")

# canvas = pd.read_csv('canvas.csv') #read my csv
if 'canvas' not in st.session_state:
    st.session_state.canvas = pd.read_csv('canvas.csv')
    st.session_state.canvas['dtstart'] = pd.to_datetime(st.session_state.canvas['dtstart'])

# canvas = st.session_state.canvas.sort_values(by=['priority','dtstart'], ascending=[False,True])
canvas = st.session_state.canvas.sort_values(by='dtstart', ascending=True)
canvas['dtstart'] = pd.to_datetime(canvas['dtstart'])

#save button to update the csv 
if st.button("Save"):
    canvas.to_csv('canvas.csv', index=False)
    st.success("Data saved successfully!")

#add item to the list using title and due date
task_title = st.text_input("Add new task:", key = "task_title")
task_due_date = st.date_input("Due Date", value=today_date, format="MM/DD/YYYY")
task_due_date = pd.to_datetime(task_due_date)
# task_priority = st.selectbox("Priority", [3, 2, 1], format_func=lambda x: {3: "High", 2: "Medium", 1: "Low"}[x])
if st.button("Add Task"):
    if task_title:
        new_task = pd.DataFrame({'summary': [task_title], 'dtstart': [task_due_date], 'status': ['F'], 'uid': [f"event-assignment-{random.randint(1, 1000)}"]})
        st.session_state.canvas = pd.concat([canvas, new_task], ignore_index=True)
        st.success(f"Task '{task_title}' added successfully!")
        canvas = pd.concat([canvas, new_task], ignore_index=True)
        # canvas = canvas.sort_values(by=['priority','dtstart'], ascending=[False,True]).reset_index(drop=True)
        canvas = canvas.sort_values(by='dtstart', ascending=True).reset_index(drop=True)
    else:
        st.error("Please enter a task title.")

# sort by due date
st.write("### 🔴 Overdue")
for i, row in canvas[(canvas['dtstart'] < today_date) & (canvas['status'] != 'T')].iterrows():
        checked = st.checkbox(row['summary'], key=f"overdue_check_{i}", value=(row['status'] == 'T'))
        canvas.at[i, 'status'] = 'T' if checked else 'F'
st.write("### 🔵 Today")
for i, row in canvas[(canvas['dtstart'] == today_date) & (canvas['status'] != 'T')].iterrows():
        checked = st.checkbox(row['summary'], key=f"check_{i}")
        canvas.at[i, 'status'] = 'T'if checked else 'F'
st.write("### 🟢 Upcoming")
for i, row in canvas[(canvas['dtstart'] > today_date) & (canvas['status'] != 'T')].iterrows():
        checked = st.checkbox(row['summary'], key=f"check_{i}")
        canvas.at[i, 'status'] = 'T' if checked else 'F'
st.write("### ✅ Completed")
for i, row in canvas[canvas['status'] == 'T'].iterrows():
        checked = st.checkbox(f"~~{row['summary']}~~", value=True, key=f"completed_check_{i}")
        if not checked:
            canvas.at[i, 'status'] = 'F'