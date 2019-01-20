'''
Python Homework Assignment #1
Here is my favorite song
By: Hieu Nguyen

'''

# This is all the information about my song

# Name of the Music Artist
Music_Artist = "Linkin Park"

# Name of the Music Album List
Music_Album = "Transformers: Revenge of the Fallen - The Music_Album"

# Here is when the song was released
Song_Released = 2009

# Here is when the song was recorded
Song_Recorded = 2008

# Type of music genre
Music_Genre = "Rock/Hard Rock"

# Lyric Word Count
Word_Count = 248 

# Lyric Character Count
Character_Count = 1252

# Time in minutes and seconds EXACTLY minutes:seconds ex. 1:22 means one minute and twenty-two seconds
# This integer CANNOT be a number or float only string because it is the EXACTLY time finialized.
Time_Duration_Exactly = "4:28" 

# Total Number of Seconds ONLY
Time_Duration_Seconds = 268

# Using the print() to display my results for each of the Variables from above.

# Printing out the results on each variables 
# Printing out to the string for Music Artist, Music Album and Music_Genre
print('Favorite Music Artist/Band: ' + Music_Artist)
print('This song came out in the ' + Music_Album)
# Using str() means a string and I was using it to convert the integer numbers I have defined and put them into strings because to print out the results.
print('The song was released in the year ' + str(Song_Released))
print('Otherwise the song was recorded in the year ' + str(Song_Recorded))
print('The type of music genre is ' + Music_Genre)
print('From counting and listening to the lyrics to all the words counted to ' + str(Word_Count))
print('Also all the characters from the lyrics counted to ' + str(Character_Count))
print('Time Length for my favorite song is ' + str(Time_Duration_Exactly))
print('Lastly the song is about ' + str(Time_Duration_Seconds) + ' seconds')




