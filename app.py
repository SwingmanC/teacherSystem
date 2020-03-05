import pymysql
pymysql.install_as_MySQLdb()

from domain.__init__ import create_app,db

app = create_app('default')

if __name__ == '__main__':
    app.run(debug=True)
