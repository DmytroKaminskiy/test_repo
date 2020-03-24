import sqlite3

from flask import Flask, request

app = Flask(__name__)  # __main__


def exec_query(query: str, params: tuple = None) -> list:

    try:
        conn = sqlite3.connect('./chinook.db')  # path to file
        cursor = conn.cursor()

        if params is None:
            cursor.execute(query)
        else:
            cursor.execute(query, params)

        result = cursor.fetchall()
    finally:
        conn.close()

    return result

# client -> request -> flask -> database -> flask -> response -> client


@app.route('/customers/')
def home():
    # http://127.0.0.1:5000/customers/?country=USA&city=NewYork

    country = request.args.get('country')
    if country:
        params = (country, )
        query = f'SELECT * FROM customers WHERE Country = ?;'
        result = exec_query(query, params)
    else:
        query = f'SELECT * FROM customers;'
        result = exec_query(query)

    # from pdb import set_trace; set_trace()
    return '<br>'.join(map(str, result))


@app.route('/invoices/')
def invoices_count():
    query = 'SELECT COUNT(*) FROM invoices;'
    result = exec_query(query)
    return str(result)

'''
1. Вью функция должна принимать параметр который регулирует количество символов (вью функция генерации 10 случайных символов)
/generate-password/?length=20 + validation, [20, 10000000000000000, -20, sefsefse]
2. Вью функция должна фильтровать таблицу кастомерс по Штату И Городу ?state=IL&city=Boston ?state=IL ?city=Boston NoParameters
3. Вью функция должна выводить количество уникальных имен (FirstName) из таблицы customers
4. Вывести общую прибыль из колонки invoice_items ((UnitPrice * Quantity) + ...)
'''
