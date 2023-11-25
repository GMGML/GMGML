code_commits = {}

def create_code_commit(com_id,commit_msg):
    code_commits[com_id] = commit_msg
    print(f"Code Commit created successfully with ID {com_id}.")

def read_code_commit(com_id):
    if com_id in code_commits:
        commit_msg = code_commits[com_id]
        print(f"Code Commit with ID {com_id}: {commit_msg}")
    else:
        print(f"Code Commit with ID {com_id} does not exist.")

def update_code_commit(com_id, new_commit_msg):
    if com_id in code_commits:
        code_commits[com_id] = new_commit_msg
        print(f"Code Commit with ID {com_id} updated successfully.")
    else:
        print(f"Code Commit with ID {com_id} does not exist.")

def delete_code_commit(com_id):
    if com_id in code_commits:
        del code_commits[com_id]
        print(f"Code Commit with ID {com_id} deleted successfully.")
    else:
        print(f"Code Commit with ID {com_id} does not exist.")