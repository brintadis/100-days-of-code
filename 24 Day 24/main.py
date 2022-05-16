#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    with open("Input/Names/invited_names.txt", "r") as names:
        name_list = names.read().split()
    letter = starting_letter.read().split('\n')
    for name in name_list:
        letter[0] = f"Dear {name},"
        with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as new_letter:
            new_letter.write('\n'.join(letter))

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp