from gtts import gTTS 
import androidhelper 

droid = androidhelper.Android()

droid.ttsSpeak('please enter your lyrics ')
lyrics = input(' please enter lyrics ')

droid.ttsSpeak('save as') 
file = input(' Format type = .mp3 \n SAVE AS:  ')
TYPE = (file + '.' + '{}'.format('mp3'))

tts = gTTS(lyrics, 'en')
tts.save(TYPE)