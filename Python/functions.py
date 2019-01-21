'''
Python Homework Assignment #2
Functions to declare
By: Hieu Nguyen

'''

# This is all the information about my song

# Name of the Music Artist using def function
def Music_Artist():
	return "Linkin Park" 

# Name of the Music Album List using def function
def Music_Album(): 
	return "Transformers: Revenge of the Fallen - The Music_Album"

# Here is when the song was released using def function
def Song_Released():
	return "2009"

# Here is when the song was recorded using def function
def Song_Recorded():
	return "2008"

# Type of music genre
def Music_Genre():
	return "Rock/Hard Rock"

# Lyric Word Count
Word_Count = 248 

# Lyric Character Count
Character_Count = 1252

# Time in minutes and seconds EXACTLY minutes:seconds ex. 1:22 means one minute and twenty-two seconds
# This integer CANNOT be a number or float only string because it is the EXACTLY time finialized.
def Time_Duration_Exactly():
	return "4:28" 

# Total Number of Seconds ONLY
def Time_Duration_Seconds():
	return "268"

def Download_Available():
	return True

# Using the print() to display my results for each of the Variables from above.

# Printing out the results on each variables along with functions using str and functionnames(). 
# Printing out to the string for Music Artist, Music Album and Music_Genre
print('Favorite Music Artist/Band: ' + Music_Artist())
print('This song came out in the ' + Music_Album())
# Using str() means a string and I was using it to convert the integer numbers I have defined and put them into strings because to print out the results.
print('The song was released in the year ' + Song_Released())
print('Otherwise the song was recorded in the year ' + Song_Recorded())
print('The type of music genre is ' + Music_Genre())
print('From counting and listening to the lyrics to all the words counted to ' + str(Word_Count))
print('Also all the characters from the lyrics counted to ' + str(Character_Count))
print('Time Length for my favorite song is ' + Time_Duration_Exactly())
print('Lastly the song is about ' + Time_Duration_Seconds() + ' seconds')
print('Available NOW to DOWNLOAD:', Download_Available())




