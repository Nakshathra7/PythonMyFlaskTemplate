import pymysql
import re
from baseObject import baseObject

class customerList(baseObject):
	def __init__(self):
		self.setupObject('customers')

	def tryLogin(self,email,password):
		sql = 'SELECT * FROM `' + self.tn +'` WHERE `email` = %s AND `password` = %s;'
		tokens = (email,password)
		self.connect()
		cur = self.conn.cursor(pymysql.cursors.DictCursor)
		cur.execute(sql,tokens)
		self.data = []
		n = 0
		for row in cur:
			self.data.append(row)
			n+=1
		if n>0:
			return True
		else:
			return False

	def verifyNew(self,n=0):
		self.errList = []

		if len(self.data[n]['fname']) == 0:
			self.errList.append("First name cannot be blank")

		if len(self.data[n]['lname']) == 0:
			self.errList.append("Last name cannot be blank")

		if len(self.data[n]['email']) == 0:
			self.errList.append("Email cannot be blank")

		elif not(bool(re.search(self.regex,self.data[n]['email']))):
			self.errList.append("Enter Valid Email with . and @")

		if len(self.data[n]['password']) == 0:
			self.errList.append("Password cannot be blank")

		elif len(self.data[n]['password']) <= 4:
			self.errList.append("Password must be longer than 4 characters")

		if len(str(self.data[n]['subscribed'])) == 0:
			self.errList.append("Subscribed cannot be blank")

		elif type(self.data[n]['subscribed']) != bool:
			self.errList.append("Subscribed value must be 'True' or 'False'")

		if len(self.errList) > 0:
			return False
		else:
			return True	

		#Add if statements for validation of other fields
		#Add Unit Test

	






