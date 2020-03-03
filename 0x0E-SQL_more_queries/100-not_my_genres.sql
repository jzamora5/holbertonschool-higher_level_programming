-- List all genres not linked to the show Dexter
-- Query to perform operation
SELECT gr.name FROM tv_genres AS gr
LEFT JOIN
(
       SELECT gr.id, gr.name FROM tv_genres AS gr
       JOIN tv_show_genres AS shgr
       	    ON gr.id=shgr.genre_id
       JOIN tv_shows AS sh
       	    ON shgr.show_id=sh.id
       WHERE sh.title = "Dexter"
       ORDER BY gr.name ASC
) AS subdx
ON subdx.id = gr.id
WHERE subdx.name IS NULL
ORDER BY gr.name ASC;
