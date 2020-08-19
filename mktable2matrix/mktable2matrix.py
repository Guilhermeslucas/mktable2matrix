def parse_line(line):
    splitted_line = line.split('|')
    return splitted_line

def to_matrix(table_content):
    matrix_table = []
    
    for line in table_content.split('\n')[2:]:
        matrix_line = parse_line(line)
        matrix_table.append(matrix_line[1:-1])
    
    return matrix_table

