x=[]
z=[]
with open('desktop/litere.txt','r+') as f :
    x=f.read()
for i in range(len(x)):
    if x[i]=='a' or x[i]=='A':
        z.append(x[i])
    elif x[i]=='e' or x[i]=='E':
        z.append(x[i])
    elif x[i]=='i' or x[i]=='I':
        z.append(x[i])    
    elif x[i]=='o' or x[i]=='O':
        z.append(x[i])
    elif x[i]=='u' or x[i]=='U':
        z.append(x[i])
with open('desktop/litere.txt','a') as f :
    f.write('\nAceste sunt vocalele:\n')
    f.write(str(z))
