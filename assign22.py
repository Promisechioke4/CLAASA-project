My_List = ["mummy", "hannah", "murder for a jar of red rum", "mom", "seagull","tomato", "no lemon", "no melon", "some men interpret nine memos", "madam"]

# Using for loop without removing spaces

for strings in My_List:
    if strings[0::1] == strings[::-1]:
        print(f"Yes, {strings} is a palindrome.")
    else:
        print(f"No, {strings} is not a palindrome.")
        
# Removing spaces
for nospaces in My_List:
    drag = "".join(c.lower() for c in nospaces if c.isalnum())
    if drag == drag[::-1]:
        print(f"Yes, {nospaces} is a palindrome.")
    else:
        print(f"No, {nospaces} is not a palindrome.")
        
# Done by Chimereucheya Patriarch Okoroafo
# Class Number - A1