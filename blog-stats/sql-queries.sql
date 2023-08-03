-- Get all of the recorded views, along with the article title and author

SELECT stats_articleviews.article_views_article_id_fk_id as id, 
				 stats_articles.title, 
				 stats_articleviews.change, 
				 stats_articleviews.count as view_count, 
				 stats_articleviews.date_added as time_collected,
				 stats_articles.published_date, 
				 users_user.username as author

FROM stats_articleviews

INNER JOIN stats_articles ON stats_articleviews.article_views_article_id_fk_id = stats_articles.article_id

INNER JOIN users_user ON stats_articles.article_user_id_fk_id = users_user.id /* Get the username */

ORDER BY stats_articleviews.date_added DESC;
