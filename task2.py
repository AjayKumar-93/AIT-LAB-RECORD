graph={
    ('A','B'):2,
    ('B','C'):3,
    ('C','D'):1,
    ('D','A'):4
    }
print("Edge costs:")
for edge,cost in graph.items():
    print(f"{edge[0]}->{edge[1]}:{cost}")
    path=['A','B','C','D']
    totalcost=0
    for i in range(len(path)-1):
        edge=(path[i],path[i+1])
        totalcost+=graph.get(edge,0)
print(f"\n total cost of path {'->'.join(path)}:{totalcost}")
path=['A','B','C','D','A']
totalcost=0
for i in range(len(path)-1):
    edge=(path[i],path[i+1])
    totalcost+=graph.get(edge,0)
print(f"\n total cost of path {'->'.join(path)}:{totalcost}")
