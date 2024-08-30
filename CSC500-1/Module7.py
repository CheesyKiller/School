# Author: Jacob Abts
# Submission Date: 8/29/2024
# CSU Global - CSC500-1

room_numbers = {
    "CSC101" : 3004,
    "CSC102" : 4501,
    "CSC103" : 6755,
    "NET110" : 1244,
    "COM241" : 1411
}

instructors = {
    "CSC101" : "Haynes",
    "CSC102" : "Alvarado",
    "CSC103" : "Rich",
    "NET110" : "Burk",
    "COM241" : "Lee"
}

meeting_times = {
    "CSC101" : 8,
    "CSC102" : 9,
    "CSC103" : 10,
    "NET110" : 11,
    "COM241" : 13
}

course_info = {
    "CSC101" : (3004, "Haynes", 8),
    "CSC102" : (4501, "Alvarado", 9),
    "CSC103" : (6755, "Rich", 10),
    "NET110" : (1244, "Burk", 11),
    "COM241" : (1411, "Lee", 13)
}

def PrintCourseAssigned(course):
    found = False
    for courseID, key in room_numbers.items():
        if (course == courseID):
            time = 12 if (meeting_times[course] % 12) == 12 else (meeting_times[course] % 12)
            time_indicator = "a" if (meeting_times[course] < 12) else "p"
            print(f"\n{course}\nRoom Number: {room_numbers[courseID]}\nInstructor: {instructors[courseID]}\nMeeting Time: {time} {time_indicator}.m.")
            return
    print(f"{course}: Not found!")

def PrintCourseBetter(course):
    info = course_info[course]
    print(f"\n{course}\nRoom Number: {info[0]}\nInstructor: {info[1]}\nMeeting Time: {(12 if (info[2] % 12) == 0 else (info[2] % 12))} {'a' if (info[2] < 12) else 'p'}.m.")

def Main():
    course_name = input("Please enter a course to search: ")
    PrintCourseAssigned(course_name)
    PrintCourseBetter(course_name)

Main()