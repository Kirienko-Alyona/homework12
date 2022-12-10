from requests_for_bot import BOT_COMMANDS

def bot_answer_func(question):
    """
    Функція повертає відповідь бота
    """
    return BOT_COMMANDS.get(question, incorrect_input_func)


def incorrect_input_func():
    """
    Функція корректної обробки невалідних команд для бота
    """
    return ValueError("I don't know this command. Try again.") 


def input_func(input_string):
    """
    Функція відокремлює слово-команду для бота
    """
    command = input_string
    data = ""
    for key in BOT_COMMANDS:
        if input_string.strip().lower().startswith(key):
            command = key
            data = input_string[len(command):]
            break
    if data:
        return bot_answer_func(command)(data)
    
    return bot_answer_func(command)() 
