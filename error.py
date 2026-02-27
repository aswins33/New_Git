num=[34,"aswin",43,11]
try:
    print(num1)
except ValueError:
    print("Error: Please enter a valid number.")
except IndexError:
    print("Index position  not found")
except TypeError:
    print("Please provide correct values")
except Exception as e:
    print("error",e)
else:
    print("successfull")
finally:
    print("execution complete")