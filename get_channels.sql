SELECT DISTINCT ch_id AS chnl, username_ch AS username
FROM channel JOIN ch_subscr
USING(ch_id)
