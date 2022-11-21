print("Amount Due: 50")
amount_due = 50
coins_added = 0
while True:
    insert_coin = int(input("Insert Coin: "))

    if insert_coin == 25 or insert_coin == 10 or insert_coin == 5:
        amount_due = amount_due - insert_coin
        coins_added += insert_coin

    if coins_added >= 50:
        print("Change owed:", coins_added - 50)
        break
    else:
        print("Amount Due:", amount_due)
