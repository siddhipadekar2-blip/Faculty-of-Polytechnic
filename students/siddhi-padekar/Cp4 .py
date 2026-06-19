#problem1
def print_menu():
    print("MENU ")
    print("1. Add Subject")
    print("2. View Report")
    print("3. Clear Data")
    print("4. Exit")
print_menu()

#problem2

def print_h(h):
    if len(h) == 0:
        print("No h yet.")
    else:
        print(" Session H ")
        for i in range(len(h)):
            print(f"[{i + 1}] {h[i]}")
        print("-")

h = ["Added 1 subject(s)", "Viewed report"]

print_h(h)
