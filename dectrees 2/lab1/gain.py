from python import dtree
from python import monkdata as m


for i in m.attributes:
    print(dtree.averageGain(m.monk1, i))
    print(dtree.averageGain(m.monk2, i))
    print(dtree.averageGain(m.monk3, i))

