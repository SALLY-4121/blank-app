import streamlit as st
from openai import OpenAI
import json

client = OpenAI(api_key=st.secrets["api_key"])
s = ("""You are an organisation helper. You will be given a block of text and you must create tasks according to the priotities of the user, 
     or in whichevery order you think is most suitible. You will create tasks with a title, and description for the user, 
     with a star rating of 1 - 5 based on it's importance, 1 is least important, 5 is most. Return only in JSON format with the following template
     { 'title': {'desc':'description here', star:1}
     }
     """)
   
if "task" not in st.session_state:
    st.session_state["task"]=[]
if "chat" not in st.session_state:
    st.session_state["chat"]=[{"role": "system", "content": s}]
with st.form("Task form"):
    user_input = st.text_area("Paste or type the tasks you wish to generate")

    press = st.form_submit_button("Click me to generate your tasks!")

    if press:
        st.session_state['chat'].append({'role':'user','content':user_input})
        response = client.chat.completions.create(
    model="gpt-4o",
    response_format={'type':'json_object'},
    messages=st.session_state["chat"]
)
        st.write(json.loads(response.choices[0].message.content))
        st.session_state['chat'].append({'role':'user','content':response.choices[0].message.content})