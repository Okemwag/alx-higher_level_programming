-- This script lists genres by their rating
SELECT name, SUM(rate) AS rating FROM tv_genres g
INNER JOIN tv_show_genres tvg
ON tvg.genre_id = g.id
INNER JOIN tv_shows tvs
ON tvs.id = tvg.show_id
INNER JOIN tv_show_ratings tr
ON tr.show_id = tvs.id
GROUP BY g.name
ORDER BY rating DESC;
