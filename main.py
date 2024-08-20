import importlib
import inspect
import os

def load_functions():
    functions = {}
    functions_dir = 'functions'
    for file in os.listdir(functions_dir):
        if file.endswith(".py"):
            module_name = file[:-3]
            module = importlib.import_module(f"{functions_dir}.{module_name}")
            for name, func in inspect.getmembers(module, inspect.isfunction):
                functions[name] = func
    return functions

def main():
    functions = load_functions()
    
    while True:
        print("\nMenu:")
        for i, func_name in enumerate(functions.keys(), 1):
            print(f"{i}. {func_name}")
        print(f"{len(functions) + 1}. Exit")
        
        choice = input("Enter your choice: ")
        
        try:
            choice = int(choice)
            if choice == len(functions) + 1:
                break
            func_name = list(functions.keys())[choice - 1]
            func = functions[func_name]
            
            # Get function parameters
            params = inspect.signature(func).parameters
            args = []
            for param in params.values():
                arg = input(f"Enter value for {param.name}: ")
                args.append(arg)
            
            # Call the function with the provided arguments
            result = func(*args)
            print(f"Result: {result}")
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()