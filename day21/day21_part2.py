opportunities = {"N": (-1, 0), "S": (1, 0), "W": (0, -1), "E": (0, 1)}
def valid(r, c, row, column, array):
    # print(0<=r<row)
    if 0 <= r < row and 0 <= c < column and array[r][c] == '.':
        return True
    return False

def func(r, c, plots, array_rows, array_cols,parity):
    i = 1
    plots3 = set()
    x= 0 if parity=='even' else 1
    while True:
        plots2 = set()
        for r, c in plots:
            for dir in opportunities:
                if valid(r+opportunities[dir][0], c+opportunities[dir][1], array_rows, array_cols, array) and (r+opportunities[dir][0], c+opportunities[dir][1]) not in plots2:
                    plots2.add(
                        (r+opportunities[dir][0], c+opportunities[dir][1]))
        if (len(plots3.symmetric_difference(plots2)) == 0):
            return plots3
        plots = plots2
        if i % 2 == x:
            plots3 = plots
        i += 1
if __name__ == '__main__':
    s = 0
    with open(file='input.txt') as f:
        lines = f.readlines()
    # print(lines)
    array = [list(i[:-1]) for i in lines]
    row, col = 0, 0
    array_rows = len(array)
    array_cols = len(array[0])
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == 'S':
                row, col = i, j
    array[row][col] = '.'
    plots = {(row, col)}
    odd = func(row, col, plots, array_rows, array_cols,'odd')
    even = func(row, col, plots, array_rows, array_cols,'even')
    odd_corners = len([(i, j) for i, j in odd if abs(row-i)+abs(col-j) > 65])
    even_corners = len([(i, j) for i, j in even if abs(row-i)+abs(col-j) > 65])
    odd_all = (len(odd))
    even_all = (len(even))
    n = 202300
    print(n*n * odd_all + (n-1)*(n-1) * even_all- ((n + 1) * odd_corners)+ (n * even_corners))

