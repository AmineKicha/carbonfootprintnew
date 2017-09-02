import MySQLdb

def connection():
    conn = MySQLdb.connect("pcfc.mysql.pythonanywhere-services.com","pcfc","pcfc9495966059","pcfc$tcs_user_data")
    c = conn.cursor()
    return c,conn