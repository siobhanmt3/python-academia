#Siobhan
from pymongo import MongoClient

#Base de datos
MONGODB_URL = "mongodb://academia:academia@localhost:27017"

def get_db():
    mongodb_client = MongoClient(MONGODB_URL)

    return mongodb_client["academia"]

def insert(items: list):
    database = get_db()

    for item in items:
        database.inventory.insert_one(item)

#Imprimir por categoría
def get(filter: dict):
    database = get_db()

    for item in database.inventory.find(filter):
        print(item)

get(filter={"category": "Cocina"})

#Eliminar por nombre
def delete(filter: dict):
    database = get_db()

    result = database.inventory.delete_many(filter)
    print(f"Se eliminaron {result.deleted_count} elementos")

delete(filter={"name": "Tenedor"})

#Actualizar por nombre
def update(filter: dict, update: dict):
    database = get_db()

    result = database.inventory.update_many(filter, {"$set": update})
    print(f"Se actualizaron {result.modified_count} elementos")

update(filter={"name": "Cuchara"}, update={"price": 10})


#insert([
#    {
#        "name": "Tenedor",
#        "category": "Cocina",
#        "quantity": 20,
#        "price": 5,
#    },
#    {
#        "name": "Cuchara",
#        "category": "Cocina",
#        "quantity": 15,
#        "price": 3,
#    },
#    {
#        "name": "Papel de baño",
#        "category": "Blancos",
#        "quantity": 50,
#        "price": 15,
#    }   
#])