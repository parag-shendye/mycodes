# defining paths for both source and target files
def commentremover(sourcefile,Targetfile):

#open source file as readable and Target file as apendable
    S=open(sourcefile,'r')

    T=open(Targetfile,'a')
    for line in S.readlines():
        if not line.startswith("#"):# this command checks for line not beginning with "#" 
            T.write(line) 
                
#Close both the files                 
    S.close()
    T.close()
        
