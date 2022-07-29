-- This script selects all shows of title Dexter
SELECT genres.name FROM tv_genres genres
INNER JOIN tv_show_genres tg
ON tg.genre_id = genres.id
INNER JOIN tv_shows tvs
ON tg.show_id = tvs.id
WHERE tvs.title = "Dexter"
ORDER BY genres.name ASC;
