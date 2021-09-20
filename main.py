import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='', database='food_orders')

# Функции для ресторана
def addRestaurant(name, address):
    global mydb
    mycursor = mydb.cursor()
    sql = 'INSERT INTO restaurants (id, name, address) VALUES (NULL, %s, %s)'
    values = (name, address)
    mycursor.execute(sql, values)
    mydb.commit()

def deleteRestaurant(id):
    global mydb
    mycursor = mydb.cursor()
    sql = 'DELETE FROM restaurants WHERE id = '+str(id)
    mycursor.execute(sql)
    mydb.commit()

def updateRestaurant(id, name, address):
    global mydb
    mycursor = mydb.cursor()
    sql = 'UPDATE restaurants SET name = %s, address = %s WHERE id = '+str(id)
    values = (name, address)
    mycursor.execute(sql, values)
    mydb.commit()

def getAllRestaurants():
    global mydb
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM restaurants'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for res in result:
        print(res)

# Функции для типа еды
def add_food_types(name):
    global mydb
    mycursor = mydb.cursor()
    sql = 'INSERT INTO food_types (id, name) VALUES (NULL, %s)'
    values = (name,)
    mycursor.execute(sql, values)
    mydb.commit()

def delete_food_types(id):
    global mydb
    mycursor = mydb.cursor()
    sql = 'DELETE FROM food_types WHERE id = '+str(id)
    mycursor.execute(sql)
    mydb.commit()

def update_food_types(id, name):
    global mydb
    mycursor = mydb.cursor()
    sql = 'UPDATE food_types SET name = %s WHERE id = '+str(id)
    values = (name,)
    mycursor.execute(sql, values)
    mydb.commit()

def get_food_types():
    global mydb
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM food_types'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for res in result:
        print(res)

# Функции для блюд
def addFoods(name, price, description, foodtype_id, restaurant_id):
    global mydb
    mycursor = mydb.cursor()
    sql = 'INSERT INTO foods (id, name, price, description, foodtype_id, restaurant_id) ' \
          'VALUES (NULL, %s, %s, %s, %s, %s)'
    values = (name, price, description, foodtype_id, restaurant_id)
    mycursor.execute(sql, values)
    mydb.commit()

def deleteFoods(id):
    global mydb
    mycursor = mydb.cursor()
    sql = 'DELETE FROM foods WHERE id = '+str(id)
    mycursor.execute(sql)
    mydb.commit()

def updateFoods(id, name, price, description, foodtype_id, restaurant_id):
    global mydb
    mycursor = mydb.cursor()
    sql = 'UPDATE foods SET name = %s, price = %s, description = %s, foodtype_id = %s, restaurant_id = %s WHERE id = '+str(id)
    values = (name, price, description, foodtype_id, restaurant_id)
    mycursor.execute(sql, values)
    mydb.commit()

def getAllFoods():
    global mydb
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM foods'
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for res in result:
        print(res)

# Консоль управления
while True:
    choice = input('Press 1 to add restaurant.\n'
                   'Press 2 to delete restaurant.\n'
                   'Press 3 to update restaurant.\n'
                   'Press 4 to list all restaurants.\n'
                   'Press 5 to add food type.\n'
                   'Press 6 to delete food type.\n'
                   'Press 7 to update food type.\n'
                   'Press 8 to list all food types.\n'
                   'Press 9 to add food.\n'
                   'Press 10 to delete food.\n'
                   'Press 11 to update food.\n'
                   'Press 12 to list all foods.\n'
                   'Press 0 to exit.\n')

    if choice == '1':
        name = input('Insert name: ')
        address = input('Insert address: ')
        addRestaurant(name, address)
        print('')
        print('Restaurant was added to database\n')

    elif choice == '2':
        id = int(input('Insert id: '))
        deleteRestaurant(id)
        print('')
        print(f'Restaurant with id = {id} was deleted\n')

    elif choice == '3':
        id = int(input('Insert id: '))
        name = input('Insert name: ')
        address = input('Insert address: ')
        updateRestaurant(id, name, address)
        print('')
        print(f'Restaurant with id = {id} was updated\n')

    elif choice == '4':
        getAllRestaurants()
        print('')

    elif choice == '5':
        name = input('Insert name: ')
        add_food_types(name)
        print('')
        print('Food type was added to database\n')

    elif choice == '6':
        id = int(input('Insert id: '))
        delete_food_types(id)
        print('')
        print(f'Food type with id = {id} was deleted\n')

    elif choice == '7':
        id = int(input('Insert id: '))
        name = input('Insert name: ')
        update_food_types(id, name)
        print('')
        print(f'Food type with id = {id} was updated\n')

    elif choice == '8':
        get_food_types()
        print('')

    elif choice == '9':
        name = input('Insert name: ')
        price = int(input('Insert price: '))
        description = input('Insert description: ')
        foodtype_id = int(input('Insert foodtype id: '))
        restaurant_id = int(input('Insert restaurant id: '))
        addFoods(name, price, description, foodtype_id, restaurant_id)
        print('')
        print('Food was added to database\n')

    elif choice == '10':
        id = int(input('Insert id: '))
        deleteFoods(id)
        print('')
        print(f'Food with id = {id} was deleted\n')

    elif choice == '11':
        id = int(input('Insert id: '))
        name = input('Insert name: ')
        price = int(input('Insert price: '))
        description = input('Insert description: ')
        foodtype_id = int(input('Insert foodtype id: '))
        restaurant_id = int(input('Insert restaurant id: '))
        updateFoods(id, name, price, description, foodtype_id, restaurant_id)
        print('')
        print(f'Food with id = {id} was updated\n')

    elif choice == '12':
        getAllFoods()
        print('')

    elif choice == '0':
        exit()
