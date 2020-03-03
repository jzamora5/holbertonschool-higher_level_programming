-- Lists all the cities of California that can be found in the database hbtn_0d_usa
-- Query to perform operation
SELECT c.id, c.name FROM cities AS c, states AS s
       WHERE c.state_id=s.id AND s.name = "California";
