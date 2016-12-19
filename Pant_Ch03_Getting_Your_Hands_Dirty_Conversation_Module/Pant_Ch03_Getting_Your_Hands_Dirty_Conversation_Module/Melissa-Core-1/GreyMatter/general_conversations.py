from SenseCells.tts import tts

def who_are_you():
    message = 'I am Melissa, your lovely personal assistant.'
    tts(message)

def undefined():
    tts('I dont know what that means!')
