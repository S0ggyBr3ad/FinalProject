from os import path
from pydub import AudioSegment
from pydub.playback import play

def mp3towav(filename):
    # convert mp3 to wav
    sound = AudioSegment.from_mp3(filename)
    sound.export("temp.wav", format="wav")

def toMono(filename):
    raw_audio = AudioSegment.from_file(filename, format="wav")
    channel_count = raw_audio.channels
    mono_wav = raw_audio.set_channels(1)
    mono_wav.export("pt_mono.wav", format="wav")
    mono_wav_audio = AudioSegment.from_file("pt_mono.wav", format="wav")
    channel_count = mono_wav_audio.channels
    mono_wav_audio.export("temp.wav", format="wav")
