import psycopg2

def connect():
    return psycopg2.connect(
        host = "localhost", 
        database = "Hotel",
        user = "postgres",
        password = "Strzelce0", 
        port = "5432",
        )



