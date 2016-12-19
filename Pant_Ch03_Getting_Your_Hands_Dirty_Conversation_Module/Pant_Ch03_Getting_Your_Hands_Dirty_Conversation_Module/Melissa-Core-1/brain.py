from GreyMatter import general_conversations 

def brain(name, speech_text):
    def check_message(check): 

        if speech_text ==  check:
            return True
        else:
            return False

    if check_message('who are you'):
        general_conversations.who_are_you()
    else:
        general_conversations.undefined()
