from random import choices

picks = [str(i) for i in range(1, 11)]
picks.extend(['a', 'b', 'c', 'd', 'e'])
print(choices(picks, k=5), 'wins a price')
