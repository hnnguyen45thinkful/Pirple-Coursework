
'''
Python Homework Assignment #7
Dictionaries and Sets
By: Hieu Nguyen

'''

# Details:
 
# Return to your first homework assignments, when you described your favorite song. Refactor that code so all the variables are held as dictionary keys and value. Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.


# Extra Credit:

# Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. This function should accept two parameters: Key and Value. If the key exists in the dictionary and that value is the correct value, then the function should return true. In all other cases, it should return false.

# create an empty dictionary with soon to have a collection below with curly brackets and each below has keys and key values.
favorite_song = {}
#Refactor all variables into all keys and values in a dictionary and sets
favorite_song['Music_Artist'] = "Linkin Park" 
favorite_song['Music_Album'] = "Transformers: Revenge of the Fallen - The Music_Album"  
favorite_song['Song_Released'] =  2009  
favorite_song['Song_Recorded'] = 2008  
favorite_song['Music_Genre'] = "Rock/Hard Rock" 
favorite_song['Word_Count'] = 248  
favorite_song['Character_Count'] = 1252  
favorite_song['Time_Duration_Exactly'] = "4:28"  
favorite_song['Time_Duration_Seconds'] = 268  

for key in favorite_song:
	print(key, ':', favorite_song[key])

def GuessMusicInfo(key, value):
	if key in favorite_song and favorite_song[key] == value:
		return True
	else:
		return False

print(GuessMusicInfo('Music_Artist', 'Linkin Park')) #True
print(GuessMusicInfo('Music_Artist', 'The Vines')) #False
print(GuessMusicInfo('Music_Album', 'Transformers: Revenge of the Fallen - The Music_Album')) #True
print(GuessMusicInfo('Music_Album', 'Bumblebee - The Music_Album'))#False
print(GuessMusicInfo('Song_Released', 2009)) #True
print(GuessMusicInfo('Song_Released', 2010)) #False
print(GuessMusicInfo('Song_Recorded', 2008)) #True
print(GuessMusicInfo('Song_Recorded', 2007)) #False
print(GuessMusicInfo('Music_Genre', "Rock/Hard Rock")) #True
print(GuessMusicInfo('Music_Genre', "Punk Rock")) #False
print(GuessMusicInfo('Word_Count', 248)) #True
print(GuessMusicInfo('Word_Count', 250)) #False
print(GuessMusicInfo('Character_Count', 1252))#True
print(GuessMusicInfo('Character_Count', 1200)) #False
print(GuessMusicInfo('Time_Duration_Exactly', "4:28"))#True
print(GuessMusicInfo('Time_Duration_Exactly', "5:00")) #False
print(GuessMusicInfo('Time_Duration_Seconds', 268))#True
print(GuessMusicInfo('Time_Duration_Seconds', 260))#False
