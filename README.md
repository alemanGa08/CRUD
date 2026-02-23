# CRUD `tbl_account`

Una **aplicación de consola** en Python para ejecutar operaciones CRUD  
(Crear, Leer, Actualizar y Eliminar) sobre una tabla en SQL Server Express.  
Se emplean *procedimientos almacenados* y una conexión ODBC.

---

## 📁 Estructura del proyecto

```
CRUD/
├── main.py
├── database/
│   ├── db_conexion.py
│   └── BD_CRUD.sql
└── modules_crud/
    ├── create_account.py
    ├── read_account.py
    ├── update_account.py
    └── delete_account.py
```

---

## 🛠 Requisitos

- **Sistema operativo:** Windows
- **Python:** 3.x
- **Servidor de datos:** SQL Server Express
- **Librería:** `pyodbc`  
  ```bash
  pip install pyodbc
  ```

---

## 🗄️ Base de datos

La base de datos es obligatoria para ejecutar el proyecto.

1. Crear la base de datos:
   ```sql
   CREATE DATABASE users;
   ```
2. Ejecutar `BD_CRUD.sql` para crear:
   - Tabla `tbl_account`
   - Procedimientos almacenados CRUD

---

## 🔌 Conexión

Configura la cadena de conexión en `database/db_conexion.py` según tu instancia
 de SQL Server Express.

---

## ▶️ Ejecución

Desde la raíz del proyecto:

```bash
python main.py
```

Se mostrará un menú interactivo en consola para gestionar las cuentas.

---

## ℹ️ Notas

- El proyecto **no funciona sin la base de datos**.
- SQL Server Express debe estar en ejecución.
- Diseñado para un entorno Windows.

---

© Proyecto **CRUD** | Python + SQL Server Express