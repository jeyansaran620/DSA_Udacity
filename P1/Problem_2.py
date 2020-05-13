# -*- coding: utf-8 -*-
import os

def find_files(suffix, path):
    
    if suffix == '':
        return "No Suffix included"
    # Base condition
    
    elements = os.listdir(path)
    if len(elements) == 0:
        return [] #No files in Path
    
    
    files = [] #list for files with suffix
    folders = [] #list for folders
  
    for element in elements:
       if ('.' + suffix) in element:
           files.append(path+'\\'+element)
           
       elif '.' not in element:
            folders.append(element)
        
    for folder in folders:
        files.extend(find_files(suffix,path + '\\' + folder))
    return files
# Tests
    
for x in find_files('c',os.getcwd() + '\\testdir'):
     print(x) 
# prints a list of all files with .c extension from the testdir folder
  
for x in find_files('h',os.getcwd() + '\\testdir'):
     print(x) 
# prints a list of all files with .h extension from the testdir folder
     
if len(find_files('c',os.getcwd() + '\\testdir\\subdir4'))==0:
     print("None") 
# prints None as there is no .c file in the folder

     
for x in find_files('c',os.getcwd() + '\\testdir\\subdir2\\subdir\\subsubdir1'):
     print(x) 
# prints a list of all files with .c extension from the \\testdir\\subdir2\\subdir\\subsubdir1 folder





