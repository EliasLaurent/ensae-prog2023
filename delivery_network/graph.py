class Graph:
    """
    A class representing graphs as adjacency lists and implementing various algorithms on the graphs. Graphs in the class are not oriented. 
    Attributes: 
    -----------
    nodes: NodeType
        A list of nodes. Nodes can be of any immutable type, e.g., integer, float, or string.
        We will usually use a list of integers 1, ..., n.
    graph: dict
        A dictionnary that contains the adjacency list of each node in the form
        graph[node] = [(neighbor1, p1, d1), (neighbor2, p2, d2), ...]
        where p1 is the minimal power on the edge (node, neighbor1) and d1 is the distance on the edge
    nb_nodes: int
        The number of nodes.
    nb_edges: int
        The number of edges. 
    """

    def __init__(self, nodes=[]):
        """
        Initializes the graph with a set of nodes, and no edges. 
        Parameters: 
        -----------
        nodes: list, optional
            A list of nodes. Default is empty.
        """
        self.nodes = nodes
        self.graph = dict([(n, []) for n in nodes])
        self.nb_nodes = len(nodes)
        self.nb_edges = 0
    

    def __str__(self):
        """Prints the graph as a list of neighbors for each node (one per line)"""
        if not self.graph:
            output = "The graph is empty"            
        else:
            output = f"The graph has {self.nb_nodes} nodes and {self.nb_edges} edges.\n"
            for source, destination in self.graph.items():
                output += f"{source}-->{destination}\n"
        return output
    
    def add_edge(self, node1, node2, power_min, dist=1):
        """
        Adds an edge to the graph. Graphs are not oriented, hence an edge is added to the adjacency list of both end nodes. 

        Parameters: 
        -----------
        node1: NodeType
            First end (node) of the edge
        node2: NodeType
            Second end (node) of the edge
        power_min: numeric (int or float)
            Minimum power on this edge
        dist: numeric (int or float), optional
            Distance between node1 and node2 on the edge. Default is 1.
        """
        if node1 not in self.graph:
            self.graph[node1] = []
            self.nb_nodes += 1
            self.nodes.append(node1)
        if node2 not in self.graph:
            self.graph[node2] = []
            self.nb_nodes += 1
            self.nodes.append(node2)

        self.graph[node1].append((node2, power_min, dist))
        self.graph[node2].append((node1, power_min, dist))
        self.nb_edges += 1
    

    def get_path_with_power(self, src, dest, power):
        raise NotImplementedError
    

    """def comp(self,l,lb,lv):
        if lv==[]:
            return(l,lb)
        else:   
            i=lv.pop()
            if lb[i-1]:
                lb[i-1]=False
                b=[a for (a,a2,a3) in self.graph[i]]
                l.append(i)
                lv+=b
            return(self.comp(l,lb,lv))
            
    def compco(self):
        n=self.nb_nodes
        lb=[True for i in range(n)]
        c=[]
        for k in range(1,n+1):
            l1,l2=self.comp([],lb,[k])
            lb=l2
            if l1!=[]:
                c.append(l1)
        return(c)???"""
    
    def min_power(self, src, dest):
        """
        Should return path, min_power. 
        """
        raise NotImplementedError


    def CCsommet(self,i):
        n=len(self.nodes)
        L=[]
        compconn=[0 for  _ in range(n)]
        compconn[i-1]=1
        L+=self.graph[i]
        while L!=[]:
            voisin = L.pop(0)
            if compconn[voisin[0]-1]==0 :
                compconn[voisin[0]-1]=1
                L+=self.graph[voisin[0]] #ajout dans L des voisins de voisin
        return(compconn)
    def CConnexes(self):
        L=[]
        for i in self.nodes:
            L.append(self.CCsommet(i))
        Lsansdouble = [] 
        for i in L : 
            if i not in Lsansdouble: 
                Lsansdouble.append(i) 
        return(Lsansdouble)
#3
    def get_path_with_power(self,p,t):
        i,j=t[0],t[1]
        n=self.nb_nodes()
        visit=[0 for _ in range(n)]
        cc=self.compco()
        for c in cc:
            if c.count(i)==1:
                if c.count(j)==0:
                    return None
def graph_from_file(filename):
    with open(filename, "r") as file:
        n, m = map(int, file.readline().split())
        g = Graph(range(1, n+1))
        for _ in range(m):
            edge = list(map(int, file.readline().split()))
            if len(edge) == 3:
                node1, node2, power_min = edge
                g.add_edge(node1, node2, power_min) # will add dist=1 by default
            elif len(edge) == 4:
                node1, node2, power_min, dist = edge
                g.add_edge(node1, node2, power_min, dist)
            else:
                raise Exception("Format incorrect")
    return g

        
        


#TD2
