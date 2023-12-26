# Simple Text To Audio Program Written In Python.
# That Program Uses Multiprocessing!
# Created By; Luiz Gabriel Magalhães Trindade.
# Distributed Under The GPL3 License.
# GPL3 License: https://www.gnu.org/licenses/gpl-3.0.en.html#license-text

from multiprocessing import Process
from gtts import gTTS
from pydub import AudioSegment
from sys import argv
from time import time
from os import remove

parts = 4
language = "pt-br"
speed = 1.25

start = time()

def TextToSpeach(words, output):
    text = " ".join(words)
    tts = gTTS(text=text, lang=language)
    tts.save(output)

def JoinAudios():
    audio1 = AudioSegment.from_file("file1.mp3")
    audio2 = AudioSegment.from_file("file2.mp3")
    audio3 = AudioSegment.from_file("file3.mp3")
    audio4 = AudioSegment.from_file("file4.mp3")
    merged_audio = audio1 + audio2 + audio3 + audio4
    merged_audio_speedup = merged_audio.speedup(playback_speed=speed)
    merged_audio_speedup.export("FINAL_AUDIO.mp3", format="mp3")
    try:
        remove("file1.mp3")
        remove("file2.mp3")
        remove("file3.mp3")
        remove("file4.mp3")
    except: pass

text = ""
file_name = argv[1]
with open(file_name, "r") as file:
    content = file.read()
    for i in content:
        text += i  
              
text = text.split()
qntd = int(len(text)/parts)
print(f"Words: {len(text)}")
print(f"Quantity per part: {qntd}")

part1 = text[:qntd]
part2 = text[qntd:qntd*2]
part3 = text[qntd*2:qntd*3]
part4 = text[qntd*3:]

job1 = Process(target=TextToSpeach, args=(part1, "file1.mp3",))
job1.start()
job2 = Process(target=TextToSpeach, args=(part2, "file2.mp3",))
job2.start()
job3 = Process(target=TextToSpeach, args=(part3, "file3.mp3",))
job3.start()
job4 = Process(target=TextToSpeach, args=(part4, "file4.mp3",))
job4.start()

job1.join()
job2.join()
job3.join()
job4.join()

JoinAudios()
end = time()

total = float(end-start)
print(f"Total time: {total}")
