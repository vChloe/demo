import psycopg2

conn = psycopg2.connect(host="localhost", database="hw04", user="dbo", password="123456")


cur = conn.cursor()
cur.execute( '''

        SELECT hw_a, hw_b
        FROM hw_a 
        RIGHT JOIN hw_b 
        ON hw_a.sn=hw_b.sn
        WHERE hw_a.sn is null
	;
	''')
for row in cur:
	print( '%s, %s' % (row[0], row[1]))

conn.commit()

