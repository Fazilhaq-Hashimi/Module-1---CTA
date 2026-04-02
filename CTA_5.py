# Part 1: Average Rainfall Calculation
def average_rainfall():
    print("--- Part 1: Rainfall Tracker ---")
    total_rainfall = 0.0
    
    # Ask for number of years
    num_years = int(input("Enter the number of years: "))
    
    # Outer loop for years
    for year in range(1, num_years + 1):
        print(f"\nYear {year}:")
        # Inner loop for 12 months
        for month in range(1, 13):
            inches = float(input(f"  Enter inches of rainfall for month {month}: "))
            total_rainfall += inches
            
    # Calculations
    total_months = num_years * 12
    average_rain = total_rainfall / total_months
    
    # Display results
    print("\n--- Results ---")
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rain:.2f}")


# Part 2: Bookstore Points System
def bookstore_points():
    print("\n--- Part 2: Bookstore Points ---")
    books = int(input("Enter the number of books purchased this month: "))
    
    # Logic for points
    if books >= 8:
        points = 60
    elif books >= 6:
        points = 30
    elif books >= 4:
        points = 15
    elif books >= 2:
        points = 5
    else:
        points = 0
        
    print(f"You earned {points} points this month!")


# Main execution
if __name__ == "__main__":
    average_rainfall()
    bookstore_points()
