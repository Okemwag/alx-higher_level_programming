-- This script lists shows by their rating
SELECT title, SUM(rate) AS rating FROM tv_shows ts
LEFT JOIN tv_show_ratings tr
ON ts.id = tr.show_id
GROUP BY ts.id
ORDER BY rating DESC;
