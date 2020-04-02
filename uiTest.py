from product import productList
from customer import customerList

p = productList()
c = customerList()

'''
for fn in c.fn1:
	var = input("Enter "+ fn + "\n")
	c.set(fn, var)
c.add()
#if c.verifyNew():
c.insert()
print(c.data)
#else:
print(c.errList)
c.getByField('fname','Anu')
print(c.data)

c.getLikeField('fname','anusuya')
print(c.data) 
'''

#c.getFields()
'''
print(p.fn1)
print(p.pk)

p.set('pid','')
p.set('sku','fgfds')
p.set('name','dfdf')
p.set('price','50.56')
p.add()
p.verifyNew()
p.insert()
print(p.errList)

pl = productList()
pl.getAll()
print(pl.data)
'''

c.tryLogin('ddf','dfdfdf')
print(c.data)