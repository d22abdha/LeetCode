HowMany_Line_Sentences = int(input()) # How many sentences the user will input
alphabet = set('abcdefghijklmnopqrstuvwxyz') # Set of all 26 letters


for every_Line_Sentences in range(HowMany_Line_Sentences):
    line_Sentences = input().lower() # Read the sentence and convert to lowercase
    
    # Collect all alphabetic letters in the sentence
    letters_in_line_line_Sentences = set(char for char in line_Sentences if char.isalpha()) 

    # if there is a missing subtruct alphabetical letters in the set with written letters
    missing = sorted(alphabet - letters_in_line_line_Sentences)

    if not missing: # if the missing is empty print this
        print("pangram")
    else: # if the missing in not empty do this
        print("missing", ''.join(missing))
