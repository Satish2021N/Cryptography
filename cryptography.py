alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input = input("Enter a word: ")

shift_number = int(input("Enter a number to shift  by: "))

string_len = len(string_input)

string_output = ""

for i in range(string_len):
    character = string_input[i]
    location_of_character = alphabets.find(character)
    new_location_of_character = (location_of_character + shift_number)%26
    string_output += alphabets[new_location_of_character]

print("Encryted: ", string_output)