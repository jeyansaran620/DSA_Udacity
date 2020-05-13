# -*- coding: utf-8 -*-

class RouteTrieNode:
        # Initialize the node with children as before, plus a handler
    def __init__(self):
        self.handler = None
        self.children = {}
     
        
class Router:
    def __init__(self,root_handler,error_handler):
        
        self.root=RouteTrieNode()
        
        self.root_handler=root_handler
        
        self.error_handler=error_handler



    def add_handler(self,path,handler):
        
        path_nodes=path.split('/')
        current_node = self.root
        for x in path_nodes[1:]:
             if x not in current_node.children:
                current_node.children[x] = RouteTrieNode()
             current_node = current_node.children[x]

        current_node.handler = handler
        

    def lookup(self,path):
        if path=='/':
            return self.root_handler
        
        path_nodes=path.split('/')
        if path_nodes[-1] == '':
            path_nodes=path_nodes[:-1]
        
        current_node=self.root
        
        for x in path_nodes[1:]:
            if x not in current_node.children:
                return self.error_handler
            current_node = current_node.children[x]
            
        return current_node.handler if current_node.handler else self.error_handler
     
        
# create the router and add a route
router = Router("root handler", "not found handler") 
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/games/python/sudoku", "sudoku handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' 
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' 
print(router.lookup("/home/about/me")) # should print 'not found handler' 

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/games/python")) # should print 'about handler'
print(router.lookup("/games/python/sudoku/")) # should print 'not found handler' 