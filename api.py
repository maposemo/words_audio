from pydub import AudioSegment
from gtts import gTTS

import os

def makeAudio(path, source, langString):
    tts = gTTS(text=source, lang=langString)
    tts_audio = "./" + path + "_translation.mp3"
    tts.save(tts_audio)
    audio = AudioSegment.from_file(tts_audio)
    return audio

def combineAudio(translation, word, sentence): 
    return (translation + AudioSegment.silent(duration=2000) + 
                 word + AudioSegment.silent(duration=1500) + 
                 word + AudioSegment.silent(duration=1500) + 
                 word + AudioSegment.silent(duration=2000) + 
                 sentence + AudioSegment.silent(duration=1500) + 
                 sentence + AudioSegment.silent(duration=1500) + 
                 sentence + AudioSegment.silent(duration=3000))

# Generate and merge audio files
def makeAudioFile(name, words):
    # create temporarily directory
    os.makedirs(name, exist_ok=True)

    # Save the final combined file
    combinedAudio = AudioSegment.empty()
    for word, translation, sentence in words:
        print(word, translation, sentence)

        # make audio files
        word_audio = makeAudio(name, word, 'en')
        sentence_audio = makeAudio(name, sentence, 'en')
        translation_audio = makeAudio(name, translation, 'ko')

        combinedAudio += combineAudio(translation_audio, word_audio, sentence_audio)

    # Save the final combined file
    output_file = "./mp3/" + name + ".mp3"
    combinedAudio.export(output_file, format="mp3")
