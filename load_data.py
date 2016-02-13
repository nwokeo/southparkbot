from glob import glob
import psycopg2
import configparser
import sys

config = configparser.RawConfigParser()
config.read('sp.cfg')

conn = psycopg2.connect(host=config.get('Database', 'host'),
                        user=config.get('Database', 'username'),
                        password=config.get('Database', 'password'),
                        dbname="reader")
conn.set_session(autocommit=True)
cur = conn.cursor()

create_table = '''
drop table if exists southpark;
create table southpark
(
Season varchar(255),
Episode varchar(255),
Character varchar(255),
Line text
)
'''

cur.execute(create_table)
print(cur.statusmessage)

#for file in glob('/home/ch1r0n/PycharmProjects/southpark/SouthParkData/*.csv'):
#print(file)
with open('/home/ch1r0n/PycharmProjects/southpark/SouthParkData/All-seasons.csv') as outfile:
    #cur.copy_from(outfile, 'southpark', sep=',')
    cur.copy_expert("COPY southpark FROM STDIN WITH CSV HEADER", outfile)
    print(cur.statusmessage)
