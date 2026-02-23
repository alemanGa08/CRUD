from database.db_conexion import get_connection

def read_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("{CALL csp_read_account}")
    rows = cursor.fetchall()
    conn.close()
    return rows