"""
 * StringNode.py
 *
 * Adopted from David G. Sullivan, Ph.D. Computer Science E-22
 * Modified by: <your name>, <your e-mail address>
 */

/**
 * A class for representing a string using a linked list.  Each
 * character of the string is stored in a separate node.  
 *
 * This class represents one node of the linked list.  The string as a
 * whole is represented by storing a reference to the first node in
 * the linked list.  The methods in this class are class methods that
 * take a reference to a string linked-list as a parameter.  This
 * approach allows us to use recursion to write many of the methods.
 */ 
"""
class StringNode():

    # Constructor
    def __init__(self, c, n):
        self.ch = c;
        self.next = n;
    #
    # getNode - private helper method that returns a reference to
    # node i in the given linked-list string.  If the string is too
    # short, returns null.
    #
    def getNode(astr, i):
        if i < 0 or astr == None:
            return None
        elif i == 0:
            return astr
        else:
            index=0
            while(astr!=None):
                if(index==i):
                    return astr
                astr=astr.next
                index=index+1
            return None

    #/*****************************************************
    #* class methods (in alphabetical order)           *
    #*****************************************************/

    # 
    # charAt - returns the character at the specified index of the
    # specified linked-list string, where the first character has
    # index 0.  If the index i is < 0 or i > length - 1, the method
    # will end up printing an error message and returning a -1.
    #
    def charAt(astr, i):
        if astr == None:
            print("the string is empty")
        
        node = StringNode.getNode(astr, i)

        if node != None:
           return node.ch     
        else:
            print("invalid index: " + str(i))
            print("The string is too short.")
            return ""


    # 
    # concat - returns the concatenation of two linked-list strings
    #
    def concat(str1, str2):
        if str1 == None:
            cat = StringNode.copy(str2)
        else:
            cat = StringNode(str1.ch,None)
            temp=cat
            str1=str1.next
            while(str1!=None):
                temp.next=StringNode(str1.ch,None)
                temp=temp.next
                str1=str1.next
            while(str2!=None):
                temp.next=StringNode(str2.ch,None)
                temp=temp.next
                str2=str2.next

        return cat
    
    #
    # contains - returns true if the linked-list string astr contains
    # at least one occurrence of the character ch, and false otherwise.
    # 
    def contains(astr, ch):
        if astr == None:
            return False
        if astr.ch == ch:
            return True
        else:
            while(astr!= None):
                if(astr.ch==ch):
                    return True
                astr=astr.next
            return False

    #
    # convert - converts a standard Python string to a linked-list
    # string and returns a reference to the linked-list string
    # 
    def convert(s):
        if s == None or len(s) == 0:
            return None

        firstNode = StringNode(s[0], None)
        prevNode = firstNode
    
        for i in range(1, len(s)):
            nextNode = StringNode(s[i], None)
            prevNode.next = nextNode
            prevNode = nextNode

        return firstNode
    
    #
    # copy - returns a copy of the given linked-list string
    #
    def copy(astr):
        if astr == None:
            return None
        copyFirst = StringNode(astr.ch, None)
        currchar= copyFirst
        astr=astr.next
        while(astr!= None):
            currchar.next= StringNode(astr.ch,None)
            currchar=currchar.next
            astr=astr.next
        return copyFirst

    #
    # deleteChar - deletes character i in the given linked-list string and
    # returns a reference to the resulting linked-list string
    #
    def deleteChar(astr, i):
        if astr == None:
            print("string is empty.")
        elif i < 0: 
            print("invalid index: " + str(i))
        elif i == 0: 
            astr = astr.next
        else:
            prevNode = StringNode.getNode(astr, i-1)
            if prevNode != None and prevNode.next != None: 
                prevNode.next = prevNode.next.next
            else:
                print("invalid index: " + str(i))
        return astr

    #
    # indexOf - returns the position of the first occurrence of
    # character ch in the given linked-list string.  If there is
    # none, returns -1.
    #
    def indexOf(astr, ch):
        if astr == None:         # base case 1: ch wasn't found
            return -1
        elif astr.ch == ch:      # base case 2: ch was just found
            return 0           
        else:
            index=0
            indexInRest = StringNode.indexOf(astr.next, ch)
            while(astr!= None):
                if(astr.ch==ch):
                    return index
                astr=astr.next
                index=index+1
            return -1

    #
    # insertChar - inserts the character ch before the character
    # currently in position i of the specified linked-list string.
    # Returns a reference to the resulting linked-list string.
    # 
    def insertChar(astr, i, ch):
        if i < 0: 
            print("invalid index: " + str(i))
        elif i == 0:
            newNode = StringNode(ch, astr)
            astr = newNode
        else:
            prevNode = StringNode.getNode(astr, i-1)
            if prevNode != None:
                newNode = StringNode(ch, prevNode.next)
                prevNode.next = newNode
            else: 
                print("invalid index: " + str(i))

        return astr

    # 
    # insertSorted - inserts character ch in the correct position
    # in a sorted list of characters (i.e., a sorted linked-list string)
    # and returns a reference to the resulting list.
    #
    def insertSorted(astr, ch):

        # Find where the character belongs.
        trail = None
        trav = astr
        while trav != None and trav.ch < ch:
            trail = trav
            trav = trav.next

        # Create and insert the new node.
        newNode = StringNode(ch, trav)
        if trail == None:
            # We never advanced the prev and trav references, so
            # newNode goes at the start of the list.
            astr = newNode
        else: 
            trail.next = newNode

        return astr

    #
    # length - recursively determines the number of characters in the
    # linked-list string to which astr refers
    # 
    def length(astr):
        if astr == None:
            return  0
        else:
            len=0
            while(astr!= None):
                len=len+1
                astr=astr.next
            return len

    #
    # print - recursively printsthe specified linked-list string
    # 
    def print(astr):
        if astr == None:
            return
        else:
            while(astr!= None):
                print(astr.ch)
                astr=astr.next



    #
    # printReverse - recursively prints the reverse of the specified 
    # linked-list string 
    #
    def printReverse(astr):
        if astr == None:
            return
        else:
            newList=[]
            while(astr!= None):
                newList.insert(0,astr.ch)
                astr=astr.next
        for i in range(len(newList)):
            print(newList[i])
   
    #
    # toUpperCase - converts all of the characters in the specified
    # linked-list string to upper case.  Modifies the list itself,
    # rather than creating a new list.
    #
    def toUpperCase(astr):        
        trav = astr 
        while trav != None:
            trav.ch = trav.ch.upper() 
            trav = trav.next

    def printMirrored(astr):
        copy = StringNode.copy(astr)
        if astr == None:
            return
        else:
            print(copy.ch)
            StringNode.printMirrored(copy.next)
            print(copy.ch)
            

