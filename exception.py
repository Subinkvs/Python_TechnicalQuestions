def exception_handling(num):
    try:
        return 100 // num
    except ZeroDivisionError:
        print("Division by Zero is not allowed")
        
    finally:
        print("This block always runs..")
        
        
print(exception_handling(20))