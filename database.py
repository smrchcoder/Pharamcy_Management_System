import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pharmacy_425"
)
c = mydb.cursor()


def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS customer_425(customer_id TEXT, customer_name TEXT, doctor_id TEXT, ph_no int, addr TEXT,age int)')
    c.execute("Create table if not exists drug_425(drug_id TEXT,drug_name TEXT,stock_required int,customer_id TEXT)")


def add_data(customerid, customername,doctorid,phno, addr,age):
    c.execute('INSERT INTO customer_425(customer_id, customer_name, doctor_id, ph_no, addr,age) VALUES (%s,%s,%s,'
              '%s,%s,%s)',
              (customerid, customername, doctorid, phno, addr,age))
    mydb.commit()


def view_all_data():
    c.execute('SELECT * FROM customer_425')
    data = c.fetchall()
    return data
def view1():
    c.execute("Select drug_name,count(drug_name)*stock_required as drug_count from drug_425 group by(drug_id)")
    data = c.fetchall()
    return data


def view_only_customer_names():
    c.execute('SELECT customer_name FROM customer_425')
    data = c.fetchall()
    return data


def get_customer(customer_name):
    c.execute('SELECT * FROM customer_425 WHERE customer_name="{}"'.format(customer_name))
    data = c.fetchall()
    return data


def edit_customer_data(new_customerid, new_customername, new_doctorid, new_phno, new_addr,new_age,customerid, customername,doctorid, phno, addr,age):
    c.execute("UPDATE customer_425 SET customer_id=%s, customer_name=%s, doctor_id=%s, ph_no=%s, addr=%s ,age=%s WHERE "
              "customer_id=%s and customer_name=%s and doctor_id=%s and ph_no=%s and addr=%s and age=%s ", (new_customerid, new_customername,new_doctorid, new_phno, new_addr,new_age,customerid, customername,doctorid, phno, addr,age))
    mydb.commit()
    data = c.fetchall()
    return data


def delete_data(customername):
    c.execute('DELETE FROM customer_425 WHERE Customer_Name="{}"'.format(customername))
    mydb.commit()
def run_query(query):
    data, columns, error = None, None, None
    try:
        c.execute(query)
    except mysql.connector.Error as e:
        print(e)
        return data, columns, e
    data = c.fetchall()
    columns = c.column_names
    return data, columns, error