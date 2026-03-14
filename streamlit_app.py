import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["api_key"])

def get_standard_response(system_prompt, user_prompt):
    """
    Sends a prompt to the ChatGPT API where it will return a standard response.
    ChatGPT will not remember any prior conversations.

    Parameters:
    - system_prompt (str): Directions on how ChatGPT should act.
    - user_prompt (str): A prompt from the user.

    Returns:
    - (str): ChatGPT's response.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content

with st.form("Language form"):
    out_lang = st.selectbox("What languge do you want to output?",[
        "English", "Spanish", "Chinese", "French", "German", "Italian", "Swedish"
    ])
    inp = st.text_input("Put your text to be translated here!")

    press = st.form_submit_button("Click me to translate your text!")

    if press:
        st.write(get_standard_response("You are a translater, the user will input text in any language. You will output it in the user's chosen output language.", "This is the language to translate to: ", out_lang, ". This is the user's inputed text: ", inp))
