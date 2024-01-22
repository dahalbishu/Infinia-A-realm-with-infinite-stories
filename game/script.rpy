


######## TASKS REMAINING  #########


## Character name and content extraction in end prompt ## 

## MUSIC AND PHOTO INCLUSION ### ----- Done

## CHARACTER should change on the basis of name from the response of the API #### ---- Done



## Character images inclusion #### ---- Done

### Enhancement of the GUI ####

define h = Character("Haldy")
define m = Character("Mona")
define a = Character("Alison")
define e = Character("Ovam")
define g = Character("Infinia")

image example = Movie(play="images/startvid.webm", loop=True, channel = "m")
image end = Movie(play="images/endvid.webm", loop=False, channel = "m")


# The game starts here.

label start:
    
    
    
    
    
    python:       
        import google.generativeai as genai
        genai.configure(api_key="AIzaSyCPd0_bydYrGHMDPH3J7BXVEG04ObSaaWA")
        safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        ]

        model = genai.GenerativeModel(model_name='gemini-pro', safety_settings=safety_settings)
        gemini_chat = model.start_chat()
        
        while True:
            try:            
                resp1 = gemini_chat.send_message("You'll be the naratter of a short story for a game. You'll narrate the prologue, give me options every third turn. And also give the dialogue of the characters. The characters are Haldy the wizard, Mona the townsgirl, Alison the player and Ovam the villain. Everytime a character is to speak, tell me the name first. Are you ready?  ")
                break

            except:
                pass


        while True:
            try:            
                resp2 = gemini_chat.send_message("Can you describe the location the story is currrently at? 1 line only. 1 line. 1 line")
                break
            except:
                pass


        while True:
            try:            
                resp22 = gemini_chat.send_message("What is mood curently? 1 line only. 1 line. 1 line. very short")
                break
            except:
                pass

        from video_gen import rajat
        from music_gen import music
        music(resp22)
        

        bb = rajat(resp2.text,1)    
    
    play sound "startmusic.mp3"
    scene example 
    show gamedev:
        pos(150,300)
    
    g "WELCOME TO INFINIA: A REALM WITH INFINITE STORIES."

    menu:
        g "If you like the game, consider purchasing the subscription please."
        
        "Buy the subscription now":
            python:
                import webbrowser
                webbrowser.open('https://www.connectips.com/')
            pass
        "Continue for now":
            pass
    
    g "Now lets start the story. The characters in our story are:-"
    
    hide gamedev

    show boy:
        pos(-100,200)

    show witch:
        pos(650,-150)
    show girl:
        pos(250,200)
    show villian:
        pos(1050,200)

    g "Alison, Mona, Haldy and Ovam. Lets start the story now!"
    stop sound
    



    play music "audio.wav"
    
    scene image("bishe[bb].png")

    

    python:
        import re

        def split_paragraph_max_word_count(paragraph):
    
            sentences = paragraph.split('. ')
            max_word_count = 47
            current_word_count = 0
            current_sentence = ""
            remaining_paragraph = ""

            for sentence in sentences:
                sentence_word_count = len(sentence.split())

                if current_word_count + sentence_word_count <= max_word_count:
                    current_sentence += sentence + '. '
                    current_word_count += sentence_word_count
                else:
                    remaining_paragraph = '. '.join(sentences[sentences.index(sentence):]).strip()
                    break

            result = current_sentence.strip()
            return result, remaining_paragraph

        def remove_chars(input_string):
            chars_to_remove = ['Option', '1', ':', '*', '2', '3']

            for char in chars_to_remove:
                input_string = input_string.replace(char, '')

            # Remove any remaining white spaces
            input_string = ' '.join(input_string.split())

            return input_string
    
        def keep_first_paragraph(input_string):
            paragraphs = input_string.split('\n\n', 1)

            if paragraphs:
                # Keep only the first paragraph
                input_string = paragraphs[0]

            return input_string
        
        def remove_content_in_parentheses(input_string):
            # Use a regular expression to remove content within parentheses
            result_string = re.sub(r'\([^)]*\)', '', input_string)

            return result_string
        
        resp3 = gemini_chat.send_message("Write the prologue now. 2 sentences only. 40 words total maximum. Nothing more  ")
        # text1 = resp3.text
        # textwa1 = text1.replace('*', '')
        # resp3op = ' '.join(textwa1.split())


        resp4 = gemini_chat.send_message("Now give me character's dialogue to move the story forward. generate only dialogue. It should be in the format - Charactername: Dialogue. No markdown")
        # text2 = resp3.text
        # textwa2 = text1.replace('*', '')
        # resp4op = ' '.join(textwa2.split())

        resp5 = gemini_chat.send_message(" Now give me three options to choose from. Only the options, nothing more. Only the op-tions. ")
    
    
        while True:
            try:
                resp6 = gemini_chat.send_message("Now mention the first option only. No markdown. Only the first option. Only write the first option. Fomat should be- 1. Option ")
                break
            except:
                pass
        while True:
            try:           
                resp7 = gemini_chat.send_message("Now mention the second option only. No markdown. Only the second option. Only write the second option. Fomat should be- 2. Option ")
                break
            except:
                pass
        while True:
            try:
                resp8 = gemini_chat.send_message(" Now mention the third option only. No markdown. Only the third option. Only write the third option.  Fomat should be- 3. Option ")
                break
            except:
                pass 

        resp6op1 = remove_chars(resp6.text)

       
        resp7op2 = remove_chars(resp7.text)

        
        resp8op3 = remove_chars(resp8.text)
    
    python: 
        # Remove all asterisks from the dialogue
        
        dialogue = resp3.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)
    $ cot = lengthdig
    if cot == 0:
        "[dialogue]" #Prologue
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
          
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile




        $ iii = iii +1
        $ cot = cot-1



    python: 
        # Remove all asterisks from the dialogue
        dialogue = resp4.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)
    $ cot = lengthdig
    if cot == 0:
        "[dialogue]" 
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
          
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile


        $ iii = iii +1
        $ cot = cot-1


    # for all dialouge ------------- ------------
    python: 
        # Remove all asterisks from the dialogue
        dialogue = resp4.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
    #     characters_list = []
    #     dialogues_list = []

    #     for line in lines:
    #         line = line.strip()
    #         if line:
    #             parts = line.split(':')
    #             if len(parts) == 2:
    #                 character = parts[0].strip()
    #                 dialog = parts[1].strip()
    #                 characters_list.append(character)
    #                 dialogues_list.append(dialog)
        
    #     lengthdig = len(characters_list)
    # $ cot = lengthdig
    # $ iii = 0
    # while cot > 0:
    #     python:
    #         cha = characters_list[iii]
    #         dig = dialogues_list[iii]
    #     if cha == 'Haldy':
    #         show witch at left
    #         h "[dig]"

    #     elif cha == 'Ovam':

    #         show villan at left
          
    #         e "[dig]"
    #     elif cha =="Alison":
    #         show boy smile at left

    #         a "[dig]"
    #     else: 
    #         show girl smile at left

    #         m "[dig]"

    #     $ iii = iii +1
    #     $ cot = cot-1
            
    
    menu: #options
        
        "What will you do?"
        "[resp6op1]":
            jump opt1

        "[resp7op2]":
            jump opt2

        "[resp8op3]":
            jump opt3

    

