from project import app, mysql
from flask import render_template, redirect, url_for, request


@app.route('/order', methods=['GET'])
def index_order():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id_pedido, origen, destino, concat(nombre, ' ', apellido), producto, ubicacion FROM Pedido INNER JOIN Usuario ON id_usuario = usuario_id_usuario")
    data = cursor.fetchall()
    cursor.close()

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id_usuario, concat(nombre, ' ', apellido) FROM Usuario")
    users = cursor.fetchall()
    cursor.close()

    return render_template('order/index.html', orders=data, users=users)


@app.route('/order', methods=['POST'])
def create_order():
    origen = request.form['origen']
    destino = request.form['destino']
    producto = request.form['producto']
    address = request.form['address']
    user = request.form['usersSelect']
    print(user)
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO Pedido(origen, destino, usuario_id_usuario, producto, ubicacion) VALUES(%s, %s, %s, %s, %s)', (origen, destino, int(user), producto, address))
    mysql.connection.commit()
    return redirect(url_for('index_order'))



@app.route('/order/edit/<id>', methods=['GET', 'POST'])
def get_order(id):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT id_pedido, origen, destino, producto, ubicacion, usuario_id_usuario FROM Pedido WHERE id_pedido = %s', (id))
    data = cursor.fetchall()
    cursor.close()
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id_usuario, concat(nombre, ' ', apellido) FROM Usuario")
    users = cursor.fetchall()
    cursor.close()

    return render_template('order/editOrder.html', order=data[0], users=users)


@app.route('/order/update/<id>', methods=['POST'])
def update_order(id):
    origen = request.form['origen']
    destino = request.form['destino']
    producto = request.form['producto']
    address = request.form['address']
    user = request.form['usersSelect']
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE Pedido SET origen = %s, destino = %s, producto = %s, ubicacion = %s, usuario_id_usuario = %s WHERE id_pedido = %s', (origen, destino, producto, address, int(user), int(id)))
    mysql.connection.commit()
    return redirect(url_for('index_order'))


@app.route('/order/delete/<string:id>', methods=['POST', 'GET'])
def delete_order(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM Pedido WHERE id_pedido = {0}'.format(id))
    mysql.connection.commit()
    return redirect(url_for('index_order'))