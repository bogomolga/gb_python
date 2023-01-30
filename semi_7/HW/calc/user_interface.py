from logg import logging

def menu():
    while True:
        type_num = input ("Choice\n" \
                          "1 - rr\n" \
                          "2 - dd\n"  \
                          "3 - Exit\n")
        match type_num:
            case "1":
                logging.info('Start program')
                pass
            case "2":
                pass
            case "3":
                logging.info('Stop program')
                break
            case _:
                logging.error('Err')
                print('Err')
