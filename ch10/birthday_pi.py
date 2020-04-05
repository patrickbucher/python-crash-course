from file_reader import get_pi

pi = get_pi('pi.txt')
birthdate = input('Enter your birthday, in the form yyyymmdd: ').strip()
if birthdate in pi:
    print(f'Your birthdate appears in the first million digits of pi!')
else:
    print(f'Your birthdate does not appear in the first million digits of pi.')
