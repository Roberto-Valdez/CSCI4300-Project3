
import mysql.connector
from pprint import pprint
import json
import decimal

creds = { 'user' : 'FOO',
          'database' : 'classicmodels',
          'password' : 'FOOp4ss$',
          'auth_plugin' : 'mysql_native_password'}


def application (env, start_response):
    if env['REQUEST_METHOD'] == 'GET':
        start_response('200 OK', [('Content-Type', 'application/json')])
        body = env['QUERY_STRING']
        id = body.split('=')[-1]
        id = int(id)

        cnx = mysql.connector.connect(**creds)

        cursor = cnx.cursor(dictionary=True)

        cursor.execute('SELECT customers.salesRepEmployeeNumber AS employeeNumber, orderdetails.orderNumber, productCode, quantityOrdered, priceEach, quantityOrdered*priceEach as total FROM customers JOIN orders ON customers.customerNumber = orders.customerNumber JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber WHERE customers.salesRepEmployeeNumber = id;')

        values = cursor.fetchall()

        def decimal_default(obj):
            if isinstance(obj, decimal.Decimal):
                return float(obj)
            raise TypeError

#        html = open("jq5.html")
#        return html.read()
       
        return(json.dumps(values, default=decimal_default))
