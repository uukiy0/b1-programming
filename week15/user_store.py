import sqlite3


#UserStore does all database operations related to users
#encapsulates SQLite logic so API routes remain clean
class UserStore:

    #constructor
    #accepts a database path and initializes database
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.init_db()  #make sure table exists when the class is created

    #creates the users table if it does not already exist
    #method runs automatically when application starts
    def init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            #create users table with id, name, and email
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL
                )
            """)

            #Save changes to the database
            conn.commit()

    #Retrieves all users from the database
    #Returns a list of dictionaries
    def load(self) -> list[dict]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            #Fetch all rows from users table
            cursor.execute("SELECT id, name, email FROM users")
            rows = cursor.fetchall()

            #Convert each row into a dictionary
            return [
                {"id": row[0], "name": row[1], "email": row[2]}
                for row in rows
            ]

    #inserts a new user into the database
    #Accepts a dictionary containing name and email
    def save(self, user: dict) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            #Insert new user record
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (user["name"], user["email"])
            )

            conn.commit()

    #Finds a user by their ID
    # Returns a dictionary if found otherwise None
    def find_by_id(self, user_id: int) -> dict | None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            #Query database for specific user ID
            cursor.execute(
                "SELECT id, name, email FROM users WHERE id = ?",
                (user_id,)
            )

            row = cursor.fetchone()

            #If a row is found then convert to dictionary
            if row:
                return {"id": row[0], "name": row[1], "email": row[2]}

            #If no user found return None
            return None

    #Updates an existing user by ID
    #Returns True if update was successful, otherwise False.
    def update_user(self, user_id: int, updated_data: dict) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            #update user record
            cursor.execute(
                "UPDATE users SET name = ?, email = ? WHERE id = ?",
                (updated_data["name"], updated_data["email"], user_id)
            )

            conn.commit()

            # rowcount > 0 means a record was updated
            return cursor.rowcount > 0

    #deletes a user by ID.
    #Returns True if deletion was successful or else False.
    def delete_user(self, user_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            #delete user record
            cursor.execute(
                "DELETE FROM users WHERE id = ?",
                (user_id,)
            )

            conn.commit()

            #rowcount > 0 means a record was deleted
            return cursor.rowcount > 0