from Session9B import Song
from Session9C import CircularDoublyLinkedList

song_list = CircularDoublyLinkedList()


song_list.add(element=Song(title='1. Jaan Se Guzarte Hain', 
             artist='Shashwat Sachdev, Khan Saab, Irshad Kamil', 
             duration=4.5))

song_list.add(element=Song(title='2. Deewaana Deewaana', 
             artist='A. R. Rahman, Irshad Kamil', 
             duration=3.5))

song_list.add(element=Song(title='3. Boom Shaka', 
             artist='KR$NA, Dhanda Nyoliwala', 
             duration=4.0))

song_list.add(element=Song(title='4. Gehra Hua', 
             artist='Shashwat Sachdev, Arijit Singh, Irshad Kamil', 
             duration=5.2))

song_list.add(element=Song(title='5. Sitaare', 
             artist='Arijit Singh, Amitabh Bhattacharya, Sachin-Jigar', 
             duration=4.3))

print(vars(song_list))

song_list.show(traverse=False)


# Implement the functions in CircularDoublyLinkedList 
# on some different Object (Flight, ChatMessage etc.. of your choice)