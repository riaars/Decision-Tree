from python import dtree as d
from python import monkdata as m


print("Error rate MONK 1")
t= d.buildTree(m.monk1, m.attributes)
print(1-d.check(t,m.monk1test))

print("Error rate MONK 2")
t= d.buildTree(m.monk2, m.attributes)
print(1-d.check(t,m.monk2test))

print("Error rate MONK 3")
t= d.buildTree(m.monk3, m.attributes)
print(1-d.check(t,m.monk3test))