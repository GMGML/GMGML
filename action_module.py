actions = {}

def create_action(com_id, feed_id, action_msg):
    actions[feed_id] = [com_id, action_msg]
    print(f"Action created successfully with ID {feed_id}.")
    
def read_action(feed_id):
    if feed_id in actions:
        com_id, action_msg = actions[feed_id]
        print(f"Action with ID {feed_id}:")
        print(f" - Com ID: {com_id}")
        print(f" - Action Message: {action_msg}")
    else:
        print(f"Action with ID {feed_id} not found.")

def update_action(feed_id, new_com_id, new_action_msg):
    if feed_id in actions:
        actions[feed_id] = [new_com_id, new_action_msg]
        print(f"Action with ID {feed_id} updated successfully.")
    else:
        print(f"Action with ID {feed_id} not found.")

def delete_action(feed_id):
    if feed_id in actions:
        del actions[feed_id]
        print(f"Action with ID {feed_id} deleted successfully.")
    else:
        print(f"Action with ID {feed_id} not found.")