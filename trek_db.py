# This is a script that implements psycopg2 to connect a
# 'remote' PostgreSQL server to local Python
# The cursor can execute commands from SELECT to INSERT to COMMIT, etc.
#
# There is a lot of potential to automate DB processes from already existing data
# e.g. the JSON script dataset, or even just already written code for the script project

import psycopg2 as pc

conn = pc.connect('host=192.168.0.140 user=pi password=raspberry dbname=test')

cur = conn.cursor()

#cur.execute('select * from characters')

#results = cur.fetchall()

#for result in results:
#   print(result)

#######################################
# Here I use a list to iterate over for populating the name column of the DB
# names = ['Geordi La Forge', 'Tasha Yar', 'Worf Son of Mogh', 'Beverly Crusher', 'Katherine Pulaski', 'Deanna Troi', 'Data Soong', 'Wesley Crusher']

#for i in names:
#    cur.execute('INSERT INTO characters (name) VALUES ('+'\''+str(i)+'\''+')')

#cur.execute('COMMIT;')

#######################################
names = ['Jean-Luc Picard', 'William Riker', 'Geordi La Forge', 'Tasha Yar', 'Worf Son of Mogh', 'Beverly Crusher', 'Katherine Pulaski', 'Deanna Troi', 'Data Soong', 'Wesley Crusher']
ranks = ['Captain', 'First Officer', 'Chief Engineer', 'Chief of Security and Tactical Officer', 'Chief of Security and Tactical Officer', 'Chief Medical Officer', 'Chief Medical Officer', 'Commander and Ship Counselor', 'Lieutenant Commander', 'Ensign']
acts = ['Patrick Stewart', 'Jonathan Frakes', 'LeVar Burton', 'Denise Crosby', 'Michael Dorn', 'Gates McFadden', 'Diana Muldaur', 'Marina Sirtis', 'Brent Spiner', 'Wil Wheaton']

n = 0

for i in names:
    cur.execute('INSERT INTO characters (name, rank, actor) VALUES (' + '\'' + i + '\'' + ', ' + '\'' + ranks[n] + '\'' + ', ' + '\'' + acts[n] + '\'' + ')')
    n += 1
    
cur.execute('COMMIT;')
