from feedback_module import feedbacks
from action_module import actions

def gather_commit_feedback(com_id):
    i=com_id
    for i in feedbacks:
        if feedbacks[i][0] == com_id:
            return feedbacks[i][1]
    return None
    
def track_feedback(feed_id):
    j=feed_id
    for j in actions:
        if actions[j][0] == feed_id:
            return actions[j][1]
    return None
