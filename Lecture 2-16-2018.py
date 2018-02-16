"Wrap up Chapter 8 today apparently"

# He just showed us his Jump It GUI and we really havent done much yet

# Then went on to Psuedo code for the homework due today

# Now back to GUI with 20 minutes left...

def read_data_file(file_name: str) -> str:
    with open(file_name, 'r') as f:
        return f.read()
def read_boards(data: str) -> list:
    boards = []
    boards_data = data.split('\n')
    for board in boards_data:
        if len(board) > 0:
            boards.append(list(map(lambda v: int(v), board.split())))
    return boards

