# Try-Except block to catching errors with file
try:
    def total_salary(path):
        # Introducing variables to calculate total and avarage salary, count of workers
        total = 0
        avarage = 0
        workers_counter = 0
        with open (path, "r", encoding="utf-8") as file:
            # Loop for reading the file line by line and working with the introduced variables
            for line in file:
                line.strip('\n')
                workers_salary = line.split(',')
                total += int(workers_salary[1].strip())
                workers_counter += 1
        avarage = int(total/workers_counter)
        return total,avarage
        
                
    total, average = total_salary("salary.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
except FileNotFoundError:
    print("Error: File not founded")
except IOError:
    print("Error: Could not read file")