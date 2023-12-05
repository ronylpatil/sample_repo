

# creating linked list
from dataclasses import dataclass
from tkinter.messagebox import NO


class node : 
     def __init__(self, data) -> None :
          self.data = data
          self.next = None

class linkedlist : 
     def __init__(self) -> None :
          self.head = None

     def addNode(self, data) -> None :
          n1 = node(data)
          if self.head == None :
               self.head = n1
          else : 
               temp = self.head
               while temp.next : 
                    temp = temp.next
               temp.next = n1

     def showll(self) -> list :
          lst = []
          if self.head == None : 
               return lst
          else : 
               temp = self.head
               while temp : 
                    lst.append(temp.data)
                    temp = temp.next
               return lst

obj = linkedlist()
obj.addNode(1)
obj.addNode(2)
obj.addNode(3)
obj.addNode(4)
obj.addNode(5)
print(obj.showll())

