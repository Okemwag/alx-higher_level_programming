-- This script selects all shows of name Comedy
SELECT ts.title FROM tv_shows ts
INNER JOIN tv_show_genres tg
ON ts.id = tg.show_id
INNER JOIN tv_genres tvg
ON tvg.id = tg.genre_id
WHERE tvg.name = "Comedy"
ORDER BY ts.title ASC;
