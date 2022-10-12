

class ListNode:
    def __init__(self, newItem, nextNode):
        self.item = newItem
        self.next = nextNode

    
class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode("dummy",None,)
        self.__numItems = 0 
    def __getNode (self, i):
        curr = self.__head
        for index in range(i + 1):
            curr = curr.next
        return curr   
    def insert(self, i:int ,newItem):
        
        
        prev = self.__getNode(i - 1)
        newNode = ListNode(newItem, prev.next)
        prev.next = newNode
        self.__numItems += 1

        
    def append(self,newItem):
        prev = self.__getNode(self.__numItems -1 )
        newNode = ListNode(newItem,prev.next)
        prev.next = newNode
        self.__numItems += 1
    def pop(self,i):
        prev = self.__getNode(i-1)
        curr = prev.next
        prev.next = curr.next
        retItem = curr.item
        self.__numItems -= 1
        return retItem
    def count(self,x):
        cnt = 0
        curr = self.__head.next
        while curr != None:
            if curr.item == x :
                cnt += 1
            curr = curr.next
        return cnt
    def reverse(self):
        a = LinkedListBasic()
        for index in range(self.__numItems):
            a.insert(0,self.get(index))
        self.clear()
        for index in range(a.size()):
            self.append(a.get(index))
    def clear(self):
        self.__head = ListNode("dummy",None)
        self.__numItems = 0
    def size(self):
        
        return self.__numItems
    def remove(self,x):
        curr = self.__findNode(x)
        
        if curr != None:
            curr
            
            
        
    def get (self,i):
        if self.isEmpty():
            return None
        if (i >= 0 and i <= self.__numItems -1):
            return self.__getNode(i).item
        # else:
        # 	return None
    def isEmpty(self):
        return self.__numItems == 0

    def printList(self):
        curr = self.__head.next
        while curr != None:
            print(curr.item,end = " ")
            curr = curr.next
    def extend(self,a):
        for index in range(a.size()):
              self.append(a.get(index))
if __name__ == "__main__":
    List = LinkedListBasic()
    List.append(30)
    List.insert(0,20)

    a = LinkedListBasic()
    a.append(4)
    a.append(3)
    a.append(3)
    a.append(2)
    a.append(1)

    List.extend(a)
    List.reverse()
    List.pop(0)

    print("count(3): ",List.count(3))
    print("get(2): ",List.get(2))


    List.printList()


    