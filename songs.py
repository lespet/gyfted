# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 11:46:31 2021

"""



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
# you may also want to remove whitespace characters like `\n` at the end of each line
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
