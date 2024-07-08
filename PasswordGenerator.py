import random
import string

print("""     
^^:  ^^:  ^^: .^^: .^^.:7JJ?77??777?J?77?J?77?J?77?J?77???77?J?77?J?77?J????!. .^^:  ^^:  ^^: .^^:  
  :^^. :^^. :^^. :^^ ^YY7: .^:.77^:. .^:. .??. :::  :^:77::^  .^:  .^:  .^~~J5!:. :^^. :^^. :^^. :^^
^^:..:^:..:^:..:^:..!G! .::~GP?#B?PP^. ^PP?B#?5P^ :^PP?B#?PG~::..::...:^:..::!G!:^:..:^:..:^:..:^:..
..:::..:::..:::..:::G7.::.~?5#####B5J~^?5B#####5?~~J5######5J~.:..:^^^:..::...7G:.:::..:::..:::..:::
..:::..:::..:::..::^B~.::.755B####BPP!!5PB#####PY!!P5B####B5P7.:7YGGGBPJ^::...!B:.:::..:::..:::..:::
^^:..:^:..:^:..:^:..?G^ .::~GB5#B5BP~. ^PBYB#5GG^ :~PB5B#5BG~:.?#G7^:~J#B~ ::^P?:^:..:^:..:^:..:^:..
  :^^. :^^. :^^. :^^ 7PJ~. .!^:5Y^~: .^:^::Y5..~^:  ^~^YY^~~  :B#! .:: 5&5::75?:. :^^. :^^. :^^. :^^
^^: .^^: .^^: .^^: .^^:!JYJ7~~77!~~77!~~77!~~77!~~77!~~77!~~77!G#J7!~~!5#5?Y?^  ^^: .^^: .^^: .^^:  
. :^^. :^^. :^^. :^^. :::.:~77~~!77~~!77~~!77~~!77~~!77~~!77~7JB#J?JYJ?P#P!: :^^. :^^. :^^. :^^. :^^
:::..:::..:::..:::..:::..::...::...::...::...::...::...::.. !BB###BB#BB####G^...:::..:::..:::..:::..
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::.?#######B######B^.::::::::::::::::::::::
..:::..:::..:::..:::..:::..:::..:::..:::..:::..:::..:::..:::7#####B!^?#####B^.::..:::..:::..:::..:::
^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^:  ?######^ ?#####B~. .^^: .^^: .^^: .^^:  
  :^^  :^^  :^^  :^^  :^^  :^^  :^^  :^^  :^^  :^^  :^^  :^:7######Y7G#####B:.^^  :^^  :^^  :^^  :^^
^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^: .^^:  !PGGGGGGGGGGGGG5^: .^^: .^^: .^^: .^^:  
""")

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                print("Please enter a positive integer.")
            else:
                return length
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")

def include_letters():
    response = input("Include letters (y/n)? ").lower()
    return response == "y"

def include_symbols():
    response = input("Include symbols (y/n)? ").lower()
    return response == "y"

def generate_secure_password(length, use_letters, use_symbols):
    characters = ""
    if use_letters:
        characters += string.ascii_letters
    if use_symbols:
        characters += string.digits + string.punctuation

    if not characters:
        print("Error: You must include either letters or symbols.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = get_password_length()
    use_letters = include_letters()
    use_symbols = include_symbols()

    secure_password = generate_secure_password(password_length, use_letters, use_symbols)
    if secure_password:
        print("Secure Password:", secure_password)
