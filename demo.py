class node : 
     def __init__(self, data) -> None :
          self.data = data
          self.next = None

class linkedlist : 
     def __init__(self) -> None :
          self.head = None

     def addNode() -> None:
          # adding comment
          # making changes in sample branch
          # making changes in master branch

          # making changes in sample2 branch
          pass

     def showll() -> list:
          # it will return list of all ll elements.
          pass

<<<<<<< HEAD
     def deleteNode(self, data) -> None:
          # enter data we will drop that node
=======
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
     
     def deleteNode(self, data) -> str : 
          if self.head == None : 
               return 'LL is empty!'
          else : 
               temp = self.head
               # head ka element hi victim ho
               if temp.data == data : 
                    self.head = temp.next
               else : 
                    while temp.next : 
                         if temp.data == data : 
                              # update it
                              pass
                         else :
                              pass
               return
>>>>>>> addNode1

          pass 

