from os import path
from pydub import AudioSegment
from pydub.playback import play
#files
src = "pt.mp3"
dst = "pt.wav"

#convert mp3 to wav
def convert(filename):
    sound = AudioSegment.from_mp3(filename)
    sound.export(filename, format="wav")

    raw_audio = AudioSegment.from_file(filename, format="wav")
    channel_count = raw_audio.channels
    print(channel_count)
    mono_wav = raw_audio.set_channels(1)
    mono_wav.export("pt_mono.wav", format="wav")
    mono_wav_audio = AudioSegment.from_file("pt_mono.wav", format="wav")
    channel_count = mono_wav_audio.channels
    print(channel_count)
