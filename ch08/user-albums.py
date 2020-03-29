def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist, 'title': title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album


def is_quit_input(entered):
    return entered.strip().lower() == 'quit'


quit_message = 'Enter «quit» to finish'
while True:

    artist = input(f'Please enter the album artist ({quit_message}): ')
    if is_quit_input(artist):
        break

    title = input(f'Please enter the album title ({quit_message}): ')
    if is_quit_input(title):
        break

    album = make_album(artist, title)
    print(album)
