import pymysql


class Controller:

    def menu(self):
        while True:
            print(
                "Choose a menu item by number: \n" +
                  "1. Add new Plant \n" +
                  "2. Add new Employee \n" +
                  "3. Get plant by id \n" +
                  "4. Get employee by id \n" +
                  "5. Add new Salon \n" +
                  "6. Get salon by id \n"
                  )
            break
        self.menu_flag = int(input("Your choose: "))

    def create_plant(self):
        if self.menu_flag == 1:
            self.connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root',
                                              password='SQListhebest', db='RENEE')
            print("Successfully connected...")
            print("#" * 30)
            try:
                with self.connection.cursor() as cursor:
                    location = input("Location: ")
                    name = input("Plant name: ")
                    id = input("Director id: ")
                    insert_query = "INSERT INTO PLANTS(LOCATION, NAME, DIRECTOR_ID) VALUES ('{}', '{}', '{}')".format(
                        str(location), str(name), str(id))
                    cursor.execute(insert_query)
                    self.connection.commit()
            finally:
                pass

            try:
                cur = self.connection.cursor()
                cur.execute("SELECT * FROM PLANTS")
                for row in cur.fetchall():
                    print(row[0], "|", row[1], "|", row[2], "|", row[3])
            finally:
                self.connection.close()

    def create_employee(self):
        if self.menu_flag == 2:
            self.connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root',
                                              password='SQListhebest', db='RENEE')
            print("Successfully connected...")
            print("#" * 30)
            try:
                with self.connection.cursor() as cursor:
                    name = input("Name: ")
                    email = input("Email: ")
                    type = input("Department type: ")
                    id = int(input("Department id: "))
                    salon = input("Salon name: ")
                    insert_query = "INSERT INTO EMPLOYEES(NAME, EMAIL, DEPARTMENT_TYPE, DEPARTMENT_ID, SALON) VALUES ('{}', '{}', '{}', '{}', '{}')".format(
                        str(name), str(email), str(type), str(id), str(salon))
                    cursor.execute(insert_query)
                    self.connection.commit()
            finally:
                pass

            try:
                cur = self.connection.cursor()
                cur.execute("SELECT * FROM EMPLOYEES")

                for row in cur.fetchall():
                    print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5])
            finally:
                self.connection.close()

    def plant_id(self):
        if self.menu_flag == 3:
            connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root',
                                         password='SQListhebest', db='RENEE')
            print("#" * 30)
            try:
                with connection.cursor() as cursor:
                    a = input("Enter Plant ID: ")
                    cursor.execute("SELECT * FROM PLANTS WHERE ID = " + a)
                    for row in cursor.fetchall():
                        print(row[0], "|", row[1], "|", row[2], "|", row[3])
            finally:
                connection.close()

    def employee_id(self):
        if self.menu_flag == 4:
            connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root',
                                         password='SQListhebest', db='RENEE')
            print("#" * 30)
            try:
                with connection.cursor() as cursor:
                    a = input("Enter Employee ID: ")
                    cursor.execute("SELECT * FROM EMPLOYEES WHERE ID = " + a)
                    for row in cursor.fetchall():
                        print(row[0], "|", row[1], "|", row[2], "|", row[3], "|", row[4], "|", row[5])
            finally:
                connection.close()


    def create_salon(self):
        if self.menu_flag == 5:
            self.connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root',
                                              password='SQListhebest', db='RENEE')
            print("Successfully connected...")
            print("#" * 30)

            try:
                with self.connection.cursor() as cursor:
                    location = input("Location: ")
                    name = input("Salon name: ")
                    id = input("Director id: ")
                    insert_query = "INSERT INTO SALONS(LOCATION, NAME, DIRECTOR_ID) VALUES ('{}', '{}', '{}')".format(
                        str(location), str(name), str(id))
                    cursor.execute(insert_query)
                    self.connection.commit()
            finally:
                pass

    def salon_id(self):
        if self.menu_flag == 6:
            connection = pymysql.connect(host='127.0.0.1', unix_socket='/tmp/mysql.sock', user='root',
                                         password='SQListhebest', db='RENEE')
            print("#" * 30)
            try:
                with connection.cursor() as cursor:
                    a = input("Enter SALON ID: ")
                    cursor.execute("SELECT * FROM SALONS WHERE ID = " + a)
                    for row in cursor.fetchall():
                        print(row[0], "|", row[1], "|", row[2], "|", row[3])
            finally:
                connection.close()

    def run(self):
        c = Controller()
        c.menu()
        c.create_plant()
        c.create_employee()
        c.plant_id()
        c.employee_id()
        c.create_salon()
        c.salon_id()

