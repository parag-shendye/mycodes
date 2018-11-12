import matplotlib.pyplot as plt
import seaborn as sns

with open('rdf_sio2.rdf','r') as f:
    s=f.readlines()

a=[]    
for i in range(len(s)):
    if len(s[i].split())<3 or s[i].startswith('#'):
        continue
    else:
        a.append(s[i])



b=[]
c=[]
d=[]
e=[]
for i in range(len(a)):
    b.append(float(a[i].split()[2]))
    c.append(float(a[i].split()[4]))
    d.append(float(a[i].split()[6]))
    e.append(float(a[i].split()[1]))
    

sns.lineplot(e,b)
sns.lineplot(e,c)
sns.lineplot(e,d)
    
