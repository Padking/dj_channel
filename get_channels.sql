SELECT DISTINCT ch_id AS chnl
FROM channel JOIN ch_subscr
USING(ch_id)
