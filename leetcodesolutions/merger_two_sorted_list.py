# Linked List

class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


class HeadValue():
    def __init__(self):
        self.head = None

    def printlist(self):
        printvalue = self.head
        while printvalue is not None:
            print(printvalue.data)
            printvalue = printvalue.next


list = HeadValue()
while True:
    list.head = Node(1)
val1 = Node(2)
val2 = Node(3)

list.head.next = val1
val1.next = val2

list.printlist()



def List_input():
    list =[]
    value='a'
    while value!='':
        value=int(input("Enter the value to create a list: "))
        list.append(value)
    list.pop()
    return list

for i in range(2):
    list = List_input()

    print("List" + str(i) + "= ",list)


