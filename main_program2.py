from code_commit_module import *
from feedback_module import *
from action_module import *
from gather_track import *

code_commits = {}

feedbacks = {}

actions = {}

while True:
    print("1. Create Code Commit")
    print("2. Read Code Commit")
    print("3. Update Code Commit")
    print("4. Delete Code Commit")
    print("5. Create Feedback")
    print("6. Read Feedback")
    print("7. Update Feedback")
    print("8. Delete Feedback")
    print("9. Create Action")
    print("10. Read Action")
    print("11. Update Action")
    print("12. Delete Action")
    print("13. Gather Commit Feedback")
    print("14. Track Feedback")
    print("0. Exit")

    choice = input("Enter your choice (0-14): ")

    if choice == "0":
        break
    elif choice == "1":
        com_id = int(input("Enter Code Commit ID: "))
        commit_msg = input("Enter Commit Message: ")
        create_code_commit(com_id, commit_msg)
    elif choice == "2":
        com_id = int(input("Enter Code Commit ID: "))
        read_code_commit(com_id)
    elif choice == "3":
        com_id = int(input("Enter Code Commit ID: "))
        new_commit_msg = input("Enter New Commit Message: ")
        update_code_commit(com_id, new_commit_msg)
    elif choice == "4":
        com_id = int(input("Enter Code Commit ID: "))
        delete_code_commit(com_id)
    elif choice == "5":
        feed_id = int(input("Enter Feedback ID: "))
        com_id = int(input("Enter Code Commit ID: "))
        error_msg = input("Enter Error Message: ")
        create_feedback(feed_id, com_id, error_msg)
    elif choice == "6":
        feed_id = int(input("Enter Feedback ID: "))
        read_feedback(feed_id)
    elif choice == "7":
        feed_id = int(input("Enter Feedback ID: "))
        new_com_id = int(input("Enter New Code Commit ID: "))
        new_error_msg = input("Enter New Error Message: ")
        update_feedback(feed_id, new_com_id, new_error_msg)
    elif choice == "8":
        feed_id = int(input("Enter Feedback ID: "))
        delete_feedback(feed_id)
    elif choice == "9":
        feed_id = int(input("Enter Action ID: "))
        com_id = int(input("Enter Code Commit ID: "))
        action_msg = input("Enter Action Message: ")
        create_action(com_id, feed_id, action_msg)
    elif choice == "10":
        feed_id = int(input("Enter Action ID: "))
        read_action(feed_id)
    elif choice == "11":
        feed_id = int(input("Enter Action ID: "))
        new_com_id = int(input("Enter New Code Commit ID: "))
        new_action_msg = input("Enter New Action Message: ")
        update_action(feed_id, new_com_id, new_action_msg)
    elif choice == "12":
        feed_id = int(input("Enter Action ID: "))
        delete_action(feed_id)
    elif choice == "13":
        com_id = int(input("Enter Code Commit ID: "))
        result = gather_commit_feedback(com_id)
        print(f"Gathered Commit Feedback: {result}")
    elif choice == "14":
        feed_id = int(input("Enter Feedback ID: "))
        result = track_feedback(feed_id)
        print(f"Tracked Feedback: {result}")
    else:
        print("Invalid choice. Please enter a number between 0 and 14.")