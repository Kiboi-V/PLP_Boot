#file handling
#writing
try:
    with open('file.txt','w') as f:
        f.write('Hello pythonista.\n')
        f.write('welcome to file handling.\n')
        f.write('good luck in handling files.\n')

except PermissionError:
    print('permission not granted')
except Exception as e:
    print('an error occurred',str(e))
#reading
try:
    with open('file.txt','r') as f:
        print(f.read())

except FileNotFoundError:
    print('Sorry, not found')

except PermissionError:
    print('Permission not granted')
except Exception as e:
    print('an error occurred',str(e))
#append
try:
    with open('file.txt','a') as f:
        f.write('So you managed to read me.\n')
        f.write('Congratulations man.\n')
        f.write('good job.\n')
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", str(e))

# File Reading and Display 
try:
    with open('my_file.txt', 'r') as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", str(e))
