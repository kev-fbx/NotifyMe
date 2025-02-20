import pyodbc
import os

def connect_to_db(path):
    """Creates connection to an Access database.

    Args:
        path (str): File path to the Access database.

    Returns:
        pyodbc.Connection: pyodbc connection object.
    """
    abs_path = os.path.abspath(path)
    conn = (r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
            f'DBQ={abs_path};')
    return pyodbc.connect(conn)