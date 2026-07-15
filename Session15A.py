"""
    Function Tooling in AI

    Streamlit UI Input: 
    Call gourav on 9872898728 and assign a task to create 3 licenses for finlo for bus ticketing module for Jujhar group

    
    Sequential Steps
    1. function to save task (mongidb insert)
    2. tool for Agentic Use
    3. Streamlit UI, where user will prompt to perfrom some action
    4. based on the user input, we will request open ai LLM to 
        give us the function alongwith arguments to be passed
    5. based on the outpup of LLM model, we will execute the function 
        with arguments
    6. we will execute the function, and share the output to the user on streamlit

"""

from Session13 import DBHelper
import datetime

# DB Initialization
db_helper = DBHelper()
db_helper.select_collection(collection_name='tasks')

# 1. Define a function to perfrom some action
def save_task(task):
     # Addint 2 more keys in task
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