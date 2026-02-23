import pyodbc

def get_connection():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-VOE4O80\SQLEXPRESS01;'
        'DATABASE=users;'
        'Trusted_Connection=yes;'
    )
