with open ('Desktop/Lista Clasei 11A.txt','r') as f:
    lista=f.readlines()
se,sg,de,dg=0,0,0,0
with open('desktop/Lista Clasei 11A.Engleza.txt','a') as g:
    g.write("Nume Prenume       Nota")
    g.write('\n')
with open('desktop/Lista Clasei 11A.Germana.txt','a') as z:
    z.write("Nume Prenume       Nota")
    z.write('\n')
for i in lista:
    coloana = i.split()
    if coloana[3]=="Engleza" or coloana[3]=="engleza":
        se+=int(coloana[2])
        de+=1     
        with open('desktop/Lista Clasei 11A.Engleza.txt','a') as g:
            b=coloana[0]+' '+coloana[1]+'   '+coloana[2]+'\n'
            g.write(b)
    elif coloana[3]=="Germana" or coloana[3]=="germana":
        sg+=int(coloana[2])
        dg+=1
        with open('desktop/Lista Clasei 11A.Engleza.txt','a') as z:
            a=coloana[0]+' '+coloana[1]+'   '+coloana[2]+'\n'
            z.write(a)
with open('desktop/Lista Clasei 11A.Engleza.txt','a') as g:
    g.write('Nota medie la Engleza= '+str(se/de))
with open('desktop/Lista Clasei 11A.Germana.txt','a') as z:                
    z.write('Nota medie la Germana= '+str(sg/dg))
    
    
            
    