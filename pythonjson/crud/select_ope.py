def select_data():
    """select operation of crud"""
    with open('data/user.json') as file:
        data = file.read()

    print(data)
    print("data has been successfully selected")
    return True
    
