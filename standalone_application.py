import json
import os

DATA_FILE = "employees.json"

def load_employees():
    """Load employee data from file"""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_employees(employees):
    """Save employee data to file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(employees, f, indent=4)

def clear_screen():
    """Cross-platform screen clearing"""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_employee():
    """Create new employee with validation"""
    employees = load_employees()
    
    while True:
        try:
            clear_screen()
            print("--- Create Employee ---")
            name = input("Enter employee name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty")
            
            age = int(input("Enter employee age: "))
            if age < 18 or age > 65:
                raise ValueError("Age must be between 18 and 65")
            
            designation = input("Enter designation (programmer/manager/tester): ").lower()
            if designation not in ['programmer', 'manager', 'tester']:
                raise ValueError("Invalid designation! Must be programmer, manager, or tester")
            
            # Set base salary
            base_salaries = {'programmer': 25000, 'manager': 30000, 'tester': 20000}
            salary = base_salaries[designation]
            
            employees.append({
                'name': name,
                'age': age,
                'designation': designation,
                'salary': salary,
                'original_salary': salary
            })
            
            save_employees(employees)
            print(f"\nEmployee {name} created!")
            
            while True:
                cont = input("\nAdd another? (yes/no): ").lower().strip()
                if cont == 'no':
                    return
                elif cont == 'yes':
                    break
                print("Please enter 'yes' or 'no'")
                    
        except ValueError as e:
            print(f"\nError: {e}")
            input("Press Enter to retry...")
        except Exception as e:
            print(f"\nUnexpected error: {e}")
            return

def display_employees():
    """Display all employees"""
    clear_screen()
    employees = load_employees()
    
    if not employees:
        print("No employees found!")
        return
        
    print("--- Employee List ---")
    for emp in employees:
        hike = ((emp['salary'] - emp['original_salary']) / emp['original_salary']) * 100
        print(f"""
        Name: {emp['name']}
        Age: {emp['age']}
        Designation: {emp['designation'].title()}
        Salary: ₹{emp['salary']:,.2f}
        Hike: {hike:.1f}%
        """)

def raise_salary():
    """Raise salary with 30% max limit"""
    clear_screen()
    employees = load_employees()
    
    if not employees:
        print("No employees found!")
        return
        
    print("--- Raise Salary ---")
    name = input("Enter employee name: ").strip()
    
    for emp in employees:
        if emp['name'].lower() == name.lower():
            print(f"\nCurrent salary: ₹{emp['salary']:,.2f}")
            
            try:
                percent = float(input("Enter hike % (max 30): "))
                if not 0 <= percent <= 30:
                    print("Hike must be 0-30%")
                    return
                
                emp['salary'] = round(emp['salary'] * (1 + percent/100), 2)
                save_employees(employees)
                print(f"\n✅ New salary: ₹{emp['salary']:,.2f}")
            except ValueError:
                print("Invalid percentage!")
            return
    
    print("Employee not found!")

def run_app():
    while True:
        clear_screen()
        print("""
        Employee Management System
        ----------------------------
        1. Create Employee
        2. Display Employees
        3. Raise Salary
        4. Exit
        """)
        
        choice = input("Select option (1-4): ").strip()
        
        if choice == '1':
            create_employee()
        elif choice == '2':
            display_employees()
            input("\nPress Enter to continue...")
        elif choice == '3':
            raise_salary()
            input("\nPress Enter to continue...")
        elif choice == '4':
            print("\nThank you for using the system!")
            break
        else:
            print("Invalid choice!")
            input("Press Enter to retry...")

if __name__ == "__main__":
    run_app()