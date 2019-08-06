def printWithSpaces(str):
    if str!="":
        print(str[0]+" ", end="")
        printWithSpaces(str[1:])


printWithSpaces("space")

def weave(str1,str2):
    a = ""
    if str1 == a:
        return a + str2
    if str2 == a:
        return a + str1
    else:
        return str1[0] + str2[0] + weave (str1[1:], str2[1:])

print (weave('Jcbut' , 'aoHr'))
