import streamlit as st
import time
import datetime
from Session13 import DBHelper

"""

Task Delegation

Hello Gourav, create 3 licenses for Finlo's Bus Ticketing for Jujhar Group
Agent1 -> Save the Task (pending)

create task: Create 3 liceneses for finlo, Create licenses on immediate basis for Jujhar Group for bus ticketing, call, Gourav, 9915571177

Agent2 -> Action to call/email etc
Agent3 -> Save the response from Gourav and update the status of task accordingly
Agent4 -> Gives me analysis of what and all has been done

"""

st.set_page_config(page_title='Agentic Chat UI')
st.subheader('Write a Task to Delegate')
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')

task_clues = {
    'how to create a task': 'create task: title, description, action(call etc), contact_name, contact_phone',
    'how to view tasks': 'list all tasks',
    'how to update task': 'update task:  title, description, action(call etc), contact_name, contact_phone',
    'how to delete task': 'delete task: title',
}

# Create a temporary list of messages in Streamlit Session
# session_state its a dictionary
# we created a key messages in the session_state dictionary, whose value is a list of dictionaries
if 'messages' not in st.session_state:
    st.session_state.messages = []


# List all the previous messages stored in list
for message in st.session_state.messages:
     with st.chat_message(message['role']):
        st.markdown(message['text'])

user_input = st.chat_input('Type Your Task here')

if user_input:

    message = {
        'role': 'user',
        'text': user_input
    }

    st.session_state.messages.append(message)

    with st.chat_message(message['role']):
        st.markdown(message['text'])

    if user_input in task_clues:
        clue = task_clues[user_input]

        message = {
            'role': 'assistant',
            'text': clue
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.01)

    elif 'create task:' in user_input:
        # save the task in mongodb
        data1 = user_input.split(':')
        data2 = data1[1].split(',')
        task = {
            'title': data2[0].strip(),
            'description': data2[1].strip(),
            'action': data2[2].strip(),
            'contact_name': data2[3].strip(),
            'contact_phone': data2[4].strip(),
            'status': 'PENDING',
            'created_at': datetime.datetime.now()
        }

        db_helper.save(task)
        message = {
            'role': 'assistant',
            'text': 'Task Saved Successfully.'
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
    
    elif 'list:' in user_input:
        documents = db_helper.retrieve()
        # display all documents by concatenating string using json dumps

    elif 'update:' in user_input:
        pass

    elif 'delete:' in user_input:
        pass

    else:

        message = {
            'role': 'assistant',
            'text': 'Sorry, I cannot Help You'
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            typing_placeholder = st.empty()
            typing_text = ''
            for character in message['text']:
                typing_text += character
                typing_placeholder.markdown(typing_text)
                time.sleep(0.05)
