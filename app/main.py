# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# The text that we want to convert in audio
text = 'Welcome guys!'

# Language in which we want to convert
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
audio = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome 
audio.save("app/welcome.mp3")