label opt1:
    python:
        while True:
            try:
                resp9 = gemini_chat.send_message("Go with first option. Continue the story. 2 sentences only. 40 words maximum.")
                break
            except:
                pass


        while True:
            try:            
                resp22 = gemini_chat.send_message("What is mood curently? 1 line only. 1 line. 1 line. very short")
                break
            except:
                pass
        
        music(resp22)
        
        response11 = gemini_chat.send_message("Can you describe the location the story is currrently at? 1 line only. 1 line. 1 line")
        bb = rajat(response11.text,bb)
    play music "audio.wav"
                    
    scene image("bishe[bb].png")

    #"music: [resp22.text]"
    "Location: [response11.text]"


    "[resp9.text]"
    jump next

label opt2:
    python:
        while True:
            try:
                resp10 = gemini_chat.send_message("Go with second option. Continue the story. 2 sentences only. 40 words maximum.")
                break
            except:
                pass
                


        while True:
            try:            
                resp22 = gemini_chat.send_message("What is mood curently? 1 line only. 1 line. 1 line. very short")
                break
            except:
                pass
        
        music(resp22) 
        
        response11 = gemini_chat.send_message("Can you describe the location the story is currrently at? 1 line only. 1 line. 1 line")
        bb = rajat(response11.text,bb)
                    
    play music "audio.wav"
                    
    scene image("bishe[bb].png")

    #"music: [resp22.text]"
 
    "Location: [response11.text]"

    python: 
        # Remove all asterisks from the dialogue
        dialogue = resp10.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)
    $ cot = lengthdig
    if cot == 0:
        "[dialogue]" #Prologue
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
          
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile



        $ iii = iii +1
        $ cot = cot-1
    jump next

