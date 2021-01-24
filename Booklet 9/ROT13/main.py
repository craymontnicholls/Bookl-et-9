#ROT13 Problem

#imports
from time import sleep

#declare global vars
global alphabet_lower , alphabet_upper
alphabet_lower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alphabet_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#subroutine to run ROT13 Algorithm
def ROT13(file_from,file_to):

  print("Encrypting file. \nPlease Wait...")

  file = open(file_from,"r")

  new_text_file = open(file_to,"w")
  new_text_file.write("")
  new_text_file.close()

  for text in file:
    for x in range(0,len(text),1):
      if text[x] == " ":
        new_char = " "

      elif text[x].islower() == True:
        char_pos = alphabet_lower.index(text[x])
        new_char_pos = char_pos + 13
        if new_char_pos > 25:
          new_char_pos -= 25
        new_char = alphabet_lower[new_char_pos]

      elif text[x].isupper() == True:
        char_pos = alphabet_upper.index(text[x])
        new_char_pos = char_pos + 13
        if new_char_pos > 25:
          new_char_pos -= 26
        new_char = alphabet_upper[new_char_pos]

      else: 
        new_char = text[x]

      new_text_file = open(file_to,"a")
      new_text_file.write(new_char)
      new_text_file.close()

  file.close()

  sleep(3)
  print("\n\nEncyption Complete.")


ROT13("inputtext.txt","outputtext.txt")