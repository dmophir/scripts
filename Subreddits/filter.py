output = []
with open('filteredSubs.txt', 'r') as subs:
    for sub in subs:
        output.append(sub.split('|')[0] + '\n')

with open('subs.txt', 'w') as new_subs:
    for sub in output:
        new_subs.write(sub)