def main():
    
    # convert, print, and toUpperCase
    astr = StringNode.convert("fine")
    print("Here's a string: ")
    StringNode.print(astr)

    print()
    print("Here it is in upper-case letters: ")
    StringNode.toUpperCase(astr)
    StringNode.print(astr)
    print()
    print("Here it is mirrored: ")
    StringNode.printMirrored(astr)
    print()
    


    # read, toString, length, and printReverse.
    s = input("Type a string: ")
    str1 = StringNode.convert(s)
    print("Your string is: ") 
    StringNode.print(str1)       # implicit toString call
    print("\nHere it is reversed: ")  
    StringNode.printReverse(str1)
    print("\nIts length is " + str(StringNode.length(str1)) + " characters.")

    # charAt
    n = -1
    while n < 0:
        n = eval(input("\nWhat # character to get (>= 0)? "))
        
    ch = StringNode.charAt(str1, n)
    print("That character is " + ch)

    # contains and indexOf
    ch = input("\nWhat character to search for? ")
    print("Using contains to see if " + ch + " is in the string...")
    if (StringNode.contains(str1, ch)):
        print("it is.")
        n = StringNode.indexOf(str1, ch)
        print("indexOf returns: " + str(n))
    else:
        print("it is not.")
        n = StringNode.indexOf(str1, ch)
        print("indexOf returns: " + str(n))
    
    # deleteChar and copy
    n = -1
    while n < 0:
        n = eval(input("\nWhat # character to delete (>= 0)? "))
    copy = StringNode.copy(str1)
    str1 = StringNode.deleteChar(str1, n)
    StringNode.print(str1)
    print("\nUnchanged copy: ")
    StringNode.print(copy)
    print()
    
    # insertChar
    n = -1
    while n < 0:
        n = eval(input("\nWhat # character to insert before (>= 0)? "))
    line = input("What character to insert? ")
    str1 = StringNode.insertChar(str1, n, line[0])
    StringNode.print(str1)
    print()

    # concat
    s = input("\nType another string: ")
    str2 = StringNode.convert(s)
    print("Its length is " + str(StringNode.length(str2)) + " characters.")
    print("\nconcatenation = ")
    StringNode.print(StringNode.concat(str1, str2))
    print()
    
    # insertSorted
    s = input("\nType a string of characters in alphabetical order: ")
    str3 = StringNode.convert(s);
    line = input("What character to insert in order? ")
    str3 = StringNode.insertSorted(str3, line[0])
    StringNode.print(str3)
    print()
    
main()
