# list of alphabet letters ot be used
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# caesar function start
def caesar(start_text, shift_amount, cipher_direction):
  # blank string variable for the end result after 
  end_text = ""
  # if user's choice is decode, then the shift amount needs to be reversed, so multiply by -1
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    # if input character is not alphabetic, add it anyways, but do not encode/decode it
    if char not in alphabet:
      end_text += char
      continue
    # start within the alphabet list where character is
    position = alphabet.index(char)
    # process the shift, modulo 26 afterward so it does not go outside list range
    new_position = (position + shift_amount) % 26
    # add the new positioned letter to the end_text variable
    end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}\n")

# Import and print the logo from art.py when the program starts.
import art

print(art.logo)

# boolean variable to continue while loop
restart = True
while restart:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Would you like to restart the cipher program, yes or no?\n")
  if restart == "no":
    restart = False
    print("Goodbye")
    
