with open('programming_poll.txt', 'w') as f:
    while True:
        reason = input('Why do you like programming? ').rstrip()
        if reason:
            f.write(f'{reason}\n')
        else:
            break
