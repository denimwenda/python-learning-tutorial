sandwich_orders = ['supa', 'festive', 'county']
finished_sandwiches = []

while sandwich_orders:
    current_user = sandwich_orders.pop()

    print("every bread has being made: " + current_user.title())
    finished_sandwiches.append(current_user)

    print("\nThe following sandwiches has been baked:")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich.title())
