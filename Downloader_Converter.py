from pytube import YouTube  
import os
import subprocess
from sys import exit

def start ():
	print("insert the video link")
	link=input()
	video = YouTube(link)
	print(video.title)

	
	#insert where to download the videos
	parent_dir=  ("C:\\Users\\simon\\Desktop\\downloader")

	
	#you can choose the quality of the video
	stream = video.streams.all()
	for i in range(len(stream)):
		print(i,'.',stream[i])
	vnum = int(input("enter the number:  "))

	stream[vnum].download(parent_dir)
	print('the video has been downloaded !! \nwould you want to convert the video to mp3? \n ')
	sce =  input()
	if sce == 'yes' :
	
		new_filename = video.title + '.mp3'
		default_filename = stream[vnum].default_filename

		subprocess.call(['ffmpeg', '-i',
				os.path.join(parent_dir,default_filename),
				os.path.join(parent_dir,new_filename)
		])
		print('Converted !! \n Do you want to delete the mp4 format?')
		sce1 = input()
		if sce1 == 'yes':
			os.remove(default_filename)
		
		
	
	print('download another file?')
	scelta = input()
	if scelta == "yes" :
		again = start()
	else :
		exit("bye-bye")

		
			
begin = start()
