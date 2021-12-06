with open('desktop/INPUT.txt','r') as f:
    x=f.readlines()
medie=0
print("Nr.    Nume        Prenume       Nota(1) Nota(2) Nota(3)")
for i in x:
    col=i.split()
    print(col[0],(3-len(col[0]))*' ',col[1],(12-len(col[1]))*' ',col[2],(12-len(col[2]))*' ',col[3],(6-len(col[3]))*' ',col[4],(6-len(col[4]))*' ',col[5])
for d in x:
    s=d.split()
    with open('desktop/REZERVA.txt','a') as g:
        a=s[0]+(3-len(s[0]))*' '+s[1]+(12-len(s[1]))*' '+s[2]+(12-len(s[2]))*' '+s[3]+(6-len(s[3]))*' '+s[4]+(6-len(s[4]))*' '+s[5]+'\n'
        g.write(a)
print("\nNr.    Nume        Prenume       Media")
for a in x:
    h=a.split()
    medie=float(h[3])+float(h[4])+float(h[5])
    print(h[0],(3-len(h[0]))*' ',h[1],(12-len(h[1]))*' ',h[2],(12-len(h[2]))*' ',medie/3)
    with open('desktop/output','a') as j:
        c=h[0]+(3-len(h[0]))*' '+h[1]+(12-len(h[1]))*' '+h[2]+(12-len(h[2]))*' '+str(medie/3)+'\n'
        j.write(c)