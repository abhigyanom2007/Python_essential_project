from storage import ld
from transactions import at, vt
from analytics import cb
# import sys

def m():
    print("Welcome to your Mini Budget CLI program")

    # data = load_data()
    d = ld()

    run = True
    while run:
        print("\n Main Menu ")
        print("1. Add a Transaction")
        print("2. View All Transactions")
        print("3. Check Balance")
        print("4. Exit App")

        c = input("Enter your choice (1-4): ")

        if c == '1':
            at(d)
        if c == '2':
            vt(d)
        if c == '3':
            cb(d)
        if c == '4':
            print("Exiting app....")
            # exit(0)
            run = False

        # if c > '4' or c < '1':
        if c != '1' and c != '2' and c != '3' and c != '4':
            print("Invalid choice")

if __name__ == "__main__":
    m()