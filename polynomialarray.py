# Function to input a polynomial from the user
def input_polynomial(num):
    n = int(input(f"Enter the highest power of polynomial {num}: "))
    poly = []
    print(f"Enter coefficients from x^0 to x^{n}:")
    for i in range(n + 1):
        coeff = int(input(f"Coefficient of x^{i}: "))
        poly.append(coeff)
    return poly

# Function to display polynomial in readable format
def display_polynomial(poly):
    terms = []
    for power in range(len(poly) - 1, -1, -1):
        coeff = poly[power]
        if coeff != 0:
            if power == 0:
                terms.append(f"{coeff}")
            elif power == 1:
                terms.append(f"{coeff}x")
            else:
                terms.append(f"{coeff}x^{power}")
    return " + ".join(terms) if terms else "0"

# Function to add two polynomials
def add_polynomials(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    poly1 += [0] * (max_len - len(poly1))
    poly2 += [0] * (max_len - len(poly2))
    return [poly1[i] + poly2[i] for i in range(max_len)]

# Function to subtract two polynomials
def subtract_polynomials(poly1, poly2):
    max_len = max(len(poly1), len(poly2))
    poly1 += [0] * (max_len - len(poly1))
    poly2 += [0] * (max_len - len(poly2))
    return [poly1[i] - poly2[i] for i in range(max_len)]

# Function to multiply two polynomials
def multiply_polynomials(poly1, poly2):
    result = [0] * (len(poly1) + len(poly2) - 1)
    for i in range(len(poly1)):
        for j in range(len(poly2)):
            result[i + j] += poly1[i] * poly2[j]
    return result

# ---------------- Main Program ----------------
print("=== Polynomial Operations ===\n")

# Input polynomials
poly1 = input_polynomial(1)
poly2 = input_polynomial(2)

while True:
    print("\nSelect Operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        result = add_polynomials(poly1.copy(), poly2.copy())
        print("\nSum =", display_polynomial(result))
    elif choice == '2':
        result = subtract_polynomials(poly1.copy(), poly2.copy())
        print("\nDifference =", display_polynomial(result))
    elif choice == '3':
        result = multiply_polynomials(poly1.copy(), poly2.copy())
        print("\nProduct =", display_polynomial(result))
    elif choice == '4':
        print("\nExiting... Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
        