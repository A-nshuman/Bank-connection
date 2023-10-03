import mysql.connector

connection = mysql.connector.connect(host="localhost", user="root", passwd="123456789", database="bank")
cursor = connection.cursor()

def add_text(text_value, t_name):
    try:
        cursor.execute("INSERT INTO users(f_name, l_name, email, uname, upwd, phone) VALUES (%s,%s,%s,%s,%s,%s)", (text_value))
        cursor.execute(f"CREATE TABLE if not exists {t_name}(Statement varchar(225), entry_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")
        cursor.execute(f"INSERT INTO {t_name}(Statement) values('Account Created')")
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed inserting record into table {}".format(error))
    finally:
        print('inserted')

def check_login_credentials(email, password):
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s AND upwd = %s", (email, password))
        result = cursor.fetchone()
        if result:
            return True
        else:
            return False
    except mysql.connector.Error as error:
        print("Error checking login credentials: {}".format(error))
        return False
    
def get_name(email):
    query = "SELECT f_name, l_name, balance FROM users WHERE email = %s"
    cursor.execute(query, (email,))
    user_data = cursor.fetchone()
    return user_data

# def check_email_exist(email):
#     try:
#         query = "SELECT * FROM users WHERE email = %s"
#         cursor.execute(query, (email,))

#         result = cursor.fetchone()

#         if result:
#             return True
#         else:
#             return False
#     except mysql.connector.Error as error:
#         print("Error checking email existence: {}".format(error))
#         return False
#     finally:
#         connection.commit()

# def check_email_exist(email):
#     try:
#         cursor.execute("SELECT email FROM users WHERE email = %s", (email,))
#         result = cursor.fetchone()
#         if result:
#             return True
#         else:
#             return False
#     except mysql.connector.Error as error:
#         print("Error checking email existence: {}".format(error))
#         return False

def get_data():
    cursor.execute("SELECT * FROM mytable")
    rows = cursor.fetchall()    
    return rows