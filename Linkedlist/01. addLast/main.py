class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.size=0
        self.tail=None

    # write here (Add Last)
    def AddLast(self, newdata):
        node = Node(newdata)
        if self.size == 0:
            self.head = node
            self.tail = node
    
        else:
            # size != 0
            self.tail.next = node
            self.tail = node
        self.size += 1
   
    
    def listprint(self):
        printval = self.head
        while printval is not None:
            print (printval.data)
            printval = printval.next

         

    def printList(self) :
        temp = self.head
        while temp is not None: 
            print(temp.data)
            temp = temp.next

       

l1 = SLinkedList()
while 1>0 :
    str=input()
    if str[0]=='q':
        break

    if str[0]=='a':
        val=int(str[2:])
        l1.AddLast(val)
        
        
l1.printList()