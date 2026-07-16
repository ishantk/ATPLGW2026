import time
import datetime
import json
from Session13 import DBHelper
from openai import OpenAI
import streamlit as st

st.set_page_config(page_title='Agentic Chat UI')
st.subheader('Write a Task to Delegate')

# DB Initialization
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')

# OpenAI Initialization
openai_api_key=open('apikey.txt', 'r').read().strip()
client = OpenAI(api_key=openai_api_key)

def save_task(task):
     # Adding 2 more keys in task
     task['status'] = 'PENDING'
     task['created_at'] = datetime.datetime.now()
     db_helper.save(task)
     return 'Task saved successfully'

# 2. Define a list of callable tools for the model
tools = [
    {
        "type": "function",
        "name": "save_task",
        "description": "Save the task in MongoDB Atlas",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Title of the Task",
                },
                "description": {
                    "type": "string",
                    "description": "Description of the Task",
                },
                "action": {
                    "type": "string",
                    "description": "Action of the Task can be call, message or email",
                },
                "contact_name": {
                    "type": "string",
                    "description": "Name of the contact person who will perfrom this Task",
                },
                "contact_phone": {
                    "type": "string",
                    "description": "Phone of the person who will perfrom this Task",
                }
            },
            "required": ["title", "description", "action", "contact_name", "contact_phone"],
        },
    },
]

# Create a temporary list of messages in Streamlit Session
# session_state its a dictionary
# we created a key messages in the session_state dictionary, whose value is a list of dictionaries
if 'messages' not in st.session_state:
    st.session_state.messages = []

# List all the previous messages stored in list
for message in st.session_state.messages:
     with st.chat_message(message['role']):
        st.markdown(message['content'])

user_input = st.chat_input('Type Your Task here')

if user_input:

    message = {
        'role': 'user',
        'content': user_input
    }

    st.session_state.messages.append(message)

    with st.chat_message(message['role']):
        st.markdown(message['content'])

    input_list = [
        {"role": "user", "content": user_input}
    ]

    # Prompt the model with tools defined
    response = client.responses.create(
        model="gpt-4o-mini",
        tools=tools,
        input=input_list,
    )  

    llm_output = response.model_dump_json(indent=2) # string
    print(llm_output)
    llm_output = json.loads(llm_output) # covert to dictionary
    arguments = json.loads(llm_output['output'][0]['arguments'])
    function_name = llm_output['output'][0]['name']
    type = llm_output['output'][0]['type']

    result = 'Sorry, I cannot process your request'

    if type == 'function_call':
        if function_name == 'save_task':
            result = save_task(arguments)
        elif function_name == 'update_task':
            pass
        elif function_name == 'delete_task':
            pass
        elif function_name == 'list_tasks':
            pass

        message = {
            'role': 'assistant',
            'content': result
        }

        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['content']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.01)

    

  
