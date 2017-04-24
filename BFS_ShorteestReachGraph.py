

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
        if toHere not in self.graph[fromHere]:
            bisect.insort(self.graph[fromHere], toHere)

    def markVisited(self, temp):
        for i in temp:
            self.visited[i] += 6
    
    def find_all_distances(self, start):
        queue = []
        # start gets 0.
        self.visited = [0] * len(self.graph)
        # print(self.visited)
        # since adjacent node from start is visited
        queue.extend(self.graph[start])
        # mark those nodes as visited by adding 6 (for each move)
        self.markVisited(self.graph[start])
        
        # print('visited: ', visited)
        
        while queue:
            # if first element of queue does not have UNVISITED adjacent nodes, 
            if self.visited[queue[0]] != 0 and self.graph[queue[0]] == []:
                # then pop that element and move to other element.
                queue.pop(0)

            # if first element osf queue have UNVISITED adjacent nodes,
            else:
                # add to the queue & mark those nodes as visited
                queue.extend(self.graph[queue[0]])
                markVisited(self.graph[queue[0]])
        for m in range(len(self.visited)):
            if self.visited[m] == 0 and m != start:
                print(-1, end=' ')
            elif m != start:
                print(self.visited[m], end=' ')
            

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for _ in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
    print('\n',end='')





# class Graph(object):
#     def __init__(self, _n):
#         self.n = _n
#         self._graph = {}
#         for _i in range(_n):
#             self._graph[_i] = [[], -1]

#     def connect(self, x, y):
#         if x == y: return
#         self._graph[x][0].append(y)
#         self._graph[y][0].append(x)

#     def find_all_distances(self, start):
#         visited = [start]
#         _level = 1
#         _next_to_visit = set(self._graph[start][0])
#         while _next_to_visit:
#             for _each_id in _next_to_visit:
#                 self._graph[_each_id][1] = 6 * _level
#             visited.extend(_next_to_visit)
#             _next_to_visit = set(
#                 [_next_ids for _id in _next_to_visit for _next_ids in self._graph[_id][0] if _next_ids not in visited])
#             _level += 1
#         print(" ".join([str(key[1]) for _item,key in self._graph.items() if _item != start]))
