def Levensteindistance(Inputstring,outputstring):

    count=0 #initialise counter as zero
# if two strings are equal in length then we only need to make substitutions to make changes to the string
    
    if len(Inputstring)==len(outputstring):
        for i in range(len(Inputstring)):
            if Inputstring[i]!=outputstring[i]:
                count=count+1
# if length of one string is either greater than or less than the other string then we need to make substitutions as well as addition or deletions as per the case    
   
    elif len(outputstring)>len(Inputstring):
        for i in range(len(Inputstring)):
            if outputstring[i]!=Inputstring[i]:
                count=count+1
        count=count+len(outputstring)-len(Inputstring)

    elif len(outputstring)<len(Inputstring):
        for i in range(len(outputstring)):
            if outputstring[i]!=Inputstring[i]:
                count=count+1
        count=count+len(Inputstring)-len(outputstring)

    return count
