from customer import customerList
import time

cl = customerList()
cl.set('fname','Anusuya')
cl.set('lname','Manoharan')
cl.set('email','saran@clarkson.edu')
cl.set('password','abc123')
cl.set('subscribed',True)	
cl.add()
print("Before Insert",cl.data)
#A - show the mysql table

#cl.insert()
#print("After insert",cl.data)
#B - show cl.data

cl.data[0]['lname'] = 'rdtrdrd'
cl.insert()
cl.data[0]["id"] = 7
print(cl.data)
cl.update()
print("after update",cl.data)
#C - show the mysql table and cl.data