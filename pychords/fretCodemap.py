from functions import take_all_notes_from


def triad_map(note1, note2, note3):
    diads = cat_codemaps(get_codemap_of(init_notemap()[note1]), get_codemap_of(init_notemap()[note2]))

    return cat_codemaps(diads, get_codemap_of(init_notemap()[note3]))


def tetra_map(note1, note2, note3, note4):
    return cat_codemaps(triad_map(note1,note2,note3), get_codemap_of(init_notemap()[note4]))


def penta_map(note1, note2, note3, note4, note5):
    return cat_codemaps(tetra_map(note1, note2, note3, note4), get_codemap_of(init_notemap()[note5]))


def sixsa_map(note1, note2, note3, note4, note5, note6):
    return cat_codemaps(triad_map(note1,note2,note3), triad_map(note4,note5,note6))


def hepta_map(note1, note2, note3, note4, note5, note6, note7):
    return cat_codemaps(triad_map(note1,note2,note3), tetra_map(note4,note5,note6,note7))


def cromatic_map():
    return cat_codemaps(sixsa_map('C','C#','D','D#','E','F'), sixsa_map('F#','G','G#','A','A#','B'))


def fresh_fret_data():
    return { 'first_string' : [], 'second_string': [],
             'third_string': [],  'fourth_string': [],
             'fifth_string': [],  'sixth_string': []}


def init_fret_codemap():
    fretMap = fresh_fret_data()
    for i in ['A', 'B', 'C', 'D', 'E', 'F']:
        for x in range(12):
            compose_fret_codemap(i, x, fretMap)

    return fretMap


def compose_fret_codemap(i, x, codemap):
    if 'A' in i:
        code = (i+'-'+str(x), take_all_notes_from("E")[x], False)
        codemap['first_string'].append(code)
    if 'B' in i:
        code = (i+'-'+str(x), take_all_notes_from("B")[x], False)
        codemap['second_string'].append(code)
    if 'C' in i:
        code = (i+'-'+str(x), take_all_notes_from("G")[x], False)
        codemap['third_string'].append(code)
    if 'D' in i:
        code = (i+'-'+str(x), take_all_notes_from("D")[x], False)
        codemap['fourth_string'].append(code)
    if 'E' in i:
        code = (i+'-'+str(x), take_all_notes_from("A")[x], False)
        codemap['fifth_string'].append(code)
    if 'F' in i:
        code = (i+'-'+str(x), take_all_notes_from("E")[x], False)
        codemap['sixth_string'].append(code)


def get_codemap_of(data):
    original_codemap = init_fret_codemap()
    processed_codemap = fresh_fret_data()

    for i in ['A', 'B', 'C', 'D', 'E', 'F']:
        for x in range(12):
            code = i +'-'+ str(x)
            if (int(data[0].split('-')[1]) == x and data[0].split('-')[0] in i) or (
                int(data[1].split('-')[1]) == x and data[1].split('-')[0] in i) or (
                int(data[2].split('-')[1]) == x and data[2].split('-')[0] in i) or (
                int(data[3].split('-')[1]) == x and data[3].split('-')[0] in i) or (
                int(data[4].split('-')[1]) == x and data[4].split('-')[0] in i) or (
                int(data[5].split('-')[1]) == x and data[5].split('-')[0] in i):
                compose_new_addres(x, i, original_codemap, processed_codemap)
            else:
                get_from_orig_on_addres(x, i, original_codemap, processed_codemap)

    return processed_codemap


def compose_new_addres(x, i, orig, process):
    if 'A' in i:
        process['first_string'].append((orig['first_string'][x][0],
                                        orig['first_string'][x][1],
                                        True))
    if 'B' in i:
        process['second_string'].append((orig['second_string'][x][0],
                                         orig['second_string'][x][1],
                                         True))
    if 'C' in i:
        process['third_string'].append((orig['third_string'][x][0],
                                        orig['third_string'][x][1],
                                        True))
    if 'D' in i:
        process['fourth_string'].append((orig['fourth_string'][x][0],
                                        orig['fourth_string'][x][1],
                                        True))
    if 'E' in i:
        process['fifth_string'].append((orig['fifth_string'][x][0],
                                        orig['fifth_string'][x][1],
                                        True))
    if 'F' in i:
        process['sixth_string'].append((orig['sixth_string'][x][0],
                                        orig['sixth_string'][x][1],
                                        True))

