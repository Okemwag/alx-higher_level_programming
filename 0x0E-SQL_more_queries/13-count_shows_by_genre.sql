-- This script selects the number of rows linked to each genre
SELECT genres.name AS genre, COUNT(tg.genre_id) AS number_of_shows
FROM tv_genres genres
INNER JOIN tv_show_genres tg
ON tg.genre_id = genres.id
GROUP BY tg.genre_id
ORDER BY number_of_shows DESC;
