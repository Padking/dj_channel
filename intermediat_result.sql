SELECT subscr_id AS user, GROUP_CONCAT(ch_id) AS channels --|| " " AS channels
FROM ch_subscr JOIN (
	SELECT subscr_id, COUNT(subscr_id) AS Встречаемость_подписчика_в_таблице
	FROM ch_subscr
	WHERE ch_id IN ("-1001434239042", "-1001434239043") --"-1001434239042", "-1001434239043"
	GROUP BY subscr_id
	HAVING COUNT(subscr_id) > 1) as f_table
USING(subscr_id)
WHERE ch_id IN ("-1001434239042", "-1001434239043")
GROUP BY subscr_id