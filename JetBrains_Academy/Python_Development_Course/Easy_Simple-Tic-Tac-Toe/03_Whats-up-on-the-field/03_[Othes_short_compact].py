n = input("Enter cells: ")
print("-" * 9)
print("| " + ' '.join(n[0:3]) + " |")
print("| " + ' '.join(n[3:6]) + " |")
print("| " + ' '.join(n[6:9]) + " |")
print("-" * 9)

# dictionary with the total number of  of X, O and _ entries
x_o = {i:n.count(i) for i in set(n)}

# all possibly winning combinations
combs = [ n[0:3], n[3:6], n[6:9], n[::3], n[1::3], n[2::3], n[::4], n[2:7:2]]

# check if there is any 'XXX' in the rows
cond_1 = any(comb == 'X'*3 for comb in combs)
# check if there is any 'OOO' in the rows
cond_2 = any(comb == 'O'*3 for comb in combs)

if cond_1 and cond_2 or abs(x_o['X'] - x_o['O']) > 1:
    print("Impossible")
elif cond_1:
    print("X wins")
elif cond_2:
    print("O wins")
elif not cond_1 and not cond_2 and ( x_o.get('_') != None ):
    print("Game not finished")
else:
    print("Draw")