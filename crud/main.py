from crud.module.requests0 import *
from time import sleep

while True:
    header("CRUD SYSTEM")
    show_menu([
        "View all items",
        "View item by ID",
        "Create new item",
        "Update item",
        "Delete item",
        "EXIT"
    ])
    try:
        choice = int(input('Choose an option: '))
        if choice == 6:
            print('Exiting system...')
            break
        else:
            print(handle_options("https://jsonplaceholder.typicode.com/posts", choice))
            sleep(2)
    except ValueError:
        print('⚠️ Please enter a valid number.')