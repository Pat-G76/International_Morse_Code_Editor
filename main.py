

"""
    _____________RULES____________
    The length of the dot is one
    The length of dash is 1 is one
    The length of the space between letters/characters of the same sentence is 1
    The length of the space between words is 7
    If a key character is not found we replace it with : #
"""

# characters in a normal sentence vs the code they represent them
translation = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..", "0": "-----", "1": ".----", "2": "..---",
    "3": "...--", "4": "....-", "5": ".....", "6": "-....",
    "7": "--...", "8": "---..", "9": "----.", "&": ".-...",
    "'": ".----.", "@": ".--.-.", ")": "-.--.-", "(": "-.--.",
    ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--",
    ".": ".-.-.-", "-": "-....-", "×": "-..-", "+": ".-.-.",
    '"': ".-..-.", "?": "..--..", "/": "-..-.", "$": "...-..-",
    "_": "..--.-"
}


# Morse code translator function
def translate_sentence(sentence: str):

    sentence = sentence.upper()

    final = ""

    temp = ""

    for word in sentence.split():

        for letter in word:

            result = translation.get(letter)

            if result is None:
                temp += "#" + " "
            else:
                temp += result + " "

        final += temp + "      "

        temp = ""

    return final.strip()


user_input = input("Enter text needed to be converted : ")

print(translate_sentence(user_input))
