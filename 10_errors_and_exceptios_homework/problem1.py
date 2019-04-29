try:
    for i in ['a','b','c']:
        print(i**2)
except Exception as e:
    print(f"An error of type --{e}-- happened.") 
else:
    print("All good...")
finally:
    print("Bye!!!")