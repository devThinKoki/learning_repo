conicoin = int(input("Please, enter the number of conicoins you have:\n"))
# > 128
rate = input("Please, enter the exchange rate:\n")
if '.' in rate:
    rate = float(rate)
else:
    rate = int(rate)
#  > 3.21
print(f"The total amount of dollars: {conicoin * rate}")
# The total amount of dollars: 410.88