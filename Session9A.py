"""
    Song: title, artist, duration, next_song, previous_song
"""

class Song:

    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next_song = None
        self.previous_song = None

    def show_song(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('Title:', self.title)
        print('Artist:', self.artist)
        print('Duration:', self.duration)
        print('HashCode:', self)
        print('next_song:', self.next_song)
        print('previous_song:', self.previous_song)
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


song1 = Song(title='1. Jaan Se Guzarte Hain', 
             artist='Shashwat Sachdev, Khan Saab, Irshad Kamil', 
             duration=4.5)

song2 = Song(title='2. Deewaana Deewaana', 
             artist='A. R. Rahman, Irshad Kamil', 
             duration=3.5)

song3 = Song(title='3. Boom Shaka', 
             artist='KR$NA, Dhanda Nyoliwala', 
             duration=4.0)

song4 = Song(title='4. Gehra Hua', 
             artist='Shashwat Sachdev, Arijit Singh, Irshad Kamil', 
             duration=5.2)

song5 = Song(title='5. Sitaare', 
             artist='Arijit Singh, Amitabh Bhattacharya, Sachin-Jigar', 
             duration=4.3)

# Hard Coded the Songs for next and previous
song1.next_song = song2
song2.next_song = song3
song3.next_song = song4
song4.next_song = song5
song5.next_song = song1

song1.previous_song = song5
song2.previous_song = song1
song3.previous_song = song2
song4.previous_song = song3
song5.previous_song = song4


# Hard Coded the way to display songs
# song1.show_song()
# song2.show_song()
# song3.show_song()
# song4.show_song() # song4.show_song() -> Song.show_song(song1)
# Song.show_song(song5) # access the function with class name

# Traversing in forward direction
song = song1

while True:
    song.show_song()
    song = song.next_song

    if song == song1:
        break


print('------------------------------------')

# Traversing in backward direction
song = song5

while True:
    song.show_song()
    song = song.previous_song

    if song == song5:
        break

