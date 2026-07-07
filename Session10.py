"""
    DSA - 3 questions a day (Competitive Platform)
    Design Patterns - https://refactoring.guru/design-patterns
    SOLID Principles - https://www.designgurus.io/course-play/grokking-solid-design-principles/doc/solid-design-principles
"""

# Vehicle: registration_number, type, fasttag
# FastTag: fasttag_id, bank, balance

# 1 Vehicle has 1 FastTag

class FastTag:
    
    def __init__(self, fasttag_id, bank, balance):
        self.fasttag_id = fasttag_id
        self.bank = bank
        self.balance = balance

    def show(self):
        print('~~~~~~~~~~~FAST TAG~~~~~~~~~~~~~')
        print(f'{self.fasttag_id} | {self.bank} | {self.balance}') # formatted string
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


class Vehicle: 
    
    def __init__(self, registration_number, type, fasttag):
        self.registration_number = registration_number 
        self.type = type
        self.fasttag = fasttag
        # self.next = None
        # self.previous = None

    def show(self):
        print('~~~~~~~~~~~VEHICLE~~~~~~~~~~~~~')
        print(f'{self.registration_number} | {self.type}') # formatted string


        # data = vars(self) # vars(self) -> data of obect in dictionary format
        print('{registration_number} | {type}'.format_map(vars(self)))

        self.fasttag.show()

        # print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        print('~'*30 +'\n')



