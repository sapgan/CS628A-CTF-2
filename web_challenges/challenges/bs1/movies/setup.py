import sqlite3
from hashlib import md5
secret = "asdasd98a9ndand987a83nuindna9721n9n923"

ufp = "/home/vagrant/scripts/shell_details"
uf = open(ufp,"r").readlines()
for user in uf:
    u,p = user.strip().split(":")
    flag = "cs628a{"+md5((secret+u).encode('utf-8')).hexdigest()+"}"
    movies = [{"Dark Knight Rises", "Nolan"},{"Godfather", "Brando"},{"Shawshank Redemption","Freeman"},{"Batman","Nolan"},{"Avengers","Marvel"}]
    movies.append({"asdasdhasuh767da8m787adnb65aad8665adb7",flag})
    db_name = "movies_"+u+".db"
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('CREATE TABLE movies (title text, director text);')
    for title,director in movies:
        stmt = "INSERT INTO movies VALUES ('{}','{}')".format(title,director)
        c.execute(stmt)
    conn.commit()
    conn.close()
