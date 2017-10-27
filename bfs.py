# https://www.hackerrank.com/challenges/bfsshortreach/problem

from collections import deque

class Node:
    def __init__(self,n,d):
        self.distance = d
        self.name = n
        self.children = deque([])
        self.distanceFromOrigin = -1

    def add_child(self,c):
        self.children.append(c)

def bfs(G, s):
    Q = [s]
    V = [s]
    while Q:
        u = int(Q.pop(0))
        for v in G[u].children:
            if G[int(v)].distanceFromOrigin == -1:
                Q.append(v)
                if u == int(s):
                    G[int(v)].distanceFromOrigin = 6
                else:
                    G[int(v)].distanceFromOrigin = G[int(v)].distance + G[int(u)].distanceFromOrigin    
    return G

def test():
    G = []
    
    # test cases
    temp = input().split()

    nodes = int(temp[0])
    
    # create empty nodes
    G.append(Node(0,6))
    for i in range(1,nodes+1):
        G.append(Node(i,6))

    edges = int(temp[1])

    for i in range(0,edges):
        temp = input().split()
        G[int(temp[0])].add_child(temp[1])
        G[int(temp[1])].add_child(temp[0])

    origin = int(input())
    temp = bfs(G,origin)
    
    sentence = ''
    for i in temp:
        if i.name == int(origin) or i.name == 0:
            continue
        else:
            sentence += str(i.distanceFromOrigin) + ' '
    print(sentence.strip())

T = int(input())
for i in range(0,T):
    test()
