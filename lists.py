cursuri = ['Mate', 'fizica', 'chimie']
nrs = [1, 5, 2, 4, 3]
# slicing
print(cursuri[:])
print(cursuri[1:])
print(cursuri[:-1])

#functii
cursuri.append('desen')
print(cursuri)

cursuri.insert(0, 'desen')
print(cursuri)




cursuri_2 = ['python', 'c++']
cursuri.extend(cursuri_2)
print(cursuri)

cursuri.remove('Mate')
print(cursuri.pop()) # returneaza valoarea eliminata
print(cursuri)


cursuri.reverse()
print(cursuri)

cursuri.sort() # modifica in place
print(cursuri)

cursuri.sort(reverse=True)
print(cursuri)

cursuri_sortate_invers = sorted(cursuri, reverse=True)
print(cursuri_sortate_invers)


print(min(nrs))
print(max(nrs))
print(sum(nrs))


print(cursuri.index('desen'))
print('desen' in cursuri)


for curs in cursuri:
    # print(curs)
    print(curs, end=' ')