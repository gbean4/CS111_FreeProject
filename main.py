#using this code to deploy my to do list model

import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

st.title('My To Do List')
st.subheader('This is your to do list for the day. Feel free to add new tasks and check off completed ones. Ka-ching!')
st.write("When you're done, click the 'Save' button to save your progress.")

canvas = pd.read_csv('canvas.csv')

if st.button("Save"):
    canvas.to_csv('canvas.csv', index=False)
    st.success("Data saved successfully!")

today_date = st.date_input("Today's date:", value="today", format="YYYY/MM/DD")
formated_today = datetime.strptime(today_date, "%m/%d/%Y")
# @st.cache(allow_output_mutation=True)
def get_data():
    return []

for i, row in canvas.iterrows():
    if row['dtstart'] > formated_today:
        st.write(f"Overdue:")
        checked = st.checkbox(row['summary'], key=f"check_{i}")
        canvas.at[i, 'status'] = 'T' if checked else 'F'
    else:
        st.write(f"Upcoming:")
        checked = st.checkbox(row['summary'], key=f"check_{i}")
        canvas.at[i, 'status'] = 'T' if checked else 'F'

# st.write(canvas)



# for item in canvas['summary']:
#     st.checkbox(item)
#     if st.checkbox(item):
#         canvas.at[canvas['summary'] == item, 'status'] = 'T'

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