import re

def doesRhyme(LineOne: str, LineTwo: str) -> bool:
    #* split String in words
    LineOne = LineOne.split()
    LineTwo= LineTwo.split()
    
    #* only use last word and lower it
    LineOne = LineOne[-1].lower()
    LineTwo = LineTwo[-1].lower()

    #* filter vowels
    LineOne = re.findall("[aeiou]", LineOne)
    LineTwo = re.findall("[aeiou]", LineTwo)
    LineOne = ''.join(LineOne)
    LineTwo = ''.join(LineTwo)

    #* Compare and output
    return LineOne == LineTwo

print(
doesRhyme("Sam I am!", "Green eggs and ham."),
doesRhyme("Sam I am!", "Green eggs and HAM."),
doesRhyme("You're built like a seat", "I bet you like to eat"),
doesRhyme("You are off to the races", "a splendid day."),
doesRhyme("and frequently do?", "you gotta move.")
)
