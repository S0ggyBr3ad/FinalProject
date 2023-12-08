from os import path
import pydub
from pydub import AudioSegment
from pydub.playback import play
#files
src = "16bit1chan.mp3"
dst = "clap.wav"

#convert mp3 to wav
def convertToWav(filename):
    pydub.AudioSegment.ffmpeg = filename
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

def convert1Chan(filename):
    raw_audio = AudioSegment.from_file(filename, format="wav")
    channel_count = raw_audio.channels
    print(channel_count)
    mono_wav = raw_audio.set_channels(1)
    mono_wav.export("pt_mono.wav", format="wav")
    mono_wav_audio = AudioSegment.from_file("pt_mono.wav", format="wav")
    channel_count = mono_wav_audio.channels
    print(channel_count)
