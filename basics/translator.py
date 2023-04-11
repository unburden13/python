# Vowels to letter "f"

def translate(phrase):
    """
    what the function does
    how to get this text: print(translate.__doc__) or help(translate)
    """
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "f"
        else:
            translation = translation + letter

    return translation


print(translate(input("Enter a phrase: ")))
