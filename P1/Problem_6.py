# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size
    
    def is_present(self,data):
        if self.head is None:
            return False
        current = self.head
        while current:
            if current.value==data:
                return True
            current=current.next
        return False
            

def union(list_1, list_2):
    union_list = LinkedList()
    
    node = list_1.head
    #traverse all nodes in list_1 and append values not already in union set.
    while node:
        union_list.append(node.value)
        node = node.next
        
    node = list_2.head
    #traverse all nodes in list_2 and append values not already in union set.
    while node:
        if union_list.is_present(node.value)==False:   
            union_list.append(node.value)
        node = node.next
        
    return union_list
    pass

def intersection(list_1, list_2):
    # Your Solution Here
    intersection_list = LinkedList()
    node = list_1.head
    
    #traverse all nodes in list_1 and append values that are in list_2 set.
    while node:
        if list_2.is_present(node.value)==True:
            intersection_list.append(node)
        node = node.next
    
    return intersection_list
    pass


print("Test case 1")

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    if linked_list_1.is_present(i)==False:  #as duplicates are not allowed in sets
            linked_list_1.append(i)

for i in element_2:
    if linked_list_2.is_present(i)==False:  #as duplicates are not allowed in sets
            linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) #prints all the values in both the lists without duplicates
print (intersection(linked_list_1,linked_list_2)) #prints 4 , 6 , 21 as their intersection

print("Test case 2")

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    if linked_list_3.is_present(i)==False:  #as duplicates are not allowed in sets
            linked_list_3.append(i)

for i in element_2:
    if linked_list_4.is_present(i)==False:  #as duplicates are not allowed in sets
            linked_list_4.append(i)


print (union(linked_list_3,linked_list_4)) #prints all the values in both the lists without duplicates

print (intersection(linked_list_3,linked_list_4)) #prints nothing as there is no intersection in the values

print("Test case 3")
#this test case will have same union and intersection

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,7,8,9,11,21,1]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    if linked_list_5.is_present(i)==False:  #as duplicates are not allowed in sets
            linked_list_5.append(i)

for i in element_2:
    if linked_list_6.is_present(i)==False:  #as duplicates are not allowed in sets
            linked_list_6.append(i)


print (union(linked_list_5,linked_list_6)) #prints all the values in a list as both the list are same

print (intersection(linked_list_5,linked_list_6)) #prints all the values in a list as both the list are same
