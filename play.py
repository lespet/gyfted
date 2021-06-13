# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 15:09:08 2021

@author: user
"""
import random


with open('c:/gyft1/dataset/yes_small/tags.txt') as f:
      content = f.readlines()
# you may also want to remove whitespace characters 
content = [x.strip() for x in content] 
    
contenstn=[]

for line in content:
    if line=='#':
        contenstn.append(0) 
    else:
        s=[int(val) for val in line.split()]
        contenstn.append(s)



with open('c:/gyft1/dataset/yes_small/song_hash.txt') as f:
      song = f.readlines()
# you may also want to remove whitespace characters 
songs = [x.strip() for x in song] 

songl=[]

for line in songs:
      s=[val for val in line.split("\t")]
      songl.append(s)
    
####tasks
with open('c:/gyft1/dataset/yes_small/tag_hash.txt') as f:
      tag = f.readlines()
# you may also want to remove whitespace characters 
tags = [x.strip() for x in tag] 

tagl=[]

for line in tags:
      s=[val for val in line.split(",")]
      tagl.append(s) 
    
    
   
#the songs data such that it’s easier to read at once: (song_id, title, artist, all the tags associated with the song)
str1=''

for i in range(len(songs)):
    str1=str1+songl[i][0]+','+songl[i][1]+','+songl[i][2]+','
    if contenstn[i]!=0 :
        for k in contenstn[i]:
            str1=str1+str(tagl[k][1])+';'
    str1=str1+"\n"

songs_data=str1

#the playlist data (a list of song names for each playlist)

with open('c:/gyft1/dataset/yes_small/train.txt') as f:
    f.readline()
    f.readline()
    play = f.readlines()
# you may also want to remove whitespace characters 

playl = [x.strip() for x in play] 
plays=[]    

for line in playl:
        s=[int(val) for val in line.split()]
        plays.append(s)

str2=''

for i in range(len(plays)):
    for k in plays[i]:
        str2=str2+str(songl[k][1])+';'
    str2=str2+"\n"


text_file = open("songs_data.txt", "w")
n1 = text_file.write(songs_data)
text_file.close()

text_file = open("playlist_data.txt", "w")
n2 = text_file.write(str2)
text_file.close()

## Implement a function that given a playlist recommends a random song. 

value = input("Please enter an integer, representing playlist, from - from 0 to 41479 :\n")
 
value = int(value)
song_list=plays[value]
print(random.choice(song_list))
s1=random.choice(song_list)
random_song= songs[s1]



##mini song recommender 


print(f'You entered {value} and its random song is  {random_song}')

# taking multiple lists at a time

x = [int(x) for x in input("Enter multiple value representing lists: ").split()]

song_list=plays[value]
print(" lists are: ", x)

total=[]
for i in range(len(x)):
    total.append(plays[i])

total1 = [item for sublist in total for item in sublist]
#print(random.choice(total1))
s1=random.choice(total1)
random_song= songs[s1]



print(f'based on selecte playlists random song is  {random_song}')

