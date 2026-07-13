from Session13 import DBHelper

def main():
    
    db = DBHelper()
    db.select_collection()
    
    # condition = {'email' : 'vp@gmail.com'}
    condition = {
        'name' : 'Vanshika',
        'email' : 'vp@gmail.com'}
    
    # Assignment: Explore Operators in MongoDB eg: age is greater than 12 and less then 20

    # db.retrieve(condition)

    condition = {'email' : 'john@example.com'}
    document_to_update = {
        'name': 'John Jackson',
        'phone': '+91 99119 99119'
    }

    db.update(condition=condition, document_to_update=document_to_update)

    # condition = {'name':'VP', 'email' : 'vp@gmail.com'}
    # db.delete(condition=condition)

if __name__ == '__main__':
    main()