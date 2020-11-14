# Advanced Data Structure and Algorithm
# Parctical work number 5 
# Exercice 2 



#Graph 2 : Negative weight so we use the 
#Bellman-Ford algorithm

#Graph 1 : 
#Number of edges : 13
#Number of nodes : 8
#Complexity of the dijkstra algorithm : 64
#Complexity of the Bellman-Ford algorithm : 104
#Complexity of the Floyd-Warshall algorithm : 512
#We will use Dijkstra algorithm

#Graph 3 : 
#Number of edges : 13
#Number of nodes : 7
#Complexity of the dijkstra algorithm : 49
#Complexity of the Bellman-Ford algorithm : 91
#Complexity of the Floyd-Warshall algorithm : 343
#We will use Dijkstra algorithm

from queue import Queue
class vertex :
    def __init__(self,name,adjacent):
            self.name=name
            self.adjacent = adjacent
            self.d=None
            self.parent=None
    def __str__(self):
        res = str(self.name)+"-->"
        if (self.adjacent==None):
            res=res+" "+str(None)
        else:
            for elt in self.adjacent.keys():
                res=res+" "+elt.name
        return res
    def setd(self,k):
        self.d=k
        
def showQ(Q):
    for q_item in Q.queue:
        print (q_item)
def showS(S):
    for (obtained,init) in S.items():
        print(obtained+" is obtained by "+init)
        
def showPath(path):
    res=""
    for vert in path:
        res=res+"-->"+vert
    print(res)
    
def min_d(Q):
    min_v=None
    min_d=99999
    for vert_n in Q.queue:
        if min_d>vert_n.d:
            min_v=vert_n
            min_d=vert_n.d
    return(min_v)
    
def modifyQ(Q,vert):
    print("Q is modyfied :")
    temp=Queue()
    for q_vertex in Q.queue:
        if (q_vertex!=vert):
            temp.put(q_vertex)
    return temp
 
def findPath(S,start,end):
    Res=[end.name]
    current=end.name
    while current!=start.name:
        Res=Res+[S[current]]
        current=S[current]
    Res.reverse()
    return Res
        
def dijkstra(start,end,graph):
    Q=Queue()
    for vert in graph:
        vert.setd(99999)
    start.setd(0)
    for vert in graph:
        Q.put(vert)
    print("Queue initialization as follow :")
    showQ(Q)
    S={}  #dictionnary {vertex obtaines by : ..., }
    
    #while Q.empty()==False:
    for q_vertex in Q.queue:
        min_d_vertex=min_d(Q)
        print("\nWe work on the vertex :")
        print(min_d_vertex)
        if (q_vertex!=end):
            for v,length in min_d_vertex.adjacent.items(): #(vertex,length)
                if (length+min_d_vertex.d<v.d):
                    S[v.name]=min_d_vertex.name
                v.d=min(length+min_d_vertex.d,v.d)
        Q=modifyQ(Q,min_d_vertex)
        showQ(Q)
    print("\nSmallest weight :"+str(end.d))
    print("\nAll the movements :")
    showS(S)
    print("\nThe shortest path is :")
    print(findPath(S,start,end))
        

vert_H=vertex('H',None)
vert_G=vertex('G',{vert_H:2})
vert_E=vertex('E',{vert_H:4})
vert_D=vertex('D',{vert_G:2, vert_E:4})
vert_F=vertex('F',{vert_H:7,vert_G:4,vert_D:1})
vert_C=vertex('C',{vert_D:3})
vert_B=vertex('B',{vert_F:4,vert_C:2})
vert_A=vertex('A',{vert_B:2,vert_C:5})



graph=[vert_A,vert_B,vert_C,vert_D,vert_E,vert_F,vert_G,vert_H]
dijkstra(vert_A,vert_H,graph)



















  