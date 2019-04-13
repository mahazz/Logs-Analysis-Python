#!/usr/bin/env python2

import psycopg2
def main():
    # Connect to database
    db = psycopg2.connect("dbname=news")
    # cursor
    cursor = db.cursor()
    # Q1
    cursor.execute("""SELECT title,  count(*) as views FROM articles a, log l WHERE a.slug = substring(l.path, 10) GROUP BY title ORDER BY views DESC LIMIT 3;""")
    print("Most popular authors:")
    results = cursor.fetchall()
    print results

    # Q2
    sql_popular_authors = """
    SELECT article_view.name, SUM(article_view.view) AS author_view
    FROM article_view
    GROUP BY article_view.name
    ORDER BY author_view DESC;
    """
    cursor.execute(sql_popular_authors)
    print("Most popular authors:")
    for (name, view) in cursor.fetchall():
        print("    {} - {} views".format(name, view))
    print("-" * 70)

    # Q3
    sql_more_than_one_percent_errors = """
    SELECT *
    FROM error_rate
    WHERE error_rate.percentage > 1
    ORDER BY error_rate.percentage DESC;
    """
    cursor.execute(sql_more_than_one_percent_errors)
    print("Days with more than 1% errors:")
    for (date, percentage) in cursor.fetchall():
        print("    {} - {}% errors".format(date, percentage))
    print("-" * 70)


    # Close connection with the database
    cursor.close()
    db.close()
if __name__ == "__main__":
    main()
