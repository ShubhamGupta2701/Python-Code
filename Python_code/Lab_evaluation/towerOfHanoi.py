def TowerOfHanoi(n , source, dest, helping):
    if n == 0:
        return
    TowerOfHanoi(n-1, source, helping, dest)
    print("Move disk",n,"from ->",source,"to ->",dest)
    TowerOfHanoi(n-1, helping, dest, source)
         
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')