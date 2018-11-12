import os
import csv
#saving all the files of dir into a list
textfilesList = os.listdir("G:\\to_Parag\\py_a")
x=241.892#(use from 100 to 248)
#x=322.3077#(use from 256 to 296)
#z=394.3077
for j in range(0,len(textfilesList)):
        
        inputfile="G:\\to_Parag\\py_a" + "\\" + textfilesList[j]#change to "G:\\to_Parag\\py_a" for 104 to 248
        
        
        with open(inputfile,'r') as csvfile:
            read=csv.reader(csvfile,delimiter=' ')
            a=[]
            b=[]
            for line in read:
                    a.append(line[0])
                    b.append(line[1])


        z=x
        p=0
        q=0
        r=0
        s=0
        t=0
        u=0
        for i in range(len(a)):
                if(int(a[i])==2):
                        if (float(b[i])>(z-21.566) and float(b[i])<=z):
                                p=p+1

        z=(z-21.566)

        for i in range(len(a)):
                if(int(a[i])==2):
                        if(float(b[i])>(z-20.067) and float(b[i])<=z):
                                q=q+1
        z=z-20.067
        for i in range(len(a)):
               if(int(a[i])==2):
                       if (float(b[i])>(z-17.287) and float(b[i])<=z):
                               r=r+1
        z=z-17.287
        for i in range(len(a)):
                if(int(a[i])==2):
                         if (float(b[i])>(z-13.242) and float(b[i])<=z):
                                 s=s+1
        z=z-13.242
        for i in range(len(a)):
                if(int(a[i])==2):
                        if (float(b[i])>(z-8.324) and float(b[i])<=z):
                                t=t+1
        z=z-8.324
        for i in range(len(a)):
                if(int(a[i])==2):
                        if(float(b[i])>(z-2.84) and float(b[i])<=z):
                                u=u+1

        arp=p*3.141*0.060*0.060*0.1305
        arq=q*3.141*0.060*0.060*0.382
        arr=r*3.141*0.060*0.060*0.608
        ars=s*3.141*0.060*0.060*0.793
        art=t*3.141*0.060*0.060*0.923
        aru=u*3.141*0.060*0.060*1

        sasa_ox=arp+arq+arr+ars+art+aru

        print(sasa_ox)
        #print(x)

        #x=x+2.0#(use for 256 to 296)
        x=x-2.0#(use for 100 to 248)
        #+(21.566+20.067+17.287+13.242+8.324)


                
##        file_ox=open("G://to_Parag//ox_136000.txt",'w')
##        file_ox.write(str(sasa_ox)+"\n")
##        file_ox.close()
##        file_ox=open("G://to_Parag//ox_136000.txt",'a')
##        file_ox.write("done")
##        file_ox.close()
##

                 
                     
                        
                
            




                        



	    
	    
	    

	    
	    

