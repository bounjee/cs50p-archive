banker_greet = input("Greeting: ")

if banker_greet == '"How you doing?"' or banker_greet == "How you doing?":
    print("$20")
elif banker_greet == "\"What's happening?\"" or banker_greet == "\"What's up?\"" or banker_greet == "What's happening?" or banker_greet == "What's up?":
    print("$100")
else:
    print("$0")
# pset açıklamasını okuyun.