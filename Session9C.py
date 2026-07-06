# class SongList:
class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        print('[CircularDoublyLinkedList] [init] Object Constrcuted', self)


    def add(self, element):
        
        self.size += 1

        if self.head == None:
            self.head = element
            self.tail = element
        else:
            self.tail.next_song = element
            self.head.previous_song = element
            element.previous_song = self.tail
            element.next_song = self.head
            self.tail = element

    def add_in_front(self, element):
        pass

    def add_in_between(self, element, element1, element2):
        pass

    def delete_last():
        pass

    def delete_front():
        pass

    def delete(element):
        pass

    def show(self, traverse=True):
        
        if traverse == True:
        
            song = self.head

            while True:
                song.show_song()
                song = song.next_song

                if song == self.head:
                    break
        
        else:

            song = self.tail

            while True:
                song.show_song()
                song = song.previous_song

                if song == self.tail:
                    break

    





