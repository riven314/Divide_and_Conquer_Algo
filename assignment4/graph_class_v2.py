class vertex():
    def __init__(self,key):
        self.id = key
        self.connect = {}
    def addNode(node_key,weight):
        self.connect[node_key] = weight
    def getConnectNode(self):
        self.connect.keys()
    def __iter__(self):
        return iter(self.connect.keys())

class graph():
    def __init__(self):
        self.nodeList = {}
    def addvertex(self,node):
        self.nodeList[node.id] = node.connect
    def getvertex(self,key):
        new_vertex = vertex(key)
        new_vertex.connect = self.nodeList[key]
        return new_vertex
    def __iter__(self):
        return iter(self.nodeList.keys())
