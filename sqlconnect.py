import psycopg2
from sshtunnel import SSHTunnelForwarder

def connect():
    file = open(".credentials")
    username = file.readline()
    username = username.strip().split("=")[1]
    password = file.readline()
    password = password.strip().split("=")[1]

    # username = "YOUR_CS_USERNAME"
    # password = "YOUR_CS_PASSWORD"
    server_name = "starbug.cs.rit.edu"
    db_name = "p320_19"


    try:
        with SSHTunnelForwarder((server_name, 22),
                                ssh_username=username,
                                ssh_password=password,
                                remote_bind_address=('localhost', 5432)) as server:
            server.start()
            print("SSH tunnel established")
            params = {
                'database': db_name,
                'user': username,
                'password': password,
                'host': 'localhost',
                'port': server.local_bind_port
            }

            conn = psycopg2.connect(**params)
            print("Connected to Database")
            return conn
    except:
        print("Connection failed")


def disconnect(conn):
    print("Database connection established")
    conn.close()
