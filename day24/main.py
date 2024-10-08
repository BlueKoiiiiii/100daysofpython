#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt") as names:
    name = names.readlines()
    for i in name:
        person = i.strip()
        with open("Input/Letters/starting_letter.txt") as file:
            lines = file.readlines()
            txt = lines[0]
            lines[0] = txt.replace("[name]", i)
            with open(f"./Output/ReadyToSend/letter_for_{person}", mode="w") as letter:
                for i in lines:
                    letter.write(i)