label opt3:
    python:
        while True:
            try:
                resp11 = gemini_chat.send_message("Go with third option. Continue the story. 2 sentences only. 40 words maximum.")
                break
            except:
                pass


        while True:
            try:            
                resp22 = gemini_chat.send_message("What is mood curently? 1 line only. 1 line. 1 line. very short")
                break
            except:
                pass
        
        music(resp22)

        response11 = gemini_chat.send_message("Can you describe the location the story is currrently at? 1 line only. 1 line. 1 line")
        bb = rajat(response11.text,bb)
                    
    play music "audio.wav"
                    
    scene image("bishe[bb].png")

    #"music: [resp22.text]"
 
    "Location: [response11.text]"


    "[resp11.text]"
    python: 
        # Remove all asterisks from the dialogue
        dialogue = resp11.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)
    $ cot = lengthdig
    if cot == 0:
        "[dialogue]" #Prologue
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
          
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile



        $ iii = iii +1
        $ cot = cot-1
    jump next

label next:

    $ count = 3

    while count > 0:

        python:
            while True:
                try:
                    resp12 = gemini_chat.send_message("continue the story in just 2 sentences. 40 words maximum.")
                    break
                except:
                    pass
            
            while True:
                try:
                    resp13 = gemini_chat.send_message("continue the story further in just 2 sentences. 1 paragraph. 40 words maximum.")
                    break
                except:
                    pass
            
            while True:
                try:
                    resp131 = gemini_chat.send_message("Dialogue of one character to move the story forward. generate only dialogue. It should be in the format - Charactername: Dialogue")
                    break
                except:
                    pass
            
            while True:
                try:
                    resp141 = gemini_chat.send_message("Dialogue of another one character to move the story forward. generate only dialogue. It should be in the format - Charactername: Dialogue")
                    break
                except:
                    pass


            while True:
                try:
                    resp14 = gemini_chat.send_message("continue the story further in just 2 sentences.1 paragraph. 40 words maximum.")
                    break
                except:
                    pass
            
            ## Sentence extraction code

            paragraph = resp14.text
            temp_arr = []

            while paragraph:
                result, paragraph = split_paragraph_max_word_count(paragraph)
                if result.strip():
                    temp_arr.append(result)

            while True:
                try:
                    resp15 = gemini_chat.send_message(" Now give me three options.Nothing more explanation nonsense.")
                    break
                except:
                    pass

            while True:
                try:
                    resp16 = gemini_chat.send_message("among given three options give me one option at a time. Nothing more explanation nonsense. Just the option. Nothing more")
                    break
                except:
                    pass
            
            while True:
                try:
                    resp17 = gemini_chat.send_message("give me next option. Nothing more explanation nonsense.")
                    break
                except:
                    pass
            
            while True:
                try:
                    resp18 = gemini_chat.send_message("give me next option. Nothing more explanation nonsense.")
                    break
                except:
                    pass

            resp16op1 = remove_chars(resp16.text)


            resp17op2 = remove_chars(resp17.text)


            resp18op3 = remove_chars(resp18.text)


        python: 
            # Remove all asterisks from the dialogue
            dialogue = resp12.text
            dialogue = dialogue.replace('*', '')

            # Split the dialogue into lines
            lines = dialogue.split('\n')

            # Create two lists: one for characters and one for dialogues
            characters_list = []
            dialogues_list = []

            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 2:
                        character = parts[0].strip()
                        dialog = parts[1].strip()
                        characters_list.append(character)
                        dialogues_list.append(dialog)
        
            lengthdig = len(characters_list)
        $ cot = lengthdig
        if cot == 0:
            "[dialogue]" 
        $ iii = 0
        while cot > 0:
            python:
                cha = characters_list[iii]
                dig = dialogues_list[iii]
            if cha == 'Haldy':
                show witch at left
                h "[dig]"
                hide witch
            elif cha == 'Ovam':

                show villan at left
            
                e "[dig]"
                hide villan
            elif cha =="Alison":
                show boy smile at left

                a "[dig]"
                hide boy smile
            else: 
                show girl smile at left

                m "[dig]"
                hide girl smile



            $ iii = iii +1
            $ cot = cot-1
            
        python: 
            # Remove all asterisks from the dialogue
            dialogue = resp13.text
            dialogue = dialogue.replace('*', '')

            # Split the dialogue into lines
            lines = dialogue.split('\n')

            # Create two lists: one for characters and one for dialogues
            characters_list = []
            dialogues_list = []

            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 2:
                        character = parts[0].strip()
                        dialog = parts[1].strip()
                        characters_list.append(character)
                        dialogues_list.append(dialog)
        
            lengthdig = len(characters_list)
        $ cot = lengthdig
        if cot == 0:
            "[dialogue]" 
        $ iii = 0
        while cot > 0:
            python:
                cha = characters_list[iii]
                dig = dialogues_list[iii]
            if cha == 'Haldy':
                show witch at left
                h "[dig]"
                hide witch
            elif cha == 'Ovam':

                show villan at left
            
                e "[dig]"
                hide villan
            elif cha =="Alison":
                show boy smile at left

                a "[dig]"
                hide boy smile
            else: 
                show girl smile at left

                m "[dig]"
                hide girl smile



            $ iii = iii +1
            $ cot = cot-1
            
            "[resp13.text]"
            "[resp14.text]"
        
        python: 
            # Remove all asterisks from the dialogue
            dialogue = resp131.text
            dialogue = dialogue.replace('*', '')

            # Split the dialogue into lines
            lines = dialogue.split('\n')

            # Create two lists: one for characters and one for dialogues
            characters_list = []
            dialogues_list = []

            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 2:
                        character = parts[0].strip()
                        dialog = parts[1].strip()
                        characters_list.append(character)
                        dialogues_list.append(dialog)
        
            lengthdig = len(characters_list)
        $ cot = lengthdig
        if cot == 0:
            "[dialogue]" 
        $ iii = 0
        while cot > 0:
            python:
                cha = characters_list[iii]
                dig = dialogues_list[iii]
            if cha == 'Haldy':
                show witch at left
                h "[dig]"
                hide witch
            elif cha == 'Ovam':

                show villan at left
            
                e "[dig]"
                hide villan
            elif cha =="Alison":
                show boy smile at left

                a "[dig]"
                hide boy smile
            else: 
                show girl smile at left

                m "[dig]"
                hide girl smile



            $ iii = iii +1
            $ cot = cot-1
        
        python: 
            # Remove all asterisks from the dialogue
            dialogue = resp141.text
            dialogue = dialogue.replace('*', '')

            # Split the dialogue into lines
            lines = dialogue.split('\n')

            # Create two lists: one for characters and one for dialogues
            characters_list = []
            dialogues_list = []

            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 2:
                        character = parts[0].strip()
                        dialog = parts[1].strip()
                        characters_list.append(character)
                        dialogues_list.append(dialog)
        
            lengthdig = len(characters_list)
        $ cot = lengthdig
        if cot == 0:
            "[dialogue]" 
        $ iii = 0
        while cot > 0:
            python:
                cha = characters_list[iii]
                dig = dialogues_list[iii]
            if cha == 'Haldy':
                show witch at left
                h "[dig]"
                hide witch
            elif cha == 'Ovam':

                show villan at left
            
                e "[dig]"
                hide villan
            elif cha =="Alison":
                show boy smile at left

                a "[dig]"
                hide boy smile
            else: 
                show girl smile at left

                m "[dig]"
                hide girl smile



            $ iii = iii +1
            $ cot = cot-1


        python: 
            # Remove all asterisks from the dialogue
            dialogue = resp14.text
            dialogue = dialogue.replace('*', '')

            # Split the dialogue into lines
            lines = dialogue.split('\n')

            # Create two lists: one for characters and one for dialogues
            characters_list = []
            dialogues_list = []

            for line in lines:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) == 2:
                        character = parts[0].strip()
                        dialog = parts[1].strip()
                        characters_list.append(character)
                        dialogues_list.append(dialog)
        
            lengthdig = len(characters_list)

        $ cot = lengthdig
        if cot == 0:
            "[dialogue]"
        $ iii = 0
        while cot > 0:
            python:
                cha = characters_list[iii]
                dig = dialogues_list[iii]
            if cha == 'Haldy':
                show witch at left
                h "[dig]"
                hide witch
            elif cha == 'Ovam':

                show villan at left
            
                e "[dig]"
                hide villan
            elif cha =="Alison":
                show boy smile at left

                a "[dig]"
                hide boy smile
            else: 
                show girl smile at left

                m "[dig]"
                hide girl smile



            $ iii = iii +1
            $ cot = cot-1
            
            "[resp13.text]"
            "[resp14.text]"

        menu:
        
            "What will you do?"
            "[resp16op1]":
                jump opto1

            "[resp17op2]":
                jump opto2

            "[resp18op3]":
                jump opto3
    
