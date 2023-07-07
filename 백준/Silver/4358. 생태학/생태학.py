import sys 
input = sys.stdin.readline

trees = dict()

while 1:
    data = input().rstrip()
    if not data:
        break
    
    if trees.get(data):
        trees[data] += 1
    else:
        trees[data] = 1
    
sum_trees = sum(trees.values())
tree_key_asc = list(trees.keys())
tree_key_asc.sort()

for key in tree_key_asc:
    print(key, f'{trees[key]/sum_trees*100:.4f}')