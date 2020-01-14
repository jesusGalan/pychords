'''do functions for notemaps to be drawn'''
from functions import take_all_notes_from


def fresh_fret_data():
    '''initialized empty codemap'''

    return {'first_string': [], 'second_string': [],
            'third_string': [], 'fourth_string': [],
            'fifth_string': [], 'sixth_string': []}


def init_fret_codemap():
    '''initializing codemap'''

    fret_map = fresh_fret_data()
    for i in ['1', '2', '3', '4', '5', '6']:
        for x in range(12):  # pylint: disable=invalid-name
            compose_fret_codemap(i, x, fret_map)

    return fret_map


def compose_fret_codemap(i, string_number, codemap):
    '''writing default no visibility values'''

    names_of_guitar_strings = {'1': 'E',
                               '2': 'B',
                               '3': 'G',
                               '4': 'D',
                               '5': 'A',
                               '6': 'E'}

    string_correspondencies = get_strings_correspondencies()

    code = (i + '-' + str(string_number),
            take_all_notes_from(names_of_guitar_strings[i])[string_number],
            False)

    codemap[string_correspondencies[i]].append(code)


def get_codemap_of(notes_to_be_mapped):
    '''This is the entry point to get notemaps'''
    original_codemap = init_fret_codemap()
    processed_codemap = fresh_fret_data()

    for i in ['1', '2', '3', '4', '5', '6']:

        for fret_number in range(12):
            compose_is_needed = False

            for string_number in range(6):
                if (int(notes_to_be_mapped[string_number].split('-')[1]) == fret_number and
                        notes_to_be_mapped[string_number].split('-')[0] in i):
                    compose_is_needed = True

            if compose_is_needed:
                compose_new_address(fret_number, i, original_codemap, processed_codemap)
            else:
                get_from_orig_on_addres(fret_number, i, original_codemap, processed_codemap)

    return processed_codemap


def compose_new_address(fret_number, string_number, orig, process):
    '''Composing each adress when the note have visibility'''

    string_correspondencies = get_strings_correspondencies()

    process[string_correspondencies[string_number]].append((
        orig[string_correspondencies[string_number]][fret_number][0],
        orig[string_correspondencies[string_number]][fret_number][1],
        True))


def get_strings_correspondencies():
    '''String correspondencies refactor'''

    return {'1': 'first_string', '2': 'second_string', '3': 'third_string',
            '4': 'fourth_string', '5': 'fifth_string', '6': 'sixth_string'}


def get_from_orig_on_addres(fret_number, string_number, orig, process):
    '''Compose adress when the note is hidden'''

    string_correspondencies = get_strings_correspondencies()

    process[string_correspondencies[string_number]].append(
        orig[string_correspondencies[string_number]][fret_number])


def init_notemap(note):
    '''Positions of each note with (number_of_string)-(number_of_fret)'''

    full_map = {'C': ['1-8', '2-1', '3-5', '4-10', '5-3', '6-8'],
                'C#': ['1-9', '2-2', '3-6', '4-11', '5-4', '6-9'],
                'Db': ['1-9', '2-2', '3-6', '4-11', '5-4', '6-9'],
                'D': ['1-10', '2-3', '3-7', '4-0', '5-5', '6-10'],
                'D#': ['1-11', '2-4', '3-8', '4-1', '5-6', '6-11'],
                'Eb': ['1-11', '2-4', '3-8', '4-1', '5-6', '6-11'],
                'E': ['1-0', '2-5', '3-9', '4-2', '5-7', '6-0'],
                'F': ['1-1', '2-6', '3-10', '4-3', '5-8', '6-1'],
                'F#': ['1-2', '2-7', '3-11', '4-4', '5-9', '6-2'],
                'Gb': ['1-2', '2-7', '3-11', '4-4', '5-9', '6-2'],
                'G': ['1-3', '2-8', '3-0', '4-5', '5-10', '6-3'],
                'G#': ['1-4', '2-9', '3-1', '4-6', '5-11', '6-4'],
                'Ab': ['1-4', '2-9', '3-1', '4-6', '5-11', '6-4'],
                'A': ['1-5', '2-10', '3-2', '4-7', '5-0', '6-5'],
                'A#': ['1-6', '2-11', '3-3', '4-8', '5-1', '6-6'],
                'Bb': ['1-6', '2-11', '3-3', '4-8', '5-1', '6-6'],
                'B': ['1-7', '2-0', '3-4', '4-9', '5-2', '6-7']}

    return full_map[note]


def cat_codemaps(codemap1, codemap2):
    '''Concatenation of a pair of notemaps '''

    compo = fresh_fret_data()
    string_correspondencies = get_strings_correspondencies()

    for i in ['1', '2', '3', '4', '5', '6']:
        for fret_number in range(12):
            codemaps_note_visibility = [codemap1[string_correspondencies[i]][fret_number][2],
                                        codemap2[string_correspondencies[i]][fret_number][2]]

            if (codemaps_note_visibility[0] and codemaps_note_visibility[1] or
                    codemaps_note_visibility[0] and not codemaps_note_visibility[1]):
                compo[string_correspondencies[i]].append(
                    codemap1[string_correspondencies[i]][fret_number])
            else:
                compo[string_correspondencies[i]].append(
                    codemap2[string_correspondencies[i]][fret_number])

    return compo


if __name__ == '__main__':
    print(get_codemap_of(['A-8', 'B-1', 'C-5', 'D-10', 'E-3', 'F-8']))
