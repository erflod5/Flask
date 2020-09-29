from project import app, mysql
from flask import render_template, redirect, url_for, request


@app.route('/user', methods=['GET'])
def index_users():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Usuario')
    data = cursor.fetchall()
    cursor.close()
    return render_template('user/index.html', users=data)

@app.route('/user', methods=['POST'])
def create_user():
    name = request.form['name']
    code = request.form['code']
    lastname = request.form['lastname']
    age = request.form['age']
    address = request.form['address']
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO Usuario VALUES(%s, %s, %s, %s, %s)', (int(code), name, lastname, int(age), address))
    mysql.connection.commit()
    return redirect(url_for('index_user'))


@app.route('/user/edit/<id>', methods=['GET', 'POST'])
def get_user(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM Usuario WHERE id_usuario = %s', (id))
    data = cursor.fetchall()
    cursor.close()
    return render_template('user/editUser.html', user=data[0])


@app.route('/user/update/<id>', methods=['POST'])
def update_user(id):
    name = request.form['name']
    lastname = request.form['lastname']
    age = request.form['age']
    address = request.form['address']
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE Usuario SET nombre = %s, apellido = %s, edad = %s, direccion = %s WHERE id_usuario = %s', (name, lastname, int(age), address, int(id)))
    mysql.connection.commit()
    return redirect(url_for('index_users'))


@app.route('/user/delete/<string:id>', methods=['POST', 'GET'])
def delete_user(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('DELETE FROM Usuario WHERE id_usuario = {0}'.format(id))
        mysql.connection.commit()
    except:
        print('No se pudo eliminar el usuario')
    return redirect(url_for('index_users'))