from json import load


def get_name(username:str):
    named = username.capitalize()
    with open("save_name.json", "w") as nome:
        data = {
            "name":named
        }
        nome.write(data)

def main():
    ...


if __name__ == "__main__":
    main()