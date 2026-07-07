class TollPlazaQueue:
    
    def __init__(self):
        self.head = None    # for queue term is front
        self.tail = None    # for queue term is end
        self.size = 0
        print('[TollPlazaQueue] [init] Queue Constrcuted', self)


    def add(self, element):
        
        self.size += 1

        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next = element
            self.head.previous = element
            element.previous = self.tail
            element.next = self.head
            self.tail = element

        print(f'Vehcile Added to Queue. Size {self.size}')
        element.show()

    def deduct_toll(self, element):
        
        print(f'FastTag Balance for {element.registration_number} \u20b9{element.fasttag.balance}')        
        if element.type == '4W':
            element.fasttag.balance -= 100
        else:
            element.fasttag.balance -= 50

        print(f'Toll Deducted')        
        print(f'New FastTag Balance for {element.registration_number} \u20b9{element.fasttag.balance}')  

        self.delete()

    def delete(self):
        self.size -= 1
        self.head = self.head.next
        print(f'Vehicle Removed from Queue. Size {self.size}')

    def delete(self):
        self.size -= 1
        self.tail = self.tail.previous
        print(f'Vehicle Removed from Stack. Size {self.size}')
    
    def show(self, traverse=True):
        
        if traverse == True:
        
            element = self.head

            while True:
                element.show()
                element = element.next

                if element == self.head:
                    break
        
        else:

            element = self.tail

            while True:
                element.show()
                element = element.previous

                if element == self.tail:
                    break

    