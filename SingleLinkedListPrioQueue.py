class node:  
    def __init__(self,data,priority):
        self.data = data
        self.prio = priority
        self.next = None 

class linkedlist:
    def __init__(self):  
        self.head = None

def print_linked_list(linked_list):
    if linked_list.head == None:
        print("The linked list is empty")
        return
    current = linked_list.head 
    index = 1
    print(f"\033[1;35;1m|{'Queue':5}|\033[1;33;1m |{'Priority':7}|\033[1;32;1m |{'Name'}|\033[1;37;1m")
    while current.next != None:
        print(f"\033[1;35;1m{index:4}\033[1;33;1m {current.prio:9} \t\033[1;37;1m  {current.data:15}\033[1;37;1m ")
        current = current.next
        index += 1
    print(f"\033[1;35;1m{index:4}\033[1;33;1m {current.prio:9} \t \033[1;37;1m {current.data:15}\033[1;37;1m ")
        
def append(linked_list,node):
    if linked_list.head == None :
        linked_list = linkedlist()
        linked_list.head = node
        return linked_list
    elif linked_list.head == None :
        linked_list.head = node
        return linked_list
    elif node.prio <= (linked_list.head).prio and (linked_list.head).next == None:
        node.next = linked_list.head
        linked_list.head = node
        return linked_list
    current = linked_list.head
    while node.prio >= current.prio :
        temporary = current
        if current.next == None:
            temporary.next = node 
            return linked_list
        current = current.next
    temporary.next = node
    node.next = current
    return linked_list

def pop(linked_list):
    if linked_list.head == None:
        print("\033[1;31;1m\nQueue is empty\033[1;37;1m\n")    
    elif ((linked_list.head).next != None) or (linked_list.head != None):
        current = (linked_list.head).next
        linked_list.head.next = None
        linked_list.head = current 
        return 
    elif (linked_list.head).next == None:
        linked_list.head = None
        return 

def to_list(linked_list):
    temporary = list()
    current = linked_list.head
    while current != None:
        temporary.append(current.data)
        current = current.next
    return temporary
   
def should_append_at_the_end_based_on_priority():
    node_1 = node("Name 1",1)
    node_2 = node("Name 2",1)
    node_3 = node("Name 3",2)
    node_4 = node("Name 4",3)
    node_5 = node("Name 5",3)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = None

    temporary_linkedlist = linkedlist()
    temporary_linkedlist.head = node_1

    new_node = node("Yechiel",1)
    temporary_linkedlist = append(temporary_linkedlist,new_node)

    expected = ["Name 1","Name 2","Yechiel","Name 3","Name 4","Name 5"]
    output = to_list(temporary_linkedlist)

    assert expected == output, f"expected {expected} but get {output}"

def should_append_at_the_middle_based_on_priority():
            
    node_1 = node("Name 1",1)
    node_2 = node("Name 2",1)
    node_3 = node("Name 3",2)
    node_4 = node("Name 4",3)
    node_5 = node("Name 5",3)
    node_6 = node("Name 6",4)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = None

    temporary_linkedlist = linkedlist()
    temporary_linkedlist.head = node_1

    new_node = node("Gilbert",2)
    temporary_linkedlist = append(temporary_linkedlist,new_node)

    expected = ["Name 1","Name 2","Name 3","Gilbert","Name 4","Name 5","Name 6"]
    output = to_list(temporary_linkedlist)

    assert expected == output, f"expected {expected} but get {output}"

def should_append_at_the_last_based_on_priority():
    
            
    node_1 = node("Name 1",1)
    node_2 = node("Name 2",1)
    node_3 = node("Name 3",2)
    node_4 = node("Name 4",3)
    node_5 = node("Name 5",3)
    node_6 = node("Name 6",4)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = node_6
    node_6.next = None

    temporary_linkedlist = linkedlist()
    temporary_linkedlist.head = node_1

    new_node = node("Matthew",4)
    temporary_linkedlist = append(temporary_linkedlist,new_node)

    expected = ["Name 1","Name 2","Name 3","Name 4","Name 5","Name 6","Matthew"]
    output = to_list(temporary_linkedlist)

    assert expected == output, f"expected {expected} but get {output}"

def tests():
    print("Configuring tests...")
    should_append_at_the_end_based_on_priority()
    should_append_at_the_middle_based_on_priority()
    should_append_at_the_last_based_on_priority()
    print("Testing complete")

def main():
    
    node_1 = node("Patient 1",1)
    node_2 = node("Patient 2",2)
    node_3 = node("Patient 3",2)
    node_4 = node("Patient 4",3)
    node_5 = node("Patient 5",5)

    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = None

    linked_list      = linkedlist()
    linked_list.head = node_1

    print_linked_list(linked_list)

    while True:
        print("\n\033[1;36;1m\nWelcome to EinGetroffen Hospital")
        choice = input("\033[1;37;1m1. Append\n2. Pop\n3. Print All Queue\n4. Exit\n Choice : ")
        if choice == "1":
            while True :
                patient_name = input("Name     : ")
                try:
                    priority = int(input("Priority : "))
                except ValueError:
                    print("\033[1;31;1m\nPriority can only be integer\033[1;37;1m\n")
                    continue
                if priority < 0 or priority > 5 :
                    print("\033[1;31;1m\nPriority only scales from 1-5\033[1;37;1m\n")
                else:
                    break
            new_node = node(patient_name,priority)
            linked_list = append(linked_list,new_node)
            print_linked_list(linked_list)
            print()
        elif choice == "2":
            pop(linked_list)
            print_linked_list(linked_list)
            print()
        elif choice == "3":
            print()
            print_linked_list(linked_list)
            print()
        elif choice == "4":
            print("\nThank you for using our service")
            break
        else :
            print("\033[1;31;1m\nInvalid Input, please try again...\033[1;37;1m")

if __name__ == '__main__':
    tests()
    main()
 
 