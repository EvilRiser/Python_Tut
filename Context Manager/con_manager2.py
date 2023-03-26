class File:
    def __init__(self,filename,method):
        self.file = open(filename,method)
    
    def __enter__(self):
        '''
        with something as f--> here something calls enter method
        
        '''
        return self.file
    
    def __exit__(self, type, value, traceback):
        '''
        In case we get error value and traceback will be used
        '''
        self.file.close()
        print("Exit")
        print(f"{type},{value},{traceback}")
        if type == Exception:
            return True # --> exception message will not be shared

with File("file.txt","w") as f:
    print("Middle")
    f.write("hello!")
    # raise Exception()
    raise FileExistsError()