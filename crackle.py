print("""
──▄▀▀▀▄───────────────
──█───█───────────────
─███████─────────▄▀▀▄─
░██─▀─██░░█▀█▀▀▀▀█░░█░
░███▄███░░▀░▀░░░░░▀▀░░

╔═╗╦═╗╔═╗╔═╗╦╔═╦  ╔═╗
║  ╠╦╝╠═╣║  ╠╩╗║  ║╣ 
╚═╝╩╚═╩ ╩╚═╝╩ ╩╩═╝╚═╝
 """)
import sys
import hashlib
print("*"*50)

flag=0
print("-"*50)
pass_hash=input("Enter md5 hash: ")
wordlist=input("enter wordlist file name: ")
if wordlist == "":
	wordlist="Wordlist/rockyou.txt"       			
print("-"*50) 

print("Hash ---->", pass_hash)
print("Wordlist ---->", wordlist)
print("_"*50) 

       			 # Open File/wordlist
try:
    pass_file=open(wordlist, "r")
except:
    print("no file named", wordlist)
			# Convert the word of wordlist into hash
for word in pass_file:
    encoded_word=word.encode(' utf-8 ')
    converted_hash=hashlib.md5(encoded_word.strip()).hexdigest()
    			# Match the hashes
    if converted_hash == pass_hash:
        print("password caracked")
        print("Password: " + word)
        flag=1
        break
# if not matched
if flag == 0:
	print("Password is not in the list you provided")
	quit()
	print("|"*50)
    
    
    
def m(**m):
	print("hlo")
