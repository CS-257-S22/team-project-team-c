# Team C
Team members: 
* Kana 
* Isabella 

How to run the flask app:
1 connect to perlman and clone the team repo
2 go to ../Backend
3 create psqlConfig.py with a database name (teamc). a user name (teamc), and a password
4 run: psql -U teamc -h localhost -d teamc < createtable.sql
5 run: psql -U teamc -h localhost -d teamc
6 run: \copy productTable FROM 'FinalData.csv' DELIMITER ',' CSV
7 go to ../Code
8 run: python3 flaskapp.py