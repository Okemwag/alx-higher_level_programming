-- This script selects all genres not linked to the show selected
SELECT DISTINCT g.name FROM tv_genres g
WHERE g.name NOT IN(
	SELECT name 
    FROM tv_shows shows
    INNER JOIN tv_show_genres mg
    ON shows.id = mg.show_id 
    INNER JOIN tv_genres
    ON mg.genre_id = tv_genres.id 
    WHERE shows.title = 'Dexter'
) 
ORDER BY g.name ASC;
