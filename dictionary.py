import json
from difflib import get_close_matches

# Importing the Dictionary file containing all words with their meaning
data =json.load(open("data.json"))

def translate(meaning):
    # To make it non case-sensitive
    meaning=meaning.lower()

    # Find whether the word exist or not
    if meaning in data:
        return data[meaning]

    # Checks if missspell by user and ask, is that the word you seacrh for?
    elif len(get_close_matches(meaning, data.keys()))>0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(meaning, data.keys())[0])
        if yn =="Y":
            return data[get_close_matches(meaning, data.keys())[0]]
        elif yn == "N":
            return "The word does'nt exist. Please double check it."
        else:
            return "You may have enter a wrong input, Try again!!"
    #If no search word is found in dictionary
    else:
        return "The word does'nt exist. Please double check it."

word =input("Enter Word: ")

output = translate(word)

# If the word has two or more meanings and you want it in separate lines.
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
