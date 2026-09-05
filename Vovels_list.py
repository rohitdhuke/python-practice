letters = [
    "A", "B", "C", "D", "E", "F", "G",
    "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U",
    "V", "W", "X", "Y", "Z"
]

vowels = []

for i in range(len(letters)):

    if letters[i] == "A" or letters[i] == "E" or letters[i] == "I" or letters[i] == "O" or letters[i] == "U":
        vowels.append(letters[i])

print(vowels)
print(letters)