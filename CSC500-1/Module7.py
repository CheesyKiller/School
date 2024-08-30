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
            print(f"\n{course}\nRoom Number: {room_numbers[courseID]}\nInstructor: {instructors[courseID]}\nMeeting Time: {meeting_times[courseID]}")
            return
    print(f"{course}: Not found!")

def PrintCourseBetter(course):
    info = course_info[course]
    print(f"\n{course}\nRoom Number: {info[0]}\nInstructor: {info[1]}\nMeeting Time: {info[2]}")

def Main():
    course_name = input("Please enter a course to search: ")
    PrintCourseAssigned(course_name)
    PrintCourseBetter(course_name)

Main()