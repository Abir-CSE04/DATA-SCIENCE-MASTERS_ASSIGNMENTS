import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
mycursor = mydb.cursor()
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mycursor.execute("insert into test2.test_test values(123, 'abir', 244.4, 466, 'mallick' )")
mydb.commit()
mydb.close()