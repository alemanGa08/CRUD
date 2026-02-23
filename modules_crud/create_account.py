from database.db_conexion import get_connection

def create_account(fullname, birthdate):
    conn = get_connection()
    cursor = conn.cursor()
    # Asegurar que el procedimiento almacenado acepte los parámetros en el orden correcto
    cursor.execute("{CALL csp_create_account (?, ?)}", (fullname, birthdate))
    conn.commit()
    conn.close()