filename = 'sudoku.txt'

# Read puzzles as 2D arrays
puzzles = []
puzzle = None
with open(filename, 'r') as f1:
    for line in f1.readlines():
        if line.startswith('Grid'):
            if puzzle is not None:
                puzzles.append(puzzle)
            puzzle = []
        else:
            puzzle.append(list(line.strip()))
puzzles.append(puzzle)


with open('sudoku_formatted.txt', 'w') as f2:
    for i, puzzle in enumerate(puzzles):
        f2.write('Puzzle {:2d}\n'.format(i+1))
        for line in puzzle:
            f2.write('\t'.join(line)+'\n')
        f2.write('\n')
