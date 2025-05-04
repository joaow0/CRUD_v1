import requests

def header(text):
    print('-=' * 20)
    print(text.center(37))
    print('-=' * 20)

def show_menu(options):
    for index, option in enumerate(options, 1):
        print(f'{index} - {option}')

def handle_options(api_url, option):
    try:
        if option == 1:
            response = requests.get(api_url)
            data = response.json()
            for item in data:
                print(item)

        elif option == 2:
            item_id = int(input('ID: '))
            response = requests.get(f'{api_url}/{item_id}')
            print(response.json())

        elif option == 3:
            new_item = {
                "title": input('Title: '),
                "body": input('Content: '),
                "userId": int(input('User ID: '))
            }
            response = requests.post(api_url, data=new_item)
            print(response)
            print(response.json())

        elif option == 4:
            updated_data = {
                "title": input('New Title: '),
                "body": input('New Content: ')
            }
            item_id = int(input('ID to update: '))
            response = requests.patch(f'{api_url}/{item_id}', data=updated_data)
            print(response)
            print(response.json())

        elif option == 5:
            item_id = int(input('ID to delete: '))
            response = requests.delete(f'{api_url}/{item_id}')
            print(response)

        return "✅ Operation completed successfully!"
    except Exception as error:
        return "❌ ERROR! Check the request and try again."