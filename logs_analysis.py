#!/usr/bin/env python2

import psycopg2
def main():
    # Connect to database
    db = psycopg2.connect("dbname=news")
    # cursor
    cursor = db.cursor()
    # Q1
    cursor.execute("""SELECT title,  count(*) as views FROM articles a, log l WHERE a.slug = substring(l.path, 10) GROUP BY title ORDER BY views DESC LIMIT 3;""")
    results = cursor.fetchall()
    print results
    
    # Q2
    cursor.execute("""SELECT name,  count(*) as views FROM authors a, log l WHERE a.bio = substring(l.path, 10) GROUP BY name ORDER BY views DESC LIMIT 3;""")
    results = cursor.fetchall()
    print results
    
    # Q3
    cursor.execute("""SELECT date(log.time), count(log.status) * 100 / subquery1.error_instance AS error FROM (SELECT date(log.time), count(log.status) AS error_instance FROM log GROUP BY log.time ORDER BY error_instance desc) subquery1 JOIN log ON date(log.time) = subquery1.date GROUP BY log.time HAVING status='404 NOT FOUND' ORDER BY error;""")
    results = cursor.fetchall()
    print results
    
    
    # Close connection with the database
    cursor.close()
    db.close()
if __name__ == "__main__":
    main()
