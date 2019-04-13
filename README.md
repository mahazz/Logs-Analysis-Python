# Udacity-FSND-Logs-Analysis-Python :trophy:

# Logs Analysis Project

## [Project Description](Project_Description.md)

## [Project_Specification](Project_Specification.md)

## Questions :construction::triangular_flag_on_post:
1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Requirements:checkered_flag:
* Python 2.7.12
* psycopg2
* Postgresql 9.5.16

## How to run :dart:

* load the data onto the database
```sql
psql -d news -f newsdata.sql
```
* connect to the database
```sql
psql -d news
```
* create views
* python2 logs_analysis.py

### Create Views:blush:

```sql
CREATE VIEW author_info AS
SELECT authors.name, articles.title, articles.slug
FROM articles, authors
WHERE articles.author = authors.id
ORDER BY authors.name;
```

```sql
CREATE VIEW path_view AS
SELECT path, COUNT(*) AS view
FROM log
GROUP BY path
ORDER BY path;
```

```sql
CREATE VIEW article_view AS
SELECT author_info.name, author_info.title, path_view.view
FROM author_info, path_view
WHERE path_view.path = CONCAT('/article/', author_info.slug)
ORDER BY author_info.name;
```
```sql
CREATE VIEW total_view AS
SELECT date(time), COUNT(*) AS views
FROM log 
GROUP BY date(time)
ORDER BY date(time);
```

```sql
CREATE VIEW error_view AS
SELECT date(time), COUNT(*) AS errors
FROM log WHERE status = '404 NOT FOUND' 
GROUP BY date(time) 
ORDER BY date(time);
```

```sql
CREATE VIEW error_rate AS
SELECT total_view.date, (100.0*error_view.errors/total_view.views) AS percentage
FROM total_view, error_view
WHERE total_view.date = error_view.date
ORDER BY total_view.date;
```
