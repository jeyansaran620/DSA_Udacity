# -*- coding: utf-8 -*-

import hashlib
from datetime import datetime  

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next=None
    
    
    def calc_hash(self):
          sha = hashlib.sha256()

          hash_str = str(self.data).encode('utf-8')

          sha.update(hash_str)

          return sha.hexdigest()
    
      
    def get_utc_time(self):
         return self.timestamp
         
        

class Block_chain:
    
    def __init__(self):
        self.head=None
        self.tail=None
        
    def add_block(self,data):
        
        if self.head is None:
            self.head = Block(datetime.utcnow(), data, None)
            self.tail=self.head
            return
        block = Block(datetime.utcnow(), data, self.tail.hash)
        self.tail.next = block
        self.tail = block
        
    def print_Block_chain(self):
        if self.head is None:
            print("No elements in Block Chain")
        current = self.head
        while current!=None:
            print("Data: "+str(current.data)+"\n"+"Previous hash: "+str(current.previous_hash)+"\n"+"Current hash: "+str(current.hash)+"\n")
            current=current.next


block_chain=Block_chain()

block_chain.print_Block_chain() #prints no elements in block chain

block_chain.add_block("hi")
block_chain.add_block("how")
block_chain.add_block("are")
block_chain.add_block("you")

block_chain.print_Block_chain() #prints the elements in the block chain


block_chain.add_block("are")
block_chain.add_block("you")
block_chain.add_block("ok")


block_chain.print_Block_chain() #prints the elements in the block chain