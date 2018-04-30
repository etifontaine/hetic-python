# This function count the number of each characters in a string
def countChar():
    prompt = 'Phrase à compter : '
    my_text = None
    my_characters = {};

    while  not isinstance(my_text, str):
        try:
            my_text = str(input(prompt))
        except:
            print('\nVous n\'avez pas rentré une chaîne de charactères.')
            prompt = 'Entrez le numéro que vous voulez multiplier'
        else:
            for i in my_text:
                if i in my_characters.keys():
                    my_characters[i] += 1
                else:
                    if i != ' ' and i != ',' and i != '\'':
                        my_characters[i] = 1
            result = 'Le caractère "{0}" apparaît {1} fois.'
            for char, occur in my_characters.items():
                print(result.format(char, occur))


# This function return the multiplication table 
# between 0 and 10 from a given number
def multiplication():
    prompt = 'Table de multiplication voulue : '
    x = None

    while  not isinstance(x, int):
        try:
            x = int(input(prompt))
        except:
            print('\nVous n\'avez pas rentré un entier')
            prompt = 'Entrez le numéro que vous voulez multiplier'
        else:
            print('\nVoici la table de {0}'.format(x))
            for i in range(0, 11):
                print('{0} * {1} = {2}'.format(x, i, x*i))
        print('\nEt voila !')

# Test list
x = [element for element in range(20) if element % 2 == 0]
print(x)