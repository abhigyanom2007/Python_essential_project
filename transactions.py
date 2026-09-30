from storage import sd

def at(d):
    print("\n Add Transaction- ")
    # t = input("type? ")
    t = input("Is this Income or Expense? (Enter I or E): ")

    # manual lower case fix because I kept getting errors
    if t == 'i':
        t = 'I'
    if t == 'e':
        t = 'E'

    if t != 'I' and t != 'E':
        print("Error: Invalid input.")
        # break
        return

    try:
        a = float(input("Enter amount: "))
        # if a < 0: a = a * -1  # tried to auto fix negatives but it caused bugs
    except:
        print("Error!")
        return

    ds = input("Enter a short description: ")

    ty = ""
    if t == 'I':
        ty = "Income"
    if t == 'E':
        ty = "Expense"

    # r = {"type": t, "amount": a, "description": ds}
    r = {
        "type": ty,
        "amount": a,
        "description": ds
    }

    d.append(r)
    sd(d)
    print("saved")

def vt(d):
    print("\n All Transactions ")
    # if len(d) == 0:
    if d == []:
        print("nothing here")

    i = 0
    idx = 0
    flag = True
    while flag:
        if idx == len(d):
            flag = False
        else:
            r = d[idx]
            # print(r)
            print(str(i) + ". " + r["type"] + " | " + str(r["amount"]) + " | " + r["description"])
            i = i + 1
            idx = idx + 1