def get_from_orig_on_addres(x, i, orig, process):
    if 'A' in i:
        process['first_string'].append(orig['first_string'][x])
    if 'B' in i:
        process['second_string'].append(orig['second_string'][x])
    if 'C' in i:
        process['third_string'].append(orig['third_string'][x])
    if 'D' in i:
        process['fourth_string'].append(orig['fourth_string'][x])
    if 'E' in i:
        process['fifth_string'].append(orig['fifth_string'][x])
    if 'F' in i:
        process['sixth_string'].append(orig['sixth_string'][x])


def cat_codemaps(codemap1, codemap2):
    compo = fresh_fret_data()

    for i in ['A', 'B', 'C', 'D', 'E', 'F']:
        for x in range(12):
            if 'A' in i:
                if codemap1['first_string'][x][2] and not codemap2['first_string'][x][2]:
                    compo['first_string'].append(codemap1['first_string'][x])
                elif not codemap1['first_string'][x][2] and codemap2['first_string'][x][2]:
                    compo['first_string'].append(codemap2['first_string'][x])
                else:
                    compo['first_string'].append(codemap1['first_string'][x])

            if 'B' in i:
                if codemap1['second_string'][x][2] and not codemap2['second_string'][x][2]:
                    compo['second_string'].append(codemap1['second_string'][x])
                elif not codemap1['second_string'][x][2] and codemap2['second_string'][x][2]:
                    compo['second_string'].append(codemap2['second_string'][x])
                else:
                    compo['second_string'].append(codemap1['second_string'][x])

            if 'C' in i:
                if codemap1['third_string'][x][2] and not codemap2['third_string'][x][2]:
                    compo['third_string'].append(codemap1['third_string'][x])
                elif not codemap1['third_string'][x][2] and codemap2['third_string'][x][2]:
                    compo['third_string'].append(codemap2['third_string'][x])
                else:
                    compo['third_string'].append(codemap1['third_string'][x])

            if 'D' in i:
                if codemap1['fourth_string'][x][2] and not codemap2['fourth_string'][x][2]:
                    compo['fourth_string'].append(codemap1['fourth_string'][x])
                elif not codemap1['fourth_string'][x][2] and codemap2['fourth_string'][x][2]:
                    compo['fourth_string'].append(codemap2['fourth_string'][x])
                else:
                    compo['fourth_string'].append(codemap1['fourth_string'][x])

            if 'E' in i:
                if codemap1['fifth_string'][x][2] and not codemap2['fifth_string'][x][2]:
                    compo['fifth_string'].append(codemap1['fifth_string'][x])
                elif not codemap1['fifth_string'][x][2] and codemap2['fifth_string'][x][2]:
                    compo['fifth_string'].append(codemap2['fifth_string'][x])
                else:
                    compo['fifth_string'].append(codemap1['fifth_string'][x])

            if 'F' in i:
                if codemap1['sixth_string'][x][2] and not codemap2['sixth_string'][x][2]:
                    compo['sixth_string'].append(codemap1['sixth_string'][x])
                elif not codemap1['sixth_string'][x][2] and codemap2['sixth_string'][x][2]:
                    compo['sixth_string'].append(codemap2['sixth_string'][x])
                else:
                    compo['sixth_string'].append(codemap1['sixth_string'][x])

    return compo

if __name__ == '__main__':
    print '''usage:
mapCnotes = ['A-8', 'B-1', 'C-5', 'D-10', 'E-3', 'F-8']
print get_codemap_of(mapCnotes)'''
