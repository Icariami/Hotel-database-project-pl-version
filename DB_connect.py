import psycopg2

def connect():
    '''
    Funkcja łącząca z bazą danych w postgreSQL.
    Wykorzystywana w dalszej części projektu
    '''
    return psycopg2.connect(
        host = "localhost", 
        database = "Hotel",
        user = "postgres",
        password = "Strzelce0", 
        port = "5432",
        )



