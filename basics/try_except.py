while True:  # to keep displaying an input if failed
    try:
        number = int(input('Enter a number: '))
        div = 6/number
        print(number)
        # raise ValueError('Custom error here')
    except ZeroDivisionError as err:
        print(err)
    except ValueError:
        print('Invalid input')
    # except (ZeroDivisionError, ValueError)
    except:
        print('Error')
    else:
        print('done')
        break  # exit the input loop
    finally:
        print('end of current flow')
