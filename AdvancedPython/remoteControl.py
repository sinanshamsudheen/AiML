class remoteControl:
    def __init__(self):
        self.channels=["HBO","SUN TV","CNN","POGO"]
        self.index=-1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.index+=1

        if self.index==len(self.channels):
            raise StopIteration
        return self.channels[self.index]

r=remoteControl()
itr=iter(r)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr)) #Exception