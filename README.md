# Udacity-FSND-Logs-Analysis-Python :trophy:

# Logs Analysis Project

## [Project Description](Project_Description.md)

## [Project_Specification](Project_Specification.md)

## Questions :construction::triangular_flag_on_post:
1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a          sorted list with the most popular article at the top.
2. Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which        authors get the most page views? Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code    that the news site sent to the user's browser. 

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
* python logs.py

### Create Views:blush:

```sql
CREATE VIEW total_errors AS
SELECT date(time), COUNT(status) AS errors
FROM log WHERE status != '200 OK' 
GROUP BY date(time) 
ORDER BY errors DESC;
```

```sql
CREATE VIEW total_all_status AS
SELECT date(time), COUNT(status) AS all_status
FROM log
GROUP BY date(time)
ORDER BY all_status DESC;
```

```sql
CREATE VIEW errors_requests AS
select total_all_status.date, (100.0 * total_errors.errors/total_all_status.all_status) AS requests
from total_errors, total_all_status where errors_requests.requests > 1
order by total_all_status.date;
```

