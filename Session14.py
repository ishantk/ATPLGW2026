import streamlit as st

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
            st.markdown(message['text'])

    else:

        message = {
            'role': 'assistant',
            'text': 'Sorry, I cannot Help You'
        }
        st.session_state.messages.append(message)

        with st.chat_message(message['role']):
            st.markdown(message['text'])
