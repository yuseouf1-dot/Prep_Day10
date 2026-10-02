def read_line(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
                
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")

read_line("zen.txt")        