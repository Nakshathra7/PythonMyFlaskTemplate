from customer import customerList
import time

c1 = customerList()
c1.getByID(2)
print(c1.data)

'''
c1 = customerList()
c1.getAll()
#print(c1.data)


c1 = customerList()
c1.getAll('fname')
print(c1.data)

'''
c1.data[0]['id'] = 7
#c1.data[0]['fname'] = 'Anu'
#c1.data[0]['mname'] = 'rose'
c1.update()
print(c1.data)
