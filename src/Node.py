class Node:
    def __init__(self,key:int,pos:tuple) -> None:
        self.key = key
        self.pos = pos
        self.fromMe = {}
        self.toMe = {}
