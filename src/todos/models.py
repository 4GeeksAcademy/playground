import os
import json


class Todo():
    def create_json_file(todo_file_path):
        try:
            file = open(todo_file_path)
            file.close()
            return True

        except Exception as error:
            if error.errno == 2:
                with open(todo_file_path, 'w') as file:
                    json.dump([], file, indent=2)
                    file.close()
                    return True
            else:
                return None

    def get_all_users(todo_file_path):
        with open(todo_file_path, 'r') as file:
            data = json.load(file)
            file.close()
            users = []
            for todo in data:
                users.append(todo.get('username'))

            return users

    def get_all_todo_by_user(todo_file_path, username=None):
        with open(todo_file_path, 'r') as file:
            data = json.load(file)
            file.close()

            if username in Todo.get_all_users(todo_file_path):
                for todo in data:
                    if todo.get('username') == username:
                        # todos.append(todo.get('todo')[0])
                        return todo.get('todo')

            return None

    def update_all_todos_by_user(todo_file_path, username=None, data=None):
        with open(todo_file_path, 'r') as file:
            todos = json.load(file)
            for todo in todos:
                if todo.get('username') == username:
                    todo["todo"] = data
            file.close()

        with open(todo_file_path, 'w') as file:
            json.dump(todos, file, indent=2, ensure_ascii=False)
            file.close()

        return True

    def create_user(todo_file_path, username=None):
        with open(todo_file_path, 'r') as file:
            todos = json.load(file)

            if len(todos) == 0:
                with open(todo_file_path, 'w') as file:
                    todos.append({"username": username, "todo": [
                        {"id": 1, "label": "task 1", "done": False},
                    ]})
                    json.dump(todos, file, indent=2)
                    file.close()
                    return True

            for todo in todos:
                if todo.get("username") == username:
                    return False
                else:
                    with open(todo_file_path, 'w') as file:
                        todos.append({"username": username, "todo": [
                            {"id": 1, "label": "example task", "done": False},
                        ]})
                        json.dump(todos, file, indent=2)
                        file.close()
                    return True

    def delete_user(todo_file_path, username=None):
        with open(todo_file_path, 'r') as file:
            todos = json.load(file)
            for todo in todos:
                if todo.get('username') == username:
                    todos.remove(todo)
                    with open(todo_file_path, 'w') as file:
                        json.dump(todos, file, indent=2)
                        file.close()
                    return True
                else:
                    print("usuario no existe")
                    return False
       

     