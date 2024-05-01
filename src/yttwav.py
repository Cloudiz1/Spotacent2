import pytube
import subprocess
import os

def convert_to_wav(link):
    try:
        yt = pytube.YouTube(link)
    except:
        print("Link does not exist.")
        return None
    
    print(yt.title)
    
    file_name = yt.title + " by " + yt.author
    file_name = file_name.replace(" ", "_")
    
    try:
        video = yt.streams.filter(only_audio=True).first()
        video.download(output_path="./songs", filename=file_name + ".mp4") # downloads yt video
        
        subprocess.call(f"ffmpeg -i ./songs/{file_name}.mp4 -ab 160k -ac 2 -ar 44100 -vn songs/{file_name}.wav") # copies and converts to wav
        
        os.remove(f"./songs/{file_name}.mp4")
        
        return file_name
        
    except:
        print("Error converting to wav")
        return None
    
# convert_to_wav(input("link:"))