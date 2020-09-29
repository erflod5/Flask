from flask import Flask
from flask_mysqldb import MySQL

app = Flask('project')
app.config['MYSQL_HOST'] = '127.0.0.1' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'secret'
app.config['MYSQL_DB'] = 'ANALISIS'
app.config['MYSQL_PORT'] = 3307

mysql = MySQL(app)

from project.controllers import *