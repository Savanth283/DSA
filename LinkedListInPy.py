#Operations in Linked List

class Node:
  def __init__(self,dataval=None):
    self.dataval = dataval 
    self.nextval = None

class Linkedlistp:
  def __init__(self):
    self.headval=None
    
#Insert Operation in LinkedList  
  def atBegin(self,newdata): #adding a new node at the begin 
    NewNode = Node(newdata)
    NewNode.nextval = self.headval 
    self.headval = NewNode

  def atEnd(self,newdata1):  #adding a new node at the end
    NewNode1 = Node(newdata1)
    if self.headval is None:
      self.headval = NewNode1 
      return 
    last =  self.headval 
    while(last.nextval):
      last = last.nextval 
    last.nextval = NewNode1
  
  def inBetween(self,newdata2,prevdata):
    NewNode2 = Node(newdata2)
    if prevdata is None:
      print("The given previous node must be present")
      return 
    
    prevdata = self.headval 

    NewNode2.nextval = prevdata.nextval
    prevdata.nextval = NewNode2

  def listprint1(self):        #prinitng the linked List
    printval = self.headval
    while printval is not None:
      print(printval.dataval)
      printval = printval.nextval
 
#assigning the values 
list = Linkedlistp()
list.headval = Node('23')
e1 = Node('24')
e2 = Node('25')

#assigning the data vals 
list.headval.nextval = e1
e1.nextval = e2

#cutom inputs 
list.atBegin("34")
list.atEnd("45")
list.inBetween(list.headval.nextval,8)

#printing the list 
list.listprint1()
