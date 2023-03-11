import openai
import random
import string
import streamlit as st
from streamlit_chat import message
import os # for getting the key

# import the function to get response fron the user
from api import get_promt_based_on_TA_feedback
from db import populate_ta_feedback

from dotenv import load_dotenv
load_dotenv()
# set the key
openai.api_key = f"{os.getenv('OPENAI_GPT_KEY')}"

#set the title for the app
st.title("Teachers Bot QA")
#
# # We will get the user's input by calling the get_text function
def get_text():
    input_text = st.text_input("Message>: ", key="input")
    return input_text
#

user_input = get_text()

# starter bot prompt
bot_prompt = "What topics did you cover?"


# to get unique ID as key for the message
key = random.choice(string.ascii_uppercase)+str(random.randint(0,999999))
message(f"{bot_prompt}", key=f'chat_{key}_bot')

if st.button("Send"):
    if user_input =="":
        pass
    else:
        #use the user generated response to get another prompt
        res =get_promt_based_on_TA_feedback(user_input)
        key = random.choice(string.ascii_uppercase)+str(random.randint(0,999999))
        message(f"{user_input}", is_user=True, key=f'chat_{key}_user')
        message(f"{res}", key=f'chat_{key}_bot')

        #add these data to the Database
        try:
            populate_ta_feedback(f"{res}", f"{user_input}")
        except:
            pass
