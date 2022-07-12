string = [84, 104, 101] # the ascii numbers you want to be converted
answer = "" # the converted version

for word in string: # for each thing in string variable
    answer += chr(word) # combines the ascii so it comes in words/sentences

print(answer) # outputs the final converted version