import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'salim'
DATABASE = 'ibam'

try:
    connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
    print("conection reussie!!")
except psycopg2.Error as e:
    print("connection refusé veillez verifir les paramettre de connection!!")
    
connection.autocommit = True
cursor = connection.cursor()

sql1 = "SELECT * FROM student;"
cursor.execute(sql1)
#cursor.fetchall()
for data in cursor.fetchall():
    print(data)