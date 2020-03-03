-- Lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Query to perform operation
SELECT gr.name, COUNT(shgr.genre_id) AS number_of_shows FROM tv_genres AS gr
       JOIN tv_show_genres AS shgr
       ON gr.id=shgr.genre_id
       GROUP BY shgr.genre_id
       ORDER BY number_of_shows DESC;
