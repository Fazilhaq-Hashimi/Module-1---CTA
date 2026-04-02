def main():
    # Dictionary for Room Numbers
    rooms = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }

    # Dictionary for Instructors
    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }

    # Dictionary for Meeting Times
    times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }

    # Get user input
    course_id = input("Enter a course number (e.g., CSC101): ").strip()

    # Problem Solving: Check if the course exists before displaying
    if course_id in rooms:
        print(f"\nDetails for Course {course_id}:")
        print(f"Room Number: {rooms[course_id]}")
        print(f"Instructor:  {instructors[course_id]}")
        print(f"Meeting Time: {times[course_id]}")
    else:
        print(f"\nError: Course '{course_id}' was not found in our records.")

if __name__ == "__main__":
    main()
