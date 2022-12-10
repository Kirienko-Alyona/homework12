def input_error(func):
    """
    Декоратор для обробки помилок при виконанні команд бота
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This name is wrong"
        except ValueError as exception:
            return exception.args[0]
        except TypeError:
            return "I don't know this command" 
        except IndexError:
            return "Please, print name and phone"   

    return inner