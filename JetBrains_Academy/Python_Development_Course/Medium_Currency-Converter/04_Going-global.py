conicoin = round(float(input()), 1)

rates = {"RUB": 2.98, "ARS": 0.82, "HNL": 0.17, "AUD": 1.9622, "MAD": 0.208}
for country, rate in rates.items():
    result = "{:.2f}".format(conicoin * rate)
    print(f"I will get {result} {country} from the sale of {conicoin} conicoins.")

# RUB – Russian Ruble; 1 conicoin = 2.98 RUB;
# ARS – Argentine Peso; 1 conicoin = 0.82 ARS;
# HNL – Honduran Lempira; 1 conicoin = 0.17 HNL;
# AUD – Australian Dollar; 1 conicoin = 1.9622 AUD;
# MAD – Moroccan Dirham; 1 conicoin = 0.208 MAD.
#         > 3.5
# I will get 10.43 RUB from the sale of 3.5 conicoins.
# I will get 2.87 ARS from the sale of 3.5 conicoins.
# I will get 0.6 HNL from the sale of 3.5 conicoins.
# I will get 6.87 AUD from the sale of 3.5 conicoins.
# I will get 0.73 MAD from the sale of 3.5 conicoins.