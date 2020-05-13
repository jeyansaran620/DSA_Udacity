# -*- coding: utf-8 -*-

import sys
import operator

class Node:
    def __init__(self,char,freq):
        self.character=char
        self.frequeny=freq
        self.left=None
        self.right=None


class Huffman_Tree:
    
    def __init__(self,head=None):
        self.head=head
        
    def path_from_root_to_node(self,data):
        
        output = self.path_from_node_to_root(self.head,data)
        return output[::-1]
    
    def path_from_node_to_root(self,node,data):
        
        if node is None:
            return None

        elif node.character == data:
            return ''

        left_answer = self.path_from_node_to_root(node.left, data)
        if left_answer is not None:
            left_answer+='0'
            return left_answer

        right_answer = self.path_from_node_to_root(node.right, data)
        if right_answer is not None:
            right_answer+='1'
            return right_answer
        return None
     
def huffman_encoding(data):
    values={}
    nodes=[]
    tree=Huffman_Tree()
    
    if len(data)==0:
        return '',tree
    
    elif len(data)==1:
        tree.head=Node(data,1)
        return "0",tree
    
    for x in data:
        if values.get(x):
            values[x]+=1
        else:
            values[x]=1
            
    old_values=values.copy()  
    
    sorted_values=sorted(values.items(), key=operator.itemgetter(1))        
    while len(sorted_values)>1 :
        first=sorted_values[0]
        second=sorted_values[1]
        values.pop(first[0],None) 
        values.pop(second[0],None)
        
        node=Node(None,first[1]+second[1])
            
        if len(str(first[0]))!=1:
            for x in nodes:
                if id(x)==first[0]:
                    node1=x
        else:
            node1=Node(first[0],first[1])
           
            
        if len(str(second[0]))!=1:
            for x in nodes:
                if id(x)==second[0]:
                    node2=x
        else:
            node2=Node(second[0],second[1])
            
            
        if first[1] > second[1]:
            node.right=node1
            node.left=node2
        else:
            node.left=node1
            node.right=node2
            
        if tree.head==None:
            tree.head=node
            
        else:
            if node1==tree.head or node2==tree.head:
                tree.head=node
                
        values[id(node)]=first[1]+second[1]
        
        nodes.append(node)
        
        sorted_values=sorted(values.items(), key=operator.itemgetter(1)) 
        
        del first
        del second
    for x in old_values:   
       old_values[x]=tree.path_from_root_to_node(x)
       
    encoded_data=''
    for x in data:
        encoded_data+=old_values[x]
    del nodes         
    return encoded_data,tree
    
    pass

def huffman_decoding(data,tree):
    decoded_data=''
    current=tree.head
    
    if len(data)==1:
        return ''
        
    elif len(data)==1:
        return tree.head.character
    
    for x in data:
        if x=='0':
            current=current.left
        elif x=='1':
            current=current.right
            
        if current.left==None and current.right==None:
                decoded_data+=current.character
                current=tree.head
    return decoded_data    
    pass

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    #test case with only one character
    a_great_sentence = "T"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    
    #test case with no character
    a_great_sentence = ""

    encoded_data, tree = huffman_encoding(a_great_sentence)
    
    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))