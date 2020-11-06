def input_number(a, b):
    try:
        if a <= (x := int(input('Enter value: '))) <= b:
            return x
        else:
            print('wrong input')
            input_number(a, b)
    except ValueError:
        print('wrong input')
        input_number(a, b)
        
