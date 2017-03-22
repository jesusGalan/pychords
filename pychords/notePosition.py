def get_fretboard_c_positions():
    return [
        {'cord': 1, 'fret': 8},
        {'cord': 6, 'fret': 8},
        {'cord': 2, 'fret': 1},
        {'cord': 3, 'fret': 5},
        {'cord': 4, 'fret': 10},
        {'cord': 5, 'fret': 3},
    ]


def get_fretboard_c_sharp_positions():
    return [
        {'cord': 1, 'fret': 9},
        {'cord': 6, 'fret': 9},
        {'cord': 2, 'fret': 2},
        {'cord': 3, 'fret': 6},
        {'cord': 4, 'fret': 11},
        {'cord': 5, 'fret': 4},
    ]


def get_fretboard_d_bemol_positions():
    return [
        {'cord': 1, 'fret': 9},
        {'cord': 6, 'fret': 9},
        {'cord': 2, 'fret': 2},
        {'cord': 3, 'fret': 6},
        {'cord': 4, 'fret': 11},
        {'cord': 5, 'fret': 4},
    ]


def get_fretboard_d_positions():
    return [
        {'cord': 1, 'fret': 10},
        {'cord': 6, 'fret': 10},
        {'cord': 2, 'fret': 3},
        {'cord': 3, 'fret': 7},
        {'cord': 4, 'fret': 0},
        {'cord': 5, 'fret': 5},
    ]


def get_fretboard_d_sharp_positions():
    return [
        {'cord': 1, 'fret': 11},
        {'cord': 6, 'fret': 11},
        {'cord': 2, 'fret': 4},
        {'cord': 3, 'fret': 8},
        {'cord': 4, 'fret': 1},
        {'cord': 5, 'fret': 6},
    ]


def get_fretboard_e_bemol_positions():
    return [
        {'cord': 1, 'fret': 11},
        {'cord': 6, 'fret': 11},
        {'cord': 2, 'fret': 4},
        {'cord': 3, 'fret': 8},
        {'cord': 4, 'fret': 1},
        {'cord': 5, 'fret': 6},
    ]


def get_fretboard_e_positions():
    return [
        {'cord': 1, 'fret': 0},
        {'cord': 6, 'fret': 0},
        {'cord': 2, 'fret': 5},
        {'cord': 3, 'fret': 9},
        {'cord': 4, 'fret': 2},
        {'cord': 5, 'fret': 7},
    ]


def get_fretboard_f_positions():
    return [
        {'cord': 1, 'fret': 1},
        {'cord': 6, 'fret': 1},
        {'cord': 2, 'fret': 6},
        {'cord': 3, 'fret': 10},
        {'cord': 4, 'fret': 3},
        {'cord': 5, 'fret': 8},
    ]


def get_fretboard_f_sharp_positions():
    return [
        {'cord': 1, 'fret': 2},
        {'cord': 6, 'fret': 2},
        {'cord': 2, 'fret': 7},
        {'cord': 3, 'fret': 11},
        {'cord': 4, 'fret': 4},
        {'cord': 5, 'fret': 9},
    ]


def get_fretboard_g_bemol_positions():
    return [
        {'cord': 1, 'fret': 2},
        {'cord': 6, 'fret': 2},
        {'cord': 2, 'fret': 7},
        {'cord': 3, 'fret': 11},
        {'cord': 4, 'fret': 4},
        {'cord': 5, 'fret': 9},
    ]


def get_fretboard_g_positions():
    return [
        {'cord': 1, 'fret': 3},
        {'cord': 6, 'fret': 3},
        {'cord': 2, 'fret': 8},
        {'cord': 3, 'fret': 0},
        {'cord': 4, 'fret': 5},
        {'cord': 5, 'fret': 10},
    ]


def get_fretboard_g_sharp_positions():
    return [
        {'cord': 1, 'fret': 4},
        {'cord': 6, 'fret': 4},
        {'cord': 2, 'fret': 9},
        {'cord': 3, 'fret': 1},
        {'cord': 4, 'fret': 6},
        {'cord': 5, 'fret': 11},
    ]


def get_fretboard_a_bemol_positions():
    return [
        {'cord': 1, 'fret': 4},
        {'cord': 6, 'fret': 4},
        {'cord': 2, 'fret': 9},
        {'cord': 3, 'fret': 1},
        {'cord': 4, 'fret': 6},
        {'cord': 5, 'fret': 11},
    ]


def get_fretboard_a_positions():
    return [
        {'cord': 1, 'fret': 5},
        {'cord': 6, 'fret': 5},
        {'cord': 2, 'fret': 10},
        {'cord': 3, 'fret': 2},
        {'cord': 4, 'fret': 7},
        {'cord': 5, 'fret': 0},
    ]


def get_fretboard_a_sharp_positions():
    return [
        {'cord': 1, 'fret': 6},
        {'cord': 6, 'fret': 6},
        {'cord': 2, 'fret': 11},
        {'cord': 3, 'fret': 3},
        {'cord': 4, 'fret': 8},
        {'cord': 5, 'fret': 1},
    ]


def get_fretboard_b_bemol_positions():
    return [
        {'cord': 1, 'fret': 6},
        {'cord': 6, 'fret': 6},
        {'cord': 2, 'fret': 11},
        {'cord': 3, 'fret': 3},
        {'cord': 4, 'fret': 8},
        {'cord': 5, 'fret': 1},
    ]


def get_fretboard_b_positions():
    return [
        {'cord': 1, 'fret': 7},
        {'cord': 6, 'fret': 7},
        {'cord': 2, 'fret': 0},
        {'cord': 3, 'fret': 4},
        {'cord': 4, 'fret': 9},
        {'cord': 5, 'fret': 2},
    ]

def get_fretboard_note_positions(note):
    positions = {
        'C': get_fretboard_c_positions(),
        'C#': get_fretboard_c_sharp_positions(),
        'Db': get_fretboard_d_bemol_positions(),
        'D': get_fretboard_d_positions(),
        'D#': get_fretboard_d_sharp_positions(),
        'Eb': get_fretboard_e_bemol_positions(),
        'E': get_fretboard_e_positions(),
        'F': get_fretboard_f_positions(),
        'F#': get_fretboard_f_sharp_positions(),
        'Gb': get_fretboard_g_bemol_positions(),
        'G': get_fretboard_g_positions(),
        'G#': get_fretboard_g_sharp_positions(),
        'Ab': get_fretboard_a_bemol_positions(),
        'A': get_fretboard_a_positions(),
        'A#': get_fretboard_a_sharp_positions(),
        'Bb': get_fretboard_b_bemol_positions(),
        'B': get_fretboard_b_positions(),
    }

    if note in positions.keys():
        return positions.get(note)

    else:
        return [{'cord': 'None', 'fret': 'None'}]
