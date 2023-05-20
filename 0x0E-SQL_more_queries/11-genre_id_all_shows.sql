-- A script that list all shows contained in the database hbtn_0d_tvshows
-- list all shows that has genre linked, if no show has genre display NULL
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT JOIN
tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY
tv_show.title ASC; tv_show_genres.genre_id ASC;
