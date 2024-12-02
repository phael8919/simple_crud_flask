from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL

#Creating the app
app = Flask(__name__)

#Configuring the database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Gestao24'
app.config['MYSQL_DB'] = 'customer'

mysql = MySQL(app)

#routes

#Initial page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert')
def insert():
    return render_template('insert.html')

@app.route('/select')
def select():
    cursor = mysql.connection.cursor()
    cursor.execute(''' select * from tb_customer ''')    
    result = cursor.fetchall()
    mysql.connection.commit()
    cursor.close()
    return render_template('select.html', result=result)

@app.route('/add', methods = ['POST'])
def add():
    if request.method == 'POST':
        name_customer = request.form['name']
        age_customer = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO tb_customer (name, age) VALUES(%s,%s)''',(name_customer,age_customer))
        mysql.connection.commit()
        cursor.close()
        return redirect('select')
    
@app.route('/change', methods=['GET', 'POST'])
def change():
    id_customer = request.args.get('id') 

    cursor = mysql.connection.cursor()
    cursor.execute(''' select * from tb_customer where id = %s''',id_customer)
    mysql.connection.commit()
    result = cursor.fetchone()
    cursor.close()
    

    return render_template('change.html',id=id_customer, name=result[1], age = result[2])

@app.route('/update', methods=['GET','POST'])
def update():
    id = request.form['id']
    name = request.form['name']
    age = request.form['age']

    print("id:",id)

    cursor = mysql.connection.cursor()
    cursor.execute(''' update tb_customer set name=%s, age=%s where id = %s ''', (name, age, id))
    mysql.connection.commit()
    cursor.close()

    return redirect(url_for('select'))

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    id_customer = request.args.get('id') 

    cursor = mysql.connection.cursor()
    cursor.execute(''' delete from tb_customer where id = %s''',id_customer)
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('select'))

#execute the app
app.run(debug=True)