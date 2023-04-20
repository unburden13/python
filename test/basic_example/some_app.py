def do_stuff(num=0):
    try:
        if num:
            return 5 + int(num)
        else:
            return 'please enter a number'
    except ValueError as err:
        return err
