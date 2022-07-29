-- This script selects all genres not linked to the show selected
SELECT title FROM tv_shows ws
WHERE title NOT IN(
	SELECT title FROM tv_shows ws
    INNER JOIN tv_show_genres mg
    ON ws.id = mg.show_id 
    INNER JOIN tv_genres
    ON tv_genres.id = mg.genre_id 
    WHERE tv_genres.name = 'Comedy'
) 
ORDER BY title ASC;
