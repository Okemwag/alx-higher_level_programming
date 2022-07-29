-- This script filters TABLES using JOIN
SELECT c.id, c.name, s.name FROM cities c
INNER JOIN states s
ON c.state_id = s.id
ORDER BY c.id ASC;
