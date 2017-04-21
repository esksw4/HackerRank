# BFS: Shortest Reach in a Graph


import bisect

class Graph:
    def __init__(self, num):
        self.graph = {}
        for k in range(num):
            self.graph[k] = []
    
    def connect(self,fromHere, toHere):
        #self.graph[fromHere].append(3)
        #self.graph[fromHere].append(1)
        bisect.insort(self.graph[fromHere], toHere)

    def markVisited(self, temp):
        for i in temp:
            self.visited[i] += 6
    
    def find_all_distances(self, start):
        queue = []
        # start gets 0.
        self.visited = [0 for i in range(len(self.graph))]
        # since adjacent node from start is visited
        queue.extend(self.graph[start])
        # mark those nodes as visited by adding 6 (for each move)
        self.markVisited(self.graph[start])
        
        # print('visited: ', visited)
        
        while (len(queue) != 0):
            # if first element of queue does not have UNVISITED adjacent nodes, 
            if self.visited[queue[0]] != 0 and self.graph[queue[0]] == []:
                # then pop that element and move to other element.
                queue.pop(0)

            # if first element of queue have UNVISITED adjacent nodes,
            else:
                # add to the queue & mark those nodes as visited
                queue.extend(self.graph[queue[0]])
                markVisited(self.graph[queue[0]])
        for i in range(len(self.visited)):
            if self.visited[i] == 0 and i != start:
                print(-1, end=' ')
            elif i != start:
                print(self.visited[i], end=' ')
            

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
    print('\n',end='')

