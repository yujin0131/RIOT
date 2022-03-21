import pymysql

conn = pymysql.connect(host='172.30.138.32' user='yujin' password='admin123' db='yujin' charset='utf8')
cur = conn.cursor()
