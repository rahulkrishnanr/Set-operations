E={'0','2','4','6','8'}
N={'1','2','3','4','5'}
z=E.union(N)
print("union of E and N is",z)
y=E.intersection(N)
print("intersection of E and N is",y)
x=E.difference(N)
print("difference of E and N is",x)
w=E.symmetric_difference(N)
print("symmetric difference of E and N is",w)