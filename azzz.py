while True:
    try:
        numName = int(input('Enter the number of names to be added: '))
        
        while numName > 0:
            name = input(f'Enter a name({numName}): ')

            if name.isalpha():
                numName -= 1
                with open('names.txt', 'a') as file:
                    file.write(name.title() + '\n')
            else:
                print('No spaces!!')
        
        print('Names added on the file succesfully!')
        break

    except ValueError:
        print('Enter a valid data!!')