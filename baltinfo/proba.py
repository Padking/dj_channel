query = "WHERE ch_id IN ( {0} ) {0}"
frame = '"-1001434239042", "-1001434239043"'
new_query = query.format(frame)
# print(new_query)

query = "SELECT * FROM foo WHERE bar IN ( {} )".format(', '.join('?' * 2))
# print(query)