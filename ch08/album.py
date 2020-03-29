def make_album(artist, title, number_of_songs=None):
    album = {'artist': artist, 'title': title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album


amolad = make_album('Iron Maiden', 'A Matter of Life and Death')
painkiller = make_album('Judas Priest', 'Painkiller')
atg = make_album('Fates Warning', 'Awaken the Guardian')
rib = make_album('Slayer', 'Reign in Blood', number_of_songs=10)

print(amolad)
print(painkiller)
print(atg)
print(rib)
