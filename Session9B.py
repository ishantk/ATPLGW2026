class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next_song = None
        self.previous_song = None
        print('[Song] [init] Object Constrcuted', self)

    def show_song(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Title:', self.title)
        print('Artist:', self.artist)
        print('Duration:', self.duration)
        print('HashCode:', self)
        print('next_song:', self.next_song)
        print('previous_song:', self.previous_song)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')