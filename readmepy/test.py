
def get_row(matrix, i):
    return matrix[i]

def get_col(matrix, i):
    return [row[i] for row in matrix]

def num_row(matrix):
    return len(matrix)

def num_col(matrix):
    return len(matrix[0])

def is_col_extreme(col):
    mean = sum(col) / len(col)
    return mean in (1, 0)

def swap_cols_rows(matrix):
    """
    The matrix coming in is rows on the inside, columns
    on the outside. To swap them, I can just get the
    columns (on the outside) and put them into a list,
    so that the columns are now on the inside -- which
    puts the rows on the outside.
    """
    swapped = []
    for i in range(num_col(matrix)):
        col = get_col(matrix, i)
        swapped.append(col)
    return swapped

def remove_extreme_cols(matrix):
    """
    This function removes any extreme columns (avg col == 1 or ==0).
    """
    swapped = swap_cols_rows(matrix)
    nonextreme = [col for col in swapped if not is_col_extreme(col)]
    return swap_cols_rows(nonextreme)
    
def max_min_matrix(matrix):
    """
    Return the maximum value of all rows and
    the minimum value of all rows.
    """
    max_value = max([max(row) for row in matrix])
    min_value = min([min(row) for row in matrix])
    return max_value, min_value

def normalized_matrix(matrix):
    maxv, minv = max_min_matrix(matrix)
    difference = maxv - minv
    rebased = [[cell - minv for cell in row] for row in matrix]
    resized = [[cell*1.0/difference for cell in row] for row in rebased]
    return resized

    




