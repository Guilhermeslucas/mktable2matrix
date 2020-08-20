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

def to_dict(table_content):
    dict_table = {}
    content_splited_on_line_breaks = table_content.split('\n')
    headers = parse_line(content_splited_on_line_breaks[0])

    for i in range(len(headers)):
        dict_table[str(i)] = []

    content_without_headers = content_splited_on_line_breaks[2:]

    for i in range(len(content_without_headers)):
        parsed_line = parse_line(content_without_headers[i])
        for j in range(len(parsed_line)):
            dict_table[str(j)].append(parsed_line[j])
    
    headers[0] = 0
    headers[len(headers) - 1] = len(headers) - 1

    for i in range(len(headers)):
        dict_table[headers[i]] = dict_table[str(i)]
        del dict_table[str(i)]
    
    del dict_table[0]
    del dict_table[len(headers) - 1]
    
    return dict_table
