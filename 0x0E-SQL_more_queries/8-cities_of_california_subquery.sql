-- a script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- Fetch all cities of California using the california_state_id
SELECT id, name FROM cities c
WHERE c.state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
