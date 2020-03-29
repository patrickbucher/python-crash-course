def show_messages(messages):
    printed_messages = []
    for message in messages:
        print(message)
        printed_messages.append(message)
    return printed_messages


messages = ['Hi', 'Hello', 'How are you', 'Nice weather!']
printed_messages = show_messages(messages)
print(printed_messages)
