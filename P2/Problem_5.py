
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()    

    def insert(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True

    def find(self, word):
        
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node
 

    def suffix(self, node, word, wordlist): 
          
        # Method to recursively traverse the trie 
        # and return a whole word.  
        if node.is_word: 
            wordlist.append(word) 
  
        for a,n in node.children.items(): 
            wordlist=self.suffix(n, word + a,wordlist) 
        return wordlist
    
  
        ## Recursive function that collects the suffix for 
        ## all complete words below this point


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)
    


from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(MyTrie.suffix(prefixNode,'',[])))
        else:
            print(prefix + " not found")
    else:
        print('')
        
        
interact(f,prefix=''); #prints None
interact(f,prefix='a'); #prints suffix starting with a 
interact(f,prefix='fu'); #prints suffix starting with fu 
interact(f,prefix='trie'); #prints None