label opto1:
    python:
        while True:
            try:
                resp19 = gemini_chat.send_message("Go with first option. Continue the story. You will have to end the story soon. 2 sentences only. 1 paragraph.")
                break
            except:
                pass


        while True:
            try:            
                resp22 = gemini_chat.send_message("What is mood curently? 1 line only. 1 line. 1 line. very short")
                break
            except:
                pass
        
        music(resp22)


        
        response11 = gemini_chat.send_message("Can you describe the location the story is currrently at? 1 line only. 1 line. 1 line")
        bb = rajat(response11.text,bb)
                    
    play music "audio.wav"
                    
    scene image("bishe[bb].png")

    #"Music: [resp22.text]"
 
    "Location: [response11.text]"

    python: 
        # Remove all asterisks from the dialogue
        dialogue = resp19.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)

    $ cot = lengthdig
    if cot == 0:
        "[dialogue]"
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
        
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile



        $ iii = iii +1
        $ cot = cot-1
    
    jump end

label opto2:
    python:
        while True:
            try:
                resp20 = gemini_chat.send_message("Go with second option. Continue the story. You will have to end the story soon. 2 sentences only. 1 paragraph.")
                break
            except:
                pass


        while True:
            try:            
                resp22 = gemini_chat.send_message("What is mood curently? 1 line only. 1 line. 1 line. very short")
                break
            except:
                pass
        
        music(resp22)

        
        response11 = gemini_chat.send_message("Can you describe the location the story is currrently at? 1 line only. 1 line. 1 line")
        bb = rajat(response11.text,bb)
                    
    play music "audio.wav"
                    
    scene image("bishe[bb].png")

    #"music: [resp22.text]"
 
    "Location: [response11.text]"


    python: 
        # Remove all asterisks from the dialogue
        dialogue = resp20.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)
    $ cot = lengthdig
    if cot == 0:
        "[dialogue]"
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
          
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile



        $ iii = iii +1
        $ cot = cot-1
    jump end

