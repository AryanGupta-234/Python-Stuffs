import os
import shutil

class file_system :
    
    global extentions_images
    extentions_images=['png','jpg','svg','jpeg','ico','psd','webp','heic']
    
    def __init__(self,directory,destination=None,):
        if destination==None:
            self.destination=directory
        else:                
            self.destination=destination
        self.directory=directory
        
    def Image_Mapper(self):
        for root, dirs, files in os.walk(self.directory):
            for filename in files:     
                if filename.endswith(extentions_images[0]) or filename.endswith(extentions_images[1]) or filename.endswith(extentions_images[2]) or filename.endswith(extentions_images[3]) or filename.endswith(extentions_images[4]) or filename.endswith(extentions_images[5]) or filename.endswith(extentions_images[6]) or (filename.lower()).endswith(extentions_images[7]):
                    if os.path.exists(os.path.join(self.destination,"Images")):
                        pass
                    else:
                        os.mkdir(os.path.join(self.destination,"Images"))
                    print(os.path.join(root, filename),' Image detected')   
                    try:
                        shutil.move(os.path.join(root, filename),os.path.join(self.destination,"Images"))
                    except shutil.Error:
                        print("File with same name already exists - ",os.path.join(root, filename))
                        pass
                    except Exception as e:
                        print(e)                        
                else:
                    print(os.path.join(root, filename),' Image not detected')                          
      
    def office_Mapper(self):
        for root, dirs, files in os.walk(self.directory):
            for filename in files:     
                if filename.endswith("pptx") or filename.endswith("doc") or filename.endswith("xls") or filename.endswith("ppt") or filename.endswith("xlsx") or filename.endswith("docx"):
                    if os.path.exists(os.path.join(self.destination,"office 365 files")):
                        pass
                    else:
                        os.mkdir(os.path.join(self.destination,"office 365 files"))
                    print(os.path.join(root, filename),' office 365 file detected')   
                    try:
                        shutil.move(os.path.join(root, filename),os.path.join(self.destination,"office 365 file"))
                    except shutil.Error:
                        print("File with same name already exists - ",os.path.join(root, filename))
                        pass
                    except Exception as e:
                        print(e)                        
                else:
                    print(os.path.join(root, filename),' office 365 file not detected')                          
      
    def Document_Mapper(self):
        for root, dirs, files in os.walk(self.directory):
            for filename in files:     
                if filename.endswith("pdf") or filename.endswith("txt") or filename.endswith("csv") or filename.endswith("xml") or filename.endswith("rtf"):
                    if os.path.exists(os.path.join(self.destination,"Document")):
                        pass
                    else:
                        os.mkdir(os.path.join(self.destination,"Document"))
                    print(os.path.join(root, filename),' Document detected')   
                    try:
                        shutil.move(os.path.join(root, filename),os.path.join(self.destination,"Document"))
                    except shutil.Error:
                        print("File with same name already exists - ",os.path.join(root, filename))
                        pass
                    except Exception as e:
                        print(e)                        
                else:
                    print(os.path.join(root, filename),' Document not detected')                    
    
    
    def python_Mapper(self):
        for root, dirs, files in os.walk(self.directory):
            for filename in files:     
                if filename.endswith("py") or filename.endswith("pyw") :
                    if os.path.exists(os.path.join(self.destination,"Python")):
                        pass
                    else:
                        os.mkdir(os.path.join(self.destination,"Python"))
                    print(os.path.join(root, filename),' Python file detected')   
                    try:
                        shutil.move(os.path.join(root, filename),os.path.join(self.destination,"Python"))
                    except shutil.Error:
                        print("File with same name already exists - ",os.path.join(root, filename))
                        pass
                    except Exception as e:
                        print(e)                        
                else:
                    print(os.path.join(root, filename),' Python not detected')                    
    
    
    
    
    def map_all(self):
        self.Image_Mapper()
        self.Document_Mapper()
        self.office_Mapper()
        self.python_Mapper()
        
while True:                           
    ob1=file_system(input("Enter the directory : "))                    
    ob1.map_all()