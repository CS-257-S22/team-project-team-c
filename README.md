This is the revision for the team front-end deliverable. In particular we worked on: 
* updated our 404 page (probably useful to have html code for it so it looks similar to rest of site). 
*put our site name somewhere consistent across the pages (probably near the top) for clarity and navigation. A
* Additionally, the distance from the top of the page to the nav bar should be consistent (it's currently lower on your results page). 


# Team C
Team members: 
* Kana 
* Isabella 

How to run the flask app:
*  connect to perlman and clone the team repo
*  go to ../Backend
*  create psqlConfig.py with a database name (teamc). a user name (teamc), and a password
*  run: psql -U teamc -h localhost -d teamc < createtable.sql
*  run: psql -U teamc -h localhost -d teamc
*  run: \copy productTable FROM 'FinalData.csv' DELIMITER ',' CSV
*  go to ../Code
*  run: python3 flaskapp.py