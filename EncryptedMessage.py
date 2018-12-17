
alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 3
New_Message = ''


Message = input('Please enter a message: ')

for Character in Message:
    if Character in alphabet:
      Position = alphabet.find(Character)
      New_Position = (Position + key) % 26
      New_Character = alphabet[New_Position]
      New_Message += New_Character
    else:
        New_Message += Character

print ('Your encrypted message is:',New_Message)

