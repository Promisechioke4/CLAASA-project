# import pyscript
# import keyboard
import time
import sys

# AUTHENTICATING .py to .html using PyScript. No longer used.
# print("Hello World")
# output = document.querySelector("#divide")
# output.innerText = "Hello World"

# text1 == List1
text1 = input("Enter data: ")
text1 = list(text1.split())
done = "Are you done typing? Yes or No"
print(done)

yn1 = "Yes"
yn2 = "No"

while True:
  ask = input("")
  if ask == yn1:
    print("Successful, length =", len(text1))
    break
  elif ask == yn2:
    # allow the user to continue typing; update text1 with additional input
    more = input("Continue typing: ").split()
    text1 += more
    print(done)
  else:
    print("Unavailable response")
    
# def on_typing(text):
#     keyboard.on_press(on_typing)
#     keyboard.wait()
# print(text)

# def simulate_typing(text):
#     for char in text:
#         sys.stdout.write(char)
#         sys.stdout.flush()
#         time.sleep(0.05)
# simulate_typing("Hello! I am responding to your input.")

# text2 == List2
text2 = input("Enter data for Secondary List: ")
text2 = list(text2.split())
print(done)

while True:
  ask = input("")
  if ask == yn1:
    print("Successful, length =", len(text2))
    break
  elif ask == yn2:
    # allow the user to continue typing; update text2 with additional input
    more = input("Continue typing: ").split()
    text2 += more
    print(done)
  else:
    print("Unavailable response")
    
if len(text1) == len(text2):
  print("Lengths match.")
  # while True: (caused the repitition error)
    
  sys.stdout.write('.')
  sys.stdout.flush()
  time.sleep(1)
    
    # Print 2nd dot
  sys.stdout.write(' .')
  sys.stdout.flush()
  time.sleep(1)
    
    # Print 3rd dot
  sys.stdout.write(' .')
  sys.stdout.flush()
  time.sleep(1)
  
  sys.stdout.write("\r" "\n") #\r same line, \n new line
  sys.stdout.flush()
  time.sleep(1)
  
  print(dict(zip(text1, text2)))
  
else:
    print("Length of lists do not match.")
    
# split() to count word by word; remove split() and it counts character(letter) by character(letter).