import os
import shutil
from termcolor import colored
import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics import pairwise_distances

class file_system :

    file_name=[]
    file_data=[]
    
    def __init__(self,directory):
        self.directory=directory
        if os.path.exists(self.directory):
            print(colored("Location set to ","magenta"),colored(loc,"red"))
            self.search_data()
        else:
            print(colored("Wrong directory detected","red"))
            return
        
    def file_reader(self):
        for root, dirs, files in os.walk(self.directory) :
            for filename in files:     
                if filename.endswith('.py') or filename.endswith('.pyw') or filename.endswith('.PY'):
                    self.file_name.append(os.path.join(root, filename))
                    path=os.path.join(root, filename)
                    data=open(path,encoding='latin')
                    data=data.read()
                    i=data.replace("  ","")
                    self.file_data.append(i)
                         
        # print(self.file_name)                
    def search_data(self):
        c=0
        data=input(colored("Enter the content to be searched :-: ",'green'))
        self.file_reader()
        print(colored("----------------------------------Search Results----------------------------------","magenta"))
        for i in self.file_data:
            if data in i:
                c=c+1
            #  print(self.file_data.index(i))
                print(colored("Location -",'blue'),colored(self.file_name[self.file_data.index(i)],"light_cyan"))
                print(colored("  Filename -",'red'),colored(os.path.split(self.file_name[self.file_data.index(i)])[1] ,'light_blue'))
        print("\n",colored("Total files found :","magenta"),colored(c,"red"))    
        if c>=15:
            print(colored("Warning :","red"),colored("Multiple files detected your search may be inaccurate, try providing more unique string","green"))            
        if c==0:
            print(colored("No files found with the given data","green"))
     
        
loc=input(colored("Enter the location where search is to be performed :-: ",'green'))
ob1=file_system(loc)                    




# import nltk

# nltk.download()