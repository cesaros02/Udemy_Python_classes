
def ask():
    while True:
        
        try:
            number = int(input("Enter an integer: ")) 
        except Exception as e:
            print(f"Error of type --{e}-- happened. Try again...")
            continue
        else:
            print(f"Square of number is {number**2}")
            break
        


if __name__ == "__main__":
    ask()