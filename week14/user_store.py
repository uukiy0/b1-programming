import json


#UserStore class handles all file based data persistence.
#encapsulates loading, saving, updating, and deleting users
#so that file logic is separated from the API routes.
class UserStore:
    
    #Constructor receives the file path where users are stored
    def __init__(self, file_path: str):
        self.file_path = file_path

    #Load users from the file
    #Returns a list of user dictionaries
    #If the file does not exist return empty list
    def load(self) -> list[dict]:
        users = []
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                for line in file:
                    # Each line is a JSON object (JSON lines format)
                    users.append(json.loads(line.strip()))
        except FileNotFoundError:
            #If file doesnt exist yet return empty list
            return []
        return users

    #Save users to the file
    #Writes one JSON object per line ,JSON lines format
    def save(self, users: list[dict]) -> None:
        with open(self.file_path, "w", encoding="utf-8") as file:
            for user in users:
                file.write(json.dumps(user) + "\n")

    # Find a user by ID
    # Returns the user dictionary if found, otherwise None
    def find_by_id(self, user_id: int) -> dict | None:
        users = self.load()
        for user in users:
            if user["id"] == user_id:
                return user
        return None

    # Update an existing user by ID
    # Returns True if successful, False if user not found
    def update_user(self, user_id: int, updated_data: dict) -> bool:
        users = self.load()
        for i, user in enumerate(users):
            if user["id"] == user_id:
                # Update only the provided fields
                users[i].update(updated_data)
                self.save(users)
                return True
        return False

    #Delete a user by ID
    #Returns True if deletion occurred, False if user not found.
    def delete_user(self, user_id: int) -> bool:
        users = self.load()

        #Create a new list excluding the user to delete
        new_users = [user for user in users if user["id"] != user_id]

        #If length didnt change, user wasnt found
        if len(new_users) == len(users):
            return False

        self.save(new_users)
        return True