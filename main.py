#using this code to deploy my to do list model
#import libraries
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

#top important intros
st.title('My To Do List')
st.subheader('This is your to do list for the day. Feel free to add new tasks and check off completed ones. Ka-ching!')
st.write("When you're done, click the 'Save' button to save your progress.")

canvas = pd.read_csv('canvas.csv') #read my csv

#save button to update the csv 
if st.button("Save"):
    canvas.to_csv('canvas.csv', index=False)
    st.success("Data saved successfully!")

#date input for the user to select the date
st.write("Please select the date for your tasks:")
today_date = st.date_input("Today's date:", value="today", format="MM/DD/YYYY")
today_date = pd.to_datetime(today_date)
canvas['dtstart'] = pd.to_datetime(canvas['dtstart'])

#sort by due date
st.write("### 🔴 Overdue")
for i, row in canvas[(canvas['dtstart'] < today_date) & (canvas['status'] != 'T')].iterrows():
        checked = st.checkbox(row['summary'], key=f"overdue_check_{i}", value=(row['status'] == 'T'))
        canvas.at[i, 'status'] = 'T' if checked else 'F'
st.write("### 🔵 Today")
for i, row in canvas[(canvas['dtstart'] == today_date) & (canvas['status'] != 'T')].iterrows():
        checked = st.checkbox(row['summary'], key=f"check_{i}")
        canvas.at[i, 'status'] = 'T' if checked else 'F'
st.write("### 🟢 Upcoming")
for i, row in canvas[(canvas['dtstart'] > today_date) & (canvas['status'] != 'T')].iterrows():
        checked = st.checkbox(row['summary'], key=f"check_{i}")
        canvas.at[i, 'status'] = 'T' if checked else 'F'
st.write("### ✅ Completed")
for i, row in canvas[canvas['status'] == 'T'].iterrows():
        checked = st.checkbox(f"~~{row['summary']}~~", value=True, key=f"completed_check_{i}")
    # If the user unchecks the box, mark it as not completed
        if not checked:
            canvas.at[i, 'status'] = 'F'
        # st.checkbox(f"~~{row['summary']}~~", value=True, key=f"completed_check_{i}", disabled=True)
        # checked = st.checkbox(f"~~{row['summary']}~~", key=f"completed_check_{i}", value=True)
        # canvas.at[i, 'status'] = 'T' if checked else 'F' 
        
        # checked = st.checkbox(row['summary'], key=f"check_{i}", value=True)
        # canvas.at[i, 'status'] = 'T' if checked else 'F'

# separate my tasks by due date
# overdue = canvas[canvas['dtstart'] < today_date]
# today = canvas[canvas['dtstart'] == today_date]
# upcoming = canvas[canvas['dtstart'] > today_date]

#function to render tasks based on their status
# def render_tasks(tasks_df, section_title):
#     st.write(f"### {section_title}")
#     for i, row in tasks_df.iterrows():
#         checked = st.checkbox(row['summary'], key=f"check_{i}", value=(row['status'] == 'T'))
#         canvas.at[i, 'status'] = 'T' if checked else 'F'

# render_tasks(overdue[overdue['status'] != 'T'], "Overdue")
# render_tasks(today[today['status'] != 'T'], "Today")
# render_tasks(upcoming[upcoming['status'] != 'T'], "Upcoming")

# Show completed tasks
# completed = canvas[canvas['status'] == 'T']
# if not completed.empty:
#     st.write("### ✅ Completed")
#     for i, row in completed.iterrows():
#         st.checkbox(f"~~{row['summary']}~~", value=True, key=f"completed_{i}", disabled=True)






# st.write(canvas)

# for item in canvas['summary']:
#     st.checkbox(item)
#     if st.checkbox(item):
#         canvas.at[canvas['summary'] == item, 'status'] = 'T'

# @st.cache(allow_output_mutation=True)
# def get_data():
#     return []

# user_id = st.text_inp"User ID")
# foo = st.slider("foo", 0, 100)
# bar = st.slider("bar", 0, 100)

# if st.button("Add row"):
#     get_data().append({"UserID": user_id, "foo": foo, "bar": bar})

# st.write(pd.DataFrame(get_data()))

# for date, index, description, item in canvas.iterrows():
#     st.checkbox(item)
    # task = row['summary']
    # completed = row['Completed']
    # if st.checkbox(task, value=completed):
    #     canvas.at[index, 'Completed'] = True
    # else:
    #     canvas.at[index, 'Completed'] = False