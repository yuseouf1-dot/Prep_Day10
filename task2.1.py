read_file = open("primes.txt", "r")

def read_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
                
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

read_file("primes.txt")