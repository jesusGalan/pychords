import sys
from fretCodemap import *


def visualize_map(codemap):
    ext = '------------------------------------------------------------------------------------'
    string = ' || | | | | | | | | | | |'
    fretNumber = ' 0                    3             5             7             9'
    mastil = [fretNumber, ext, return_row(codemap, 'first_string'), return_row(codemap, 'second_string'), return_row(codemap, 'third_string'), return_row(codemap, 'fourth_string'), return_row(codemap, 'fifth_string'), return_row(codemap, 'sixth_string'), ext]

    for obj in mastil:
        print obj

def return_row(codemap, numString):
    r = []
    for x in range(12):
        if codemap[numString][x][2] and '.' in codemap[numString][x][1]:
            r.append(codemap[numString][x][1].split('.')[1])
        elif codemap[numString][x][2] and '.' not in codemap[numString][x][1]:
            r.append(codemap[numString][x][1])
        else:
            r.append(' ')

    result = ''
    for h in range(len(check_width(r))):
        result = result + check_width(r)[h]

    return result

def check_width(arr):
    f = []
    f.append(' ')
    for i in range(len(arr)):
        if len(arr[i]) > 1:
            if i == len(arr):
                f.append(arr[i])
                f.append(' |')
            else:
                f.append(arr[i])
                f.append('  |  ')
        else:
            f.append(arr[i])
            if i < 1:
                f.append('  ||  ')
            else:
                f.append('   |  ')

    return f


def init_notemap():
    return {'C': ['A-8', 'B-1', 'C-5', 'D-10', 'E-3', 'F-8'],
            'C#': ['A-9', 'B-2', 'C-6', 'D-11', 'E-4', 'F-9'],
            'Db': ['A-9', 'B-2', 'C-6', 'D-11', 'E-4', 'F-9'],
            'D': ['A-10', 'B-3', 'C-7', 'D-0', 'E-5', 'F-10'],
            'D#': ['A-11', 'B-4', 'C-8', 'D-1', 'E-6', 'F-11'],
            'Eb': ['A-11', 'B-4', 'C-8', 'D-1', 'E-6', 'F-11'],
            'E': ['A-0', 'B-5', 'C-9', 'D-2', 'E-7', 'F-0'],
            'F': ['A-1', 'B-6', 'C-10', 'D-3', 'E-8', 'F-1'],
            'F#': ['A-2', 'B-7', 'C-11', 'D-4', 'E-9', 'F-2'],
            'Gb': ['A-2', 'B-7', 'C-11', 'D-4', 'E-9', 'F-2'],
            'G': ['A-3', 'B-8', 'C-0', 'D-5', 'E-10', 'F-3'],
            'G#': ['A-4', 'B-9', 'C-1', 'D-6', 'E-11', 'F-4'],
            'Ab': ['A-4', 'B-9', 'C-1', 'D-6', 'E-11', 'F-4'],
            'A': ['A-5', 'B-10', 'C-2', 'D-7', 'E-0', 'F-5'],
            'A#': ['A-6', 'B-11', 'C-3', 'D-8', 'E-1', 'F-6'],
            'Bb': ['A-6', 'B-11', 'C-3', 'D-8', 'E-1', 'F-6'],
            'B': ['A-7', 'B-0', 'C-4', 'D-9', 'E-2', 'F-7']}

if __name__ == '__main__':
    try:
        heptaNotes = hepta_map(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5], sys.argv[6], sys.argv[7])
        visualize_map(heptaNotes)
    except IndexError:
        try:
            sixaNotes = sixsa_map(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5], sys.argv[6])
            visualize_map(sixaNotes)
        except IndexError:
            try:
                pentaNotes = penta_map(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
                visualize_map(pentaNotes)
            except IndexError:
                try:
                    tetraNotes = tetra_map(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
                    visualize_map(tetraNotes)
                except IndexError:
                    try:
                        triadNotes = triad_map(sys.argv[1],sys.argv[2],sys.argv[3])
                        visualize_map(triadNotes)
                    except IndexError:
                        try:
                            diadNotes = cat_codemaps(get_codemap_of(init_notemap()[sys.argv[1]]), get_codemap_of(init_notemap()[sys.argv[2]]))
                            visualize_map(diadNotes)
                        except IndexError:
                            try:
                                visualize_map(get_codemap_of(init_notemap()[sys.argv[1]]))
                            except IndexError:
                                visualize_map(cromatic_map())