label opto3:
    python:
        while True:
            try:
                resp21 = gemini_chat.send_message("Go with third option. Continue the story. You will have to end the story soon. 2 sentences only. 1 paragraph.")
                break
            except:
                pass


        while True:
            try:            
                resp22 = gemini_chat.send_message("What is mood curently? 1 line only. 1 line. 1 line. very short")
                break
            except:
                pass
        
        music(resp22)

        
        response11 = gemini_chat.send_message("Can you describe the location the story is currrently at? 1 line only. 1 line. 1 line")
        bb = rajat(response11.text,bb)
                    
    play music "audio.wav"
                    
    scene image("bishe[bb].png")

    #"music: [resp22.text]"
 
    "Location: [response11.text]"


    python: 
        # Remove all asterisks from the dialogue
        dialogue = resp21.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)
    $ cot = lengthdig
    if cot == 0:
        "[dialogue]"
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
          
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile



        $ iii = iii +1
        $ cot = cot-1
    jump end

label end:
    #"in end"
    python:
        #import re

        while True:
            try:
                resp22 = gemini_chat.send_message("Give me an ending story dialogue. generate only dialogue. It should be in the format - Charactername: Dialogue. No markdown")

                break
            except:
                pass
   
    python:
        # Remove all asterisks from the dialogue
        dialogue = resp22.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)
    $ cot = lengthdig
    if cot == 0:
        "[resp22.text]" #Prologue
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
          
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile


        $ iii = iii + 1
        $ cot = cot - 1
    
 
    python:
        #import re

        while True:
            try:
                resp23 = gemini_chat.send_message("Give me an ending story. Final 4 sentances. maximum 4 sentences.1 paragraph. Maximum words of 40 in total .And it should end story perfectly")

                break
            except:
                pass
   
    python:
        # Remove all asterisks from the dialogue
        dialogue = resp23.text
        dialogue = dialogue.replace('*', '')

        # Split the dialogue into lines
        lines = dialogue.split('\n')

        # Create two lists: one for characters and one for dialogues
        characters_list = []
        dialogues_list = []

        for line in lines:
            line = line.strip()
            if line:
                parts = line.split(':')
                if len(parts) == 2:
                    character = parts[0].strip()
                    dialog = parts[1].strip()
                    characters_list.append(character)
                    dialogues_list.append(dialog)
        
        lengthdig = len(characters_list)
    $ cot = lengthdig
    if cot == 0:
        "[resp23.text]" #Prologue
    $ iii = 0
    while cot > 0:
        python:
            cha = characters_list[iii]
            dig = dialogues_list[iii]
        if cha == 'Haldy':
            show witch at left
            h "[dig]"
            hide witch
        elif cha == 'Ovam':

            show villan at left
          
            e "[dig]"
            hide villan
        elif cha =="Alison":
            show boy smile at left

            a "[dig]"
            hide boy smile
        else: 
            show girl smile at left

            m "[dig]"
            hide girl smile


        $ iii = iii + 1
        $ cot = cot - 1

    
    scene end
    "{b}THE END!{/b}"
    
    
    

    return
