try:
    z = 5/0
except Exception as e:
    print(f"Error type --{e}-- found...")
else:
    print("all good")
finally:
    print ("All Done.")