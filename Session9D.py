from Session9B import Song
from Session9C import CircularDoublyLinkedList

song_list = CircularDoublyLinkedList()
print(vars(song_list))



song1 = Song(title='1. Jaan Se Guzarte Hain', 
             artist='Shashwat Sachdev, Khan Saab, Irshad Kamil', 
             duration=4.5)
print(vars(song1))

song_list.add(song1)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After addition of 1st song')
print(vars(song_list))
print(vars(song1))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

song2 = Song(title='2. Deewaana Deewaana', 
             artist='A. R. Rahman, Irshad Kamil', 
             duration=3.5)
song_list.add(song2)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After addition of 2nd song')
print(vars(song_list))
print(vars(song1))
print(vars(song2))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')

song3 = Song(title='3. Boom Shaka', 
             artist='KR$NA, Dhanda Nyoliwala', 
             duration=4.0)
song_list.add(song3)

print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('After addition of 3rd song')
print(vars(song_list))
print(vars(song1))
print(vars(song2))
print(vars(song3))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')