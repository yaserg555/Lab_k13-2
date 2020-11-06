def input_number(a, b):
    try:
        if not a <= (x := float(input('Enter value: '))) <= b:
            print('wrong input')
            input_number(a, b)
        return x
    except ValueError:
        print('wrong input')
        input_number(a, b)
