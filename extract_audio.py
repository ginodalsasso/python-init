import moviepy.editor as mp
import os

path = input("Enter the path of the video file: \n")
video = mp.VideoFileClip(path) 
audio = video.audio # Extrait l'audio de la vidéo
audio.write_audiofile("audio.mp3") # Nom du fichier audio extrait