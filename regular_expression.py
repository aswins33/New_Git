'''import re 

text = "The rain11 in SPAIN falls Mainly on the34 plain."

result=re.findall(r"[A-Za-z]+",text)

print(result)'''


import re

password = "Aswin@%123[###]"

pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

if re.match(pattern, password):
    print("Valid password")
else:
    print("Invalid password")