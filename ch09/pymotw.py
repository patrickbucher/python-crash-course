import pwd

print('{:25s} {:25s}'.format('username', 'home directory'))
print('{:25s} {:25s}'.format('-'*25, '-'*25))
for user in pwd.getpwall():
    print('{:25s} {:25s}'.format(user.pw_name, user.pw_dir))
