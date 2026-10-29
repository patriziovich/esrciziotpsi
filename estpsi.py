string = input("Inserisci una stringa: ")
string += "$"
print(string)

stringInvert = []
for i in range(len(string)):
    stringInvert.append(string[i:] + string[:i])
    
    stringInvert.sort()
    
    btw=""
for rotazione in stringInvert:
        btw += rotazione[-1]
        
   
print("risultato btw: " + btw)      
    