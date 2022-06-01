How to run the flask app:
*  connect to perlman and clone the team repo
*  go to ../Backend
*  create psqlConfig.py with a database name (teamc). a user name (teamc), and a password
*  run: psql -U teamc -h localhost -d teamc < createtable.sql
*  run: psql -U teamc -h localhost -d teamc
*  run: \copy productTable FROM 'UpdatedFinalData.csv' DELIMITER ',' CSV
*  go to ../Code
*  run: python3 flaskapp.py

# Team C
Team members: 
* Kana 
* Isabella 

