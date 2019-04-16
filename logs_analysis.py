
#!/usr/bin/env python2

import psycopg2


def database_connect("news"): """
Connect to the database.  Returns a database connection.
"""
try:
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    return db, c
except psycopg2.Error as e:
        print ("Unable to connect to database")
        sys.exit(1)
    db = psycopg2.connect("dbname=news")
# cursor
cursor = db.cursor()
def print_top_articles(): """
Prints out the top 3 articles of all time.
"""
    query = "SELECT title,  count(*) as views FROM articles a, log l WHERE a.slug = substring(l.path, 10) GROUP BY title ORDER BY views DESC LIMIT 3;"
    results = execute_query(query)

def print_top_authors(): """
Prints a list of authors ranked by article views.
"""
    query = "SELECT article_view.name, SUM(article_view.view) AS author_view FROM article_view GROUP BY article_view.name ORDER BY author_view DESC;"
    results = execute_query(query)

def print_errors_over_one(): """
Prints out the days where more than 1% of logged access requests were errors.
"""
    query = "select to_char(date, 'FMMonth FMDD, YYYY'), err/total as ratio from (select time::date as date, count(*) as total, sum((status != '200 OK')::int)::float as err from log group by date) as errors where err/total > 0.01;"
    results = execute_query(query)
    
if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one()

    # Close connection with the database
    cursor.close()
    db.close()
    connection.close();
