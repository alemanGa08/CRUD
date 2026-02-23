from modules_crud.create_account import * 
from modules_crud.read_account import * 
from modules_crud.update_account import * 
from modules_crud.delete_account import * 
from datetime import datetime
import os 

def clear_screen():
    os.system('cls')

def menu():
    while True: 
        try:
            print("\n--- CRUD TBL_ACCOUNT ---")
            print("1. Crear cuenta")
            print("2. Leer cuentas")
            print("3. Actualizar cuenta")
            print("4. Eliminar cuenta")
            print("5. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                fullname = input("Nombre completo: ")
                birthdate = input("Fecha de nacimiento (YYYY-MM-DD): ")

                try:
                    datetime.strptime(birthdate, "%Y-%m-%d")
                except ValueError:
                    print("Formato de fecha inválido. Usa YYYY-MM-DD.")
                    input("Presiona Enter para continuar...")
                    clear_screen()
                    continue

                create_account(fullname, birthdate)
                print("Cuenta creada correctamente.")

            elif opcion == "2":
                cuentas = read_accounts()
                for row in cuentas:
                    print(row)

            elif opcion == "3":
                account_id_input = input("ID de la cuenta a actualizar: ")

                if not account_id_input.isdigit():
                    print("El ID debe ser un número.")
                    input("Presiona Enter para continuar...")
                    clear_screen()
                    continue

                account_id = int(account_id_input)
                fullname = input("Nuevo nombre completo: ")
                birthdate = input("Nueva fecha de nacimiento (YYYY-MM-DD): ")

                try:
                    datetime.strptime(birthdate, "%Y-%m-%d")
                except ValueError:
                    print("Formato de fecha inválido. Usa YYYY-MM-DD.")
                    input("Presiona Enter para continuar...")
                    clear_screen()
                    continue

                update_account(account_id, fullname, birthdate)
                print("Cuenta actualizada correctamente.")
        
            elif opcion == "4":
                account_id_input = input("ID de la cuenta a eliminar: ")

                if not account_id_input.isdigit():
                    print("El ID debe ser un número.")
                    input("Presiona Enter para continuar...")
                    clear_screen()
                    continue

                account_id = int(account_id_input)
                delete_account(account_id)
                print("Cuenta eliminada correctamente.")

            elif opcion == "5":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")
            
            input("Presiona Enter para continuar")     
            clear_screen()
        
        except Exception:
            print("Ocurrió un error inesperado. Revisa los datos ingresados.")
            input("Presiona Enter para continuar...")
            clear_screen()

if __name__ == "__main__":
    menu()