global_vars = {"test": "global"}

def run_code():
    local_vars = {}
    exec("test = 'local'", global_vars, local_vars)
    print(global_vars)  # Output: {'test': 'global'}
    print(local_vars)  # Output: {'test': 'local'}

run_code()
