#!/usr/bin/python
# -*- coding: utf-8 -*-

import psycopg2


def database_connect(news):
    """
Connect to the database.
"""


try:
    db = psycopg2.connect('dbname=news')
    cursor = db.cursor()
    return (db, cursor)
except psycopg2.Error, error:
    print 'Unable to connect to database'
    sys.exit(1)

    # db = psycopg2.connect(news)
# cursor

cursor = db.cursor()


# Q1

def print_top_three_articles():
    """
The most popular three articles of all time:
"""


query = \
    """select articles.title , COUNT(log.path) AS views from articles, log
    WHERE articles.slug = substring(log.path, 10, 23) group by articles.title
    order by views DESC LIMIT 3;"""
results = execute_query(query)


# Q2

def print_top_authors():
    """
The most popular article authors of all time:
"""


query = \
    """select authors.name , COUNT(log.path) AS views from authors, log
    group by authors.name order by views DESC;"""
results = execute_query(query)


# Q3

def print_errors_over_one():
    """
The days did more than 1% of requests lead to error:
"""


query = \
    """select to_char(total_all_status.date, 'FMMonth FMDD, YYYY') AS date,
    errors_requests.requests from errors_requests, total_all_status
    where errors_requests.requests > 1
    group by total_all_status.date, errors_requests.requests
    order by errors_requests.requests DESC;"""
results = execute_query(query)

if __name__ == '__main__':
    print_top_three_articles()
    print_top_authors()
    print_errors_over_one()

    # Close connection with the database

    cursor.close()
    db.close()
    connection.close()
