from database.db_conexion import get_connection

def delete_account(account_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("{CALL csp_delete_account (?)}", (account_id,))
    conn.commit()
    conn.close()
