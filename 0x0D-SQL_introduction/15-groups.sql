-- selects the scores and count them
SELECT score, COUNT(score) AS number
FROM second_table
GROUP BY score
ORDER BY NUMBER DESC;
