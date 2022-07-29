-- This script does most of the work here. Joining and some querying
SELECT ts.title, tg.genre_id FROM tv_shows ts
LEFT JOIN tv_show_genres tg
ON tg.show_id = ts.id
WHERE tg.genre_id IS NULL
ORDER BY ts.title, tg.genre_id ASC;
