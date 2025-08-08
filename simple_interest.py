def calculate_simple_interest(principal, rate, time):
    """
    Calculate Simple Interest.

    Formula: (Principal * Rate * Time) / 100
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter rate of interest: "))
    t = float(input("Enter time (in years): "))
    
    interest = calculate_simple_interest(p, r, t)
    print(f"Simple Interest = {interest}")
