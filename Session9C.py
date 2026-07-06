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
            element.previous = self.tail
            element.next = self.head
            self.tail = element

    def show(self):
        song = self.head

        while True:
            song.show_song()
            song = song.next_song

            if song == self.head:
                break





