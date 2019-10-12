def Palindrome_Check (String):
    countt = 0
    i = 0 # initiated to approach string from left end
    j = len(String)-1 #simulataneously approach from right end
    while (i <= j):
        if ( String[i] == String[j]):
            countt = countt +1 #increment count each time encounter same value
        i=i+1
        j=j-1
    if(countt == ((len(String)//2)+(len(String)%2))): #when count becomes equal to number steps it moved before i=j
        return True
    else:
        return False

##########another method##############
def palindrome_check2(string_input):
    if string_input==string_input[::-1] :
        return True
    else:
        return False

print(palindrome_check2("abcba"))



def Anagram_Check (Strings):
    from itertools import permutations
    Anags = [''.join(p) for p in permutations(Strings)] #permute all the letters of the strings and then join them to make different strings
    count = 0
    for i in range(len(Anags)): # extracting strings and parsing them to palindrome function
        Palin = Anags[i]
        print (Palin , "is a palindrome" , Palindrome_Check (Palin))
        if(Palindrome_Check (Palin)):
            count = count+1
    if(count > 0):
        return True
    else:
        return False

