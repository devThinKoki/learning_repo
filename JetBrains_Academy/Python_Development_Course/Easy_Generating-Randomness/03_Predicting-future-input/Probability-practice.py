# fl, d = 2.71828, 3
# floating = f":.{d}f"
# print(floating)
# # print(fl.format())
# print("{0:.{1}f}".format(fl,d))

# A: Two cards are pulled from a deck of 52 cards, and both are kings. 
# B: Four cards are pulled from a deck of 52 cards, and all of them are hearts.
print('-'*20, '1', '-'*20)
print('A: ', (4/52)*(3/51) + (4/52)*(3/51))
print('B: ', (13/52)*(12/51)*(11/50)*(10/49))

# A factory produces product X with the probability of defect 0.05 and product Y with the probability of defect 0.02.
# Someone bought one X and one Y.
# A: Exactly one of the purchased products has defects.
# B: Product Y has a defect, and X doesn't have any.
print('-'*20, '2', '-'*20)
print('A: ', 1 - ((0.95*0.98) + (0.05*0.02)))
print('A: ', (0.95*0.02) + (0.05*0.98))
print('B: ', (0.02)*(0.95))


# A: Two dice are rolled, and the parity of the points is different.
# B: A die is rolled, and the number of points isn't divisible by 3.
print('-'*20, '3', '-'*20)
print('A: ', 1 - (6/36))
print('A: ', 6*(1/6)*(5/6))
print('B: ', (4/6))

# A: One card is pulled from a deck of 52 cards, and it's a king or an ace.
# B: Two cards are pulled from a deck of 52 cards, and both are hearts.
print('-'*20, '4', '-'*20)
print('A: ', (4/52) + (4/52))
print('B: ', (13/52) * (12/51))