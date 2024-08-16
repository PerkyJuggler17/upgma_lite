def connection(row1, row2):
    value = 0
    for i in range(len(row1)):
        value += int(row1[i] != row2[i])

    return value


def find_minimum(data):

    min_value, min_index = [], []
    for row in data:
        min_value.append(min(row))
        min_index.append(row.index(min(row)))

    value = min(min_value)
    row = min_value.index(value)
    col = min_index[row]

    return value, [row, col]


def connection_matrix(info):
    result = [[float('inf') for _ in range(len(info))] for _ in range(len(info))]

    for index, row in enumerate(info):
        for _index, _row in enumerate(info):
            if index < _index:
                result[index][_index] = connection(row, _row)

    return result


def sort_index(matrix, row_index, column_index):
    if column_index < row_index:
        return matrix[column_index][row_index]
    else:
        return matrix[row_index][column_index]


def improve_connection_matrix(matrix, value, position):
    # value, position = find_minimum(matrix)
    new_matrix = [[float('inf') for _ in range(len(matrix))] for _ in range(len(matrix))]

    for row_index, row in enumerate(matrix):
        for col_index, col in enumerate(row):
            if row_index < col_index:
                if row_index not in position and col_index not in position:
                    new_matrix[row_index][col_index] = col
                elif col_index in position:
                    new_matrix[row_index][col_index] = (sort_index(matrix, row_index, position[0]) +
                                                        sort_index(matrix, row_index, position[1]))/2

                elif row_index in position:
                    new_matrix[row_index][col_index] = (sort_index(matrix, position[0], col_index) +
                                                        sort_index(matrix, position[1], col_index))/2

    new_matrix.pop(position[1])

    for row in new_matrix:
        row.pop(position[1])

    return new_matrix


def update_relation(relation, value, position):
    new_relation = relation
    new_relation[position[0]] = [new_relation[position[0]], value/2, new_relation[position[1]]]
    new_relation.pop(position[1])

    return new_relation


if __name__ == '__main__':
    # initial_info = [[3,3,2,0,4,3],
    #                 [3,3,0,2,2,3],
    #                 [3,2,3,3,0,4],
    #                 [2,1,3,2,3,3],
    #                 [2,1,0,3,3,4],
    #                 [3,2,3,1,2,4]]
    initial_info = [[3,2,2,2,4,3,4,4],
                    [3,3,3,2,4,3,0,3],
                    [3,3,3,2,4,3,2,3],
                    [3,3,0,3,3,3,4,4],
                    [3,3,3,2,4,3,3,4],
                    [3,3,3,3,2,2,4,4],
                    [3,4,0,0,4,0,3,2],
                    [3,3,4,4,4,3,4,3],
                    [2.5,2.5,4,4,4,3,4,2],
                    [2.5,2.5,0,0,4,3,3,4],
                    [2,2,4,3,4,4,4,3],
                    [2,1,0,0,4,3,4,3],
                    [2,1,2,2,4,3,4,2],
                    [2,1,3,4,4,3,4,4]]

    initial_relation = [i for i in range(len(initial_info))]
    connections = connection_matrix(initial_info)

    while len(connections) > 1:
        value, position = find_minimum(connections)

        connections = improve_connection_matrix(connections, value, position)

        initial_relation = update_relation(initial_relation, value, position)

    print(initial_relation)
