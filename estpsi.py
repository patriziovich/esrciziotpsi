string = input("Inserisci una stringa: ")
string += "$"
print(string)

stringInvert = []
for i in range(len(string)):
    stringInvert.append(string[i:] + string[:i])
    
n=len(stringInvert)
for i in range (n):
    for j in range(0,n-1-i):
        if stringInvert[i]>stringInvert[j+1]:
            m=stringInvert[j]
            stringInvert[j]=stringInvert[j+1]
            stringInvert[j+1]=m
    
btw=""
for rotazione in stringInvert:
        btw += rotazione[-1]
        
   
print("risultato btw: " + btw)      
    