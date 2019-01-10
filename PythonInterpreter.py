INTERPRET_TARGET_FILE = 'InterpreterWithinSL_1.sl'

variables = {}

class KEYWORDS:
    get_file_lines = 'get_file_lines'
    interpret_lines = 'interpret'
    assign = '='
    print_c = 'print'


def get_file_lines(target_file):
    with open(target_file, 'r') as f:
        return f.readlines()


def process_command(cmd_string):
    return cmd_string.replace('\n', '')


def execute_command(cmd_string):
    if not isinstance(cmd_string, list):
        cmd_string = cmd_string.split(' ')

    if cmd_string[0] == KEYWORDS.get_file_lines:
        return get_file_lines(execute_command(cmd_string[1]))
    elif cmd_string[0] == KEYWORDS.interpret_lines:
        interpret_lines(execute_command(cmd_string[1]))
    elif cmd_string[0] == KEYWORDS.assign:
        variables[cmd_string[1]] = execute_command(cmd_string[2:])
    elif cmd_string[0] == KEYWORDS.print_c:
        print(execute_command(cmd_string[1:]))
    else:
        if cmd_string[0] in variables.keys():
            return variables[cmd_string[0]]
        return cmd_string[0]


def interpret_lines(lines):
    for line in lines:
        execute_command(process_command(line))


if __name__ == '__main__':
    interpret_lines(get_file_lines(INTERPRET_TARGET_FILE))
