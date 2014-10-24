import MySQLdb

db = MySQLdb.connect("localhost","root","ezfx0109","TESTDB")
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "INSERT INTO EMPLOYEE(FIRST_NAME,\
         LAST_NAME, AGE, SEX, INCOME)\
         VALUES ('%s', '%s', '%d', '%c', '%d' )" % \
         ('Tom', 'Jackson', 23, 'M', 4000)
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

db.close()