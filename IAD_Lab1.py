import math
import random

def min_edge(g, united_vert):
    m_ed = [math.inf, -1, -1]
    for x in g:
            if (x[1] not in united_vert) ^ (x[2] not in united_vert):
                if m_ed[0] > x[0]:
                    m_ed = x

    return m_ed

vertex_q=int(input("Enter vertex quantity: "))
#vertex_q=4
#graph=[[20, 1, 3], [32, 1, 4], [24, 3, 4]]
#array=[[1, 3], [1, 4], [3, 4]]

def is_all(ver, used, unused):
    value=False
    for l in EdgesArr:
        if ver==l[0] and l[1] not in used:
            used[l[1]]=True
            element=l[1]
        elif ver == l[1] and l[0] not in used:
            used[l[0]] = True
            element = l[0]
        else:
            continue
        if len(unused) == 0: return False
        if element in unused: del unused[element]
        if is_all(element, used, unused):
            return True
    if len(unused)!=0 and ver==1:
        w = random.randint(1, 50)
        v1=random.randint(0, len(used)-1)
        v2=random.randint(0, len(unused)-1)
        trip=[w, list(used.keys())[v1], list(unused.keys())[v2]]
        graph.append(trip)
        vertex_only = [list(used.keys())[v1], list(unused.keys())[v2]]
        EdgesArr.append(vertex_only)
        value=True
    return value


graph=[]
EdgesArr=[]
# auto generation

weight=0

for i in range(1, vertex_q + 1):
    for j in range(i + 1, vertex_q + 1):
        is_edge=random.getrandbits(1)
#        is_edge = 1 + random.randint(-1, 1)  # to increase possibility of creating an edge from 50% to 66%
        if is_edge:
            weight = random.randint(1, 50)
            triplet = [weight, i, j]
            vertexes_only = [i, j]
            EdgesArr.append(vertexes_only)
            graph.append(triplet)
print("Graph before:\n", graph)

new=True
while new:
    UsedVer = {1: True}
    UnusedVer = {}
    for k in range(2, vertex_q + 1):
        UnusedVer[k] = False
    new = is_all(1, UsedVer, UnusedVer)
#    fl=is_all(mass)
print("Graph:\n", graph)
#auto generation

united_vertexes={1} # using set to not
# add same vertex twice and do not create check for it
Prim_graph=[]
# if there is n-1 used vertexes we still continue,
# when they all used or edge can't be found then stop
while len(united_vertexes)<vertex_q:
    edge=min_edge(graph, united_vertexes)
    if edge[0]==math.inf: # if min_edge() returns [math.inf, -1, -1] means there are no more vertexes we can add
        break
    Prim_graph.append(edge)
    united_vertexes.add(edge[1])
    united_vertexes.add(edge[2])

print("Answer graph:\n", Prim_graph)