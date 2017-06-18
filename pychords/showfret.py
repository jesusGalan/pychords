'''showfret is able to write notes on ascii fretboard and show it on bash sessions'''

import sys
from pychords.fretcodemap import cat_codemaps, get_codemap_of, init_fret_codemap, init_notemap

def initialize_and_concat_codemaps(all_sys_notes):
    '''Concatenation of codemaps according to the selected notes and returning the result'''
    codemap = init_fret_codemap()

    for note in enumerate(all_sys_notes):
        if note[1] is not None:
            codemap = cat_codemaps(codemap, get_codemap_of(init_notemap(note[1])))

    return codemap

def visualize_map(codemap):
    '''Visualization of the fretboard with the selected notes'''
    ext = '------------------------------------------------------------------------------------'
    fret_number = ' 0                    3             5             7             9'
    mastil = [fret_number,
              ext,
              return_row(codemap, 'first_string'),
              return_row(codemap, 'second_string'),
              return_row(codemap, 'third_string'),
              return_row(codemap, 'fourth_string'),
              return_row(codemap, 'fifth_string'),
              return_row(codemap, 'sixth_string'), ext]

    for obj in mastil:
        print obj

def return_row(codemap, string_number):
    '''Return a row with selected notes for each guitar string'''
    structure = []

    for fret_number in range(12):
        if codemap[string_number][fret_number][2] and '.' in codemap[string_number][fret_number][1]:
            structure.append(codemap[string_number][fret_number][1].split('.')[1])
        elif (codemap[string_number][fret_number][2] and
              '.' not in codemap[string_number][fret_number][1]):
            structure.append(codemap[string_number][fret_number][1])
        else:
            structure.append(' ')

    result = ''
    
    for item in enumerate(check_width(structure)):
        result = result + check_width(structure)[item[0]]

    return result

def check_width(arr):
    '''This method can reform the draw according to the names of the notes'''

    structure = []
    structure.append(' ')
    for i, item in enumerate(arr):
        if len(item) > 1:
            if i == len(arr):
                structure.append(item)
                structure.append(' |')
            else:
                structure.append(item)
                structure.append('  |  ')
        else:
            structure.append(item)
            if i < 1:
                structure.append('  ||  ')
            else:
                structure.append('   |  ')

    return structure

def inject_arguments(num):
    try:
        return sys.argv[num]

    except IndexError:
        return None


def draw_fret_according_to(arguments_length):
    '''Initial task to show items on bash guitar replica'''

    notes = []

    for item in range(1, arguments_length):
        notes.append(inject_arguments(item))

    visualize_map(initialize_and_concat_codemaps(notes))

if __name__ == '__main__':
    draw_fret_according_to(len(sys.argv))
