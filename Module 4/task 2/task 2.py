# Try-Except block to catching errors with file
try:
    def get_cats_info(path):
        # Init list for dictionaries
        cats_info = []
        with open(path, 'r', encoding='utf-8') as file:
            # Loop for reading the file line by line and appending data from lines
            for line in file:
                line = line.strip('\n')
                cat_info = line.split(',')
                cats_info.append({'id:': cat_info[0], 'name':cat_info[1], 'age':cat_info[2]}) 
        return cats_info     
except FileNotFoundError:
    print("Error: File not founded")
except IOError:
    print("Error: Could not read file")
print(get_cats_info('cats.txt'))