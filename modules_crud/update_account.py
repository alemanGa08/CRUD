from database.db_conexion import get_connection

def update_account(account_id, fullname, birthdate):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = "{CALL csp_update_account (?, ?, ?)}"
        cursor.execute(sql, (account_id, fullname, birthdate))
        conn.commit()
    finally:
        conn.close()