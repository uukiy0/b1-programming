#Start with an empty list called songs and an empty dictionary called genre_count.
songs= []
genre_count= {}

#Create loop, it runs 5 times will run the sequence 1 to 5 python will not run the last number.

for i in range(1,6):
    print(f"Enter song {i} ")

    song_name = input(" Song name:")
    genre = input(" Genre:")

#create a tuple to keep items together and cannot be changed later. songs.append to add the tuple to list called songs.
  
    song_tuple =(song_name, genre)
    songs.append(song_tuple)

#Count the amount of genres starting from 0 and adding one for each genre 

    genre_count[genre] = genre_count.get(genre, 0) + 1

print("MUSIC LIBRARY!!!!!!!!!!! YIPPIE!!!")

#Enumerate goes through each song in the list it gives a number aswell starting from 1

for index, (name, genre) in enumerate(songs, 1):
    print(f"{index}. {name} ({genre})")

print("Genre statistics")

for genre, count in genre_count.items():
    print(f"{genre}: {count} songs")    

popular_genre = max(genre_count, key=genre_count.get)

print(f"Most popular genre: {popular_genre}")


