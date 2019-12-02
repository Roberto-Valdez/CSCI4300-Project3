from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import json

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1:4800' #replace with your own nginx host number                                                                                              
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password' #replace with your own mysql password                                                                                                   
app.config['MYSQL_DB'] = 'classicmodels'
mysql = MySQL(app)

@app.route("/p3/", methods=['GET', 'POST'])
def index():
    print("test1")
    if request.method == 'POST':                                                                                                                               
        employeeID = request.form                                                                                                                                                
        id = employeeID['employeeID'] #stores desired employeeID to be used in the mysql query later                                                                             
        cur = mysql.connection.cursor()
        tableResults = cur.execute("SELECT employeeNumber, orderdetails.orderNumber, quantityOrdered*priceEach AS Sales FROM customers JOIN orders ON customers.customerNumber = \
orders.customerNumber JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber JOIN employees ON employees.employeeNumber = customers.salesRepEmployeeNumber;") #insert\
 query here and use where id = employeeID from up above                                                                                                                           
        print("test2")
        if tableResults > 0:  #check to see if there are results associated with the employeeID number                                                                            
            rows = [x[0] for x in cur.description]
            tableDetails = cur.fetchall()
            json = []
            for result in tableDetails:
                json_data.append(dict(zip(rows,result)))
            jsonString = json.dumps(json) #returns json data, still need to figure out how to link to HTML and possibly parse using jQuery.getJSON() functions                    
            print(jsonString)
            print("test3")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


