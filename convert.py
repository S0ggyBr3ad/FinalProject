from pydub import AudioSegment

# Converts mp3 to wav
def mp3towav(filename):
    # convert mp3 to wav
    sound = AudioSegment.from_mp3(filename)
    sound.export("pt_mono.wav", format="wav")

# Converts multichannel to mono, also has the side effect of cleaning metadata
def toMono(filename):
    raw_audio = AudioSegment.from_file(filename, format="wav")
    mono_wav = raw_audio.set_channels(1)
    mono_wav.export("pt_mono.wav", format="wav")
