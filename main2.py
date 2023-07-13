str = input ("enter the str")
modified_str = ''
for char in range(0, len(str)):
    
    if(str[char] == 'l' or str[char] =='u'):
        
        modified_str += '*'
    else:
        
       modified_str += str[char]
print(modified_str)
  