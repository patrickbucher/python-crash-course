from random import choices

picks = [str(i) for i in range(1, 11)]
picks.extend(['a', 'b', 'c', 'd', 'e'])

my_ticket = choices(picks, k=5)

tries = 0
lottery = []
while my_ticket != lottery:
    lottery = choices(picks, k=5)
    tries += 1
print(f'it took {tries} tries')
