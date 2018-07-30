import os
import shutil

for i in range(2,40,2):
    inputfile ="G:\\shockwave\\Graphene_ann\\cracklength_47_53\\input_47_53.in"#give path for source file

    S=open(inputfile,'r')

    y1=47.0-(i)# subtracting and adding increase in cracklength to y coordinates
    y2=53.0+(i)

    mypath = "G:\\shockwave\\Graphene_ann\\cracklength_"+str(y1)+"_"+str(y2)
    if not os.path.isdir(mypath):#creating multiple directories to store data separately on the basis of crack length
       os.makedirs(mypath)

    src="G:\\shockwave\\Graphene_ann\\tocopy" # copying additional files from other directory to these directories
    src_files = os.listdir(src)
    for file_name in src_files:
        full_file_name = os.path.join(src, file_name)
        if (os.path.isfile(full_file_name)):
            shutil.copy(full_file_name,mypath )



    #copying data from inputfile to target and then making desired changes in particular lines as required for simulation
    #Target="G:\\shockwave\\Graphene_ann\\cracklength_"+str(y1)+"_"+str(y2)+"\\"+"input_"+str(y1)+"_"+str(y2)+".in"
    Target="G:\\shockwave\\Graphene_ann\\cracklength_"+str(y1)+"_"+str(y2)+"\\"+"input.in"
    T=open(Target,'w')
    p=S.readlines()
    p[13]='region\t\tdelete block 48.0 52.0'+' '+str(y1)+" "+str(y2)+' '+ 'INF INF\n'
    p[14]='region \t\tdelete1 cylinder z 50.0'+' '+str(y1)+' '+'2.0 INF INF\n'
    p[15]='region \t\tdelete2 cylinder z 50.0'+' '+str(y2)+' '+'2.0 INF INF\n'
    T.write("".join(p[0:len(p)]))
    T.close()

