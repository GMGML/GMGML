feedbacks = {}

def create_feedback(feed_id, com_id, error_msg):
    feedbacks[feed_id] = [com_id, error_msg]
    print(f"Feedback created successfully with ID {feed_id}.")
    
def read_feedback(feed_id):
    if feed_id in feedbacks:
        com_id, error_msg = feedbacks[feed_id]
        print(f"Feedback with ID {feed_id}:")
        print(f" - Com ID: {com_id}")
        print(f" - Error Message: {error_msg}")
    else:
        print(f"Feedback with ID {feed_id} not found.")

def update_feedback(feed_id, new_com_id, new_error_msg):
    if feed_id in feedbacks:
        feedbacks[feed_id] = [new_com_id, new_error_msg]
        print(f"Feedback with ID {feed_id} updated successfully.")
    else:
        print(f"Feedback with ID {feed_id} not found.")

def delete_feedback(feed_id):
    if feed_id in feedbacks:
        del feedbacks[feed_id]
        print(f"Feedback with ID {feed_id} deleted successfully.")
    else:
        print(f"Feedback with ID {feed_id} not found.")