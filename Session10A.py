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

    def deduct_toll(self, element):
        pass

    def delete(self, element):
        self.size -= 1
        self.head = self.head.next

    
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

    