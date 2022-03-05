#{ 
#Driver Code Starts
#Initial Template for Python 3

 # } Driver Code Ends
#User function Template for python3


class Character:
    def __init__(self, Name, hp):
        self.name = Name ##Assigning name to the current object's name variable
        self.hp = hp ##Assigning hp to the current object's hp variable
    def boost(self, boost):
        self.hp = self.hp * boost ## boosting current object's hp
    def getName(self):
        return self.name##complete this. Return name of the current object
    def getHp(self):
        return self.hp##complete this. return hp of the current object


def fusion(a, b):
    ##This function takes two Character objects as parameter
    ## Create a new object that has name equal to first-half of a's name + last-half of b's name
    ## Also new object's hp is the sum of a's hp + b's hp
    ##return the newly created object
    x = len(a.name)//2
    y = len(b.name)//2
    return Character( a.name[:x] + b.name[y:],  a.hp + b.hp)
    
    
def show(a): ##Already completed
    print(a.getName(), a.getHp()) ##printing the newobject's name and hp


#{ 
#Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        ##input object1
        Name1 = input()
        hp1 = int(input())
        boost1 = int(input())
        ##input object2
        Name2 = input()
        hp2 = int(input())
        boost2 = int(input())
        ##creating objects 1 and 2
        chara1 = Character(Name1, hp1)
        chara1.boost(boost1)
        
        chara2 = Character(Name2, hp2)
        chara2.boost(boost2)
        ##fuse and show the result
        show(fusion(chara1, chara2))
        testcases -= 1
        


if __name__=='__main__':
    main()
#} Driver Code Ends