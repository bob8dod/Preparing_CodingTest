# 백준 Tree P1991 트리 순회
"""
전위 순회(preorder traversal), 
중위 순회(inorder traversal), 
후위 순회(postorder traversal) 
관한 basic 문제
"""
from collections import defaultdict

def preorder(gmap, curr):
    if curr == '.': return
    left, right = gmap[curr][0], gmap[curr][1]

    print(curr, end="")
    preorder(gmap,left)
    preorder(gmap, right)

def inorder(gmap,curr):
    if curr == '.': return
    left, right = gmap[curr][0], gmap[curr][1]

    inorder(gmap,left)
    print(curr, end="")
    inorder(gmap, right)

def postorder(gmap,curr):
    if curr == '.': return
    left, right = gmap[curr][0], gmap[curr][1]

    postorder(gmap, left)
    postorder(gmap, right)
    print(curr, end="")

def main():
    N = int(input())
    gmap = defaultdict(list)
    for _ in range(N):
        p, l, r = input().split()
        gmap[p].append(l)
        gmap[p].append(r)

    preorder(gmap, 'A')
    print()
    inorder(gmap, 'A')
    print()
    postorder(gmap, 'A')
    print()



if __name__ == "__main__":
    main()
