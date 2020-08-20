def parse_line(line):
    splitted_line = line.split('|')
    return splitted_line

def to_matrix(table_content, has_headers=True):
    matrix_table = []
    
    if has_headers:
        content_splited_on_line_breaks = table_content.split('\n')[2:]
    else:
        content_splited_on_line_breaks = table_content.split('\n')
    
    for line in content_splited_on_line_breaks:
        matrix_line = parse_line(line)
        matrix_table.append(matrix_line[1:-1])
    
    return matrix_table
