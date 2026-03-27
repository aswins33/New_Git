import os
from random import randint
import time

pas = input("send the password")
keys = "1","2","3","4","5","6","7","8","9","0", 
"a","b","c","d","e","f","g","h","i","j",    
"k","l","m","n","o","p","q","r","s","t",    
"u","w","x","y","z"

pwg = ""
attempts = 0
start_time = time.time()

while pwg !=pas:
        pwg = ""
        attempts += 1

        for i in range(len(pas)):
                guesspass = keys[randint(0,4)]
                pwg = str(guesspass) + str(pwg)
                print(pwg)
                print("attacking....please wait")
                os.system("cls")


end_time = time.time()
total_time = end_time - start_time

print(f"The pass is : {pwg}")
print(f"Total attempts : {attempts}")
print(f"Time Taken : {total time:.2f} seconds")