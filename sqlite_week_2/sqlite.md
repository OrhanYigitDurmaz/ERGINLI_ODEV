to list tables:

res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()

if it doesnt exist, it returns None
