graph={
  'P':['Q','R','S'],
  'Q':['P','R'],
  'R':['P','Q','T'],
  'T':['R'],
  'S':['P'],
       }

visited=[]
queue=[]
  
def bfs(visited,graph,node):
       visited.append(node)
       queue.append(node)
   
while queue:
 m=queue.pop(0)
 print(m,end=" ")
 for neighbour in graph[m]:
   if neighbour not in visited:
     queue.append(neighbour)
   
   printf("following is the breadth first search")
   bfs(visited,graph,node)