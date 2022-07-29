-- This script does it all
SELECT ts.title, tg.genre_id FROM tv_shows ts
LEFT JOIN tv_show_genres tg
ON tg.show_id = ts.id OR tg.show_id = NULL
ORDER BY ts.title, tg.genre_id ASC;
