import psycopg2

CREATE_TABLE = """CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    age INT
);"""
                                            
SHOW_ALL = "SELECT * FROM person"

connection = psycopg2.connect(
    host='localhost', 
    dbname='postgres', 
    user='postgres', 
    password='1234', 
    port=5432
)

cursor = connection.cursor()

# Creates table
def create_table():
    with connection:
        cursor.execute(CREATE_TABLE)

# Create a new entry in the table
def insert_person(person_name, person_age):
    with connection:
        cursor.execute(f"INSERT INTO person (name, age) VALUES ('{person_name}', {person_age});")

# Read all entries in the table
def show_all_persons():
    with connection:
        cursor.execute(SHOW_ALL)
        results = cursor.fetchall()
        return results

# Update a person's name
def update_person(id, name):
    with connection:
        cursor.execute(f"UPDATE person SET name = '{name}' WHERE id = {id}")

# Delete a person by ID
def delete_person(id):
    with connection:
        cursor.execute(f"DELETE FROM person WHERE id = {id}")