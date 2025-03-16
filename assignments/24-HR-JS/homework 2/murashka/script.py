
starting_sum = float(input("Увядзіце пачатковую суму: "))
interest_rate = float(input("Увядзіце стаўку працэнтаў (у адсотках): "))
investment_period = float(input("Увядзіце перыяд інвеставання (у гадах): "))


interest_rate_decimal = interest_rate / 100

resulting_sum = starting_sum * ((1 + interest_rate_decimal) ** investment_period)

print(f"Па заканчэнні {investment_period} гадоў, з стаўкай працэнтаў {interest_rate}%, у вас будзе {resulting_sum:.2f}")
