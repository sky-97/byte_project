import csv
import sqlite3
#
conn = sqlite3.connect('skill.db')
c = conn.cursor()
c.execute("""create table fullstacktable (name TEXT, id REAL)""")
def database():
    with open('full_stack - Sheet1.csv','r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for line in csv_reader:
            c.execute("INSERT into fullstacktable values (?,?)",(str(line[0]),float(line[1])))
    return

# database()
conn.commit()
conn.close()
