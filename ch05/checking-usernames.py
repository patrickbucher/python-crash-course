current_users = ['alice', 'bob', 'mallory', 'admin', 'postgres']
new_users = ['Alice', 'Mallory', 'Harald', 'Bernhard', 'Hermann']

current_users_lowercase = []
for current_user in current_users:
    current_users_lowercase.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lowercase:
        print(f'{new_user}, you need to enter another user name')
    else:
        print(f'the username {new_user} is still available')
