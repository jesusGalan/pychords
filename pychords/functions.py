# -*- coding: utf-8 -*-

'''Module for produce notes according to selected scales and tones'''


def read_scales_from_json(SCALES_JSON_PATH):
    with open(SCALES_JSON_PATH, 'rb') as f:
        content = f.read()

    return content

def init_all_notes():
    '''Init all notes from C to B in array form'''
    return ['C', 'C#.Db', 'D', 'D#.Eb', 'E', 'F', 'F#.Gb', 'G', 'G#.Ab', 'A', 'A#.Bb', 'B']


def take_all_notes_from(tone):
    '''This method can sort all notes from a selected tone'''
    new_notes = []
    for pos, note in enumerate(init_all_notes() + init_all_notes()):
        if(pos >= take_position(tone, init_all_notes()) and
           pos < take_position(tone, init_all_notes()) + 12):
            new_notes.append(note)

    return new_notes


def take_position(tone, notes):
    '''Get the position of a possible note'''
    if tone not in ['Fb', 'Cb', 'E#', 'B#']:
        alteration = tone[1:2]

        for pos, note in enumerate(notes):
            if "b" in alteration and tone[0:1] in note:
                if '.' in note:
                    _pos_tone = pos - 1
                else:
                    _pos_tone = pos

            elif "#" in alteration and tone[0:1] in note:
                _pos_tone = pos + 1

            else:
                if '.' not in note and tone[0:1] in note:
                    _pos_tone = pos + 1
    else:
        print('Error in line 28 of functions')

    return _pos_tone - 1

def get_sure_notes(scale_list):
    '''get index of notes with no alterations'''
    return [scale_list.index(i) for i in scale_list if '#' not in i and 'b' not in i]

def setup_scale(scale, tone):
    out_list = scale + scale
    sures = get_sure_notes(out_list)

    if len(sures) != len(out_list):
        for data in enumerate(out_list):
            if '.' in data[1]:
                out_list[data[0]] = data[1].split('.')[0]

    return out_list

def substract_scale(scale, name_of_scale):
    if name_of_scale in 'escala_cromatica':
        return [scale[0], scale[1], scale[2], scale[3], scale[4], scale[5],
                scale[6], scale[7], scale[8], scale[9], scale[10], scale[11]]

    elif name_of_scale in 'escala_tono_a_tono' or 'escala_hexatonica_de_blues' in name_of_scale:
        return [scale[6], scale[7], scale[8], scale[9], scale[10], scale[5]]

    elif name_of_scale in 'escala_semitono_a_tono' or name_of_scale in 'escala_tono_a_semitono':
        return [scale[8], scale[9], scale[10], scale[11],
                scale[12], scale[13], scale[14], scale[15]]

    else:
        return [scale[7], scale[8], scale[9], scale[10], scale[11], scale[12], scale[6]]


def substract_fixed_scale(scale, scale_name):
    if 'escala_hexatonica_de_blues' in scale_name:
        return [scale[6], scale[7], scale[8], scale[3], scale[10], scale[5]]

    else:
        return [scale[7], scale[8], scale[9], scale[3], scale[11], scale[12], scale[6]]


def scan_duplicates(scale, scale_with_points):
    result_scale = scale

    for pos in range(len(scale) - 1):
        if '.' in scale_with_points[pos]:
            if (scale[pos][0:1] in scale[pos + 1] and
                    scale_with_points[pos][0:1] not in scale[pos - 1]):
                result_scale[pos] = scale_with_points[pos].split('.')[0]
            elif scale_with_points[pos][0:1] in scale[pos - 1]:
                result_scale[pos] = scale_with_points[pos].split('.')[1]


    return result_scale


def is_there_any_duplicate(scale):
    scales = scale
    arg = False
    # Scales that going to repeat some note need to be invested under new behaviours
    for data in enumerate(scales):
        if 6 > data[0] > 0:
            if scales[data[0]][0:1] in scales[data[0] - 1]:
                arg = True
        else:
            if scales[0][0:1] in scales[len(scales) - 1][0:1]:
                arg = True

    return arg


def get_list_of_sures(swp):
    sures = get_sure_notes(swp)
    result_list = []

    for pos in enumerate(sures):
        if pos[0] == 0:
            append = str(0) + '-' + str(sures[pos[0]] + 1)
            result_list.append(append)

        elif pos[0] == len(sures) - 1:
            append = str(sures[pos[0] - 1]) + '-' + str(13)
            result_list.append(append)

        else:
            append = str(sures[pos[0] - 1] + 1) + '-' + str(sures[pos[0]] + 1)
            result_list.append(append)

    return result_list


def get_the_count_for_each_color(color_note_list):
    count_w = 0
    count_b = 0

    for data in enumerate(color_note_list):
        if 'white' in data[1]:
            count_w = count_w + 1
        else:
            count_b = count_b + 1

    return [count_w, count_b]


def next_sure_note(root_note, swp):
    count = 0
    save_root_position = 0

    for n in range(len(swp) - 1):
        if '.' not in swp[n] and root_note in swp[n]:
            save_root_position = n
            count = 1

        elif '.' not in swp[n] and root_note in swp[n - (n - save_root_position)] and count < 2:
            count = count + 1
            save = swp[n]

    return save


def get_short_list_of_notes_reverse(scale, sure, next_sure):
    result = listRightIndex(scale, next_sure) - scale.index(sure)
    short_list = get_short_list(result, scale, sure, next_sure)
    return short_list


def get_short_list(result, scale, sure, next_sure):
    short_list = []
    for x in range(result + 1):
        short_list.append(scale[scale.index(sure) + x])

    return short_list


def get_short_list_of_notes(sure, next_sure, scale):
    result = scale.index(next_sure) - scale.index(sure)
    short_list = []
    if result < 0:
        short_list = get_short_list_of_notes_reverse(scale, sure, next_sure)

    else:
        short_list = get_short_list(result, scale, sure, next_sure)
        return short_list

    return short_list


def get_scale_fixed(scale, swp, tone, scale_name):
    scales_wp = swp * 2
    scl = scale * 2

    for data in enumerate(scales_wp):
        if '.' not in data[1]:
            white_count = get_the_count_for_each_color(
                get_the_steps_for(
                    data[1],
                    next_sure_note(data[1], scales_wp),
                    take_all_notes_from(tone) + take_all_notes_from(tone)))[0]

            short_list = get_short_list_of_notes(
                data[1],
                next_sure_note(data[1], scales_wp),
                scales_wp)

            req = len(short_list) - 2

            if req > white_count:
                good_notes = return_good_notes(short_list)
                good_notes.append(i for i in short_list if '#' not in i)

                for e in range(len(good_notes) - 1):
                    scl[scl.index(good_notes[0]) + e] = good_notes[e]

        result = substract_fixed_scale(scl, scale_name)

    return result

def get_good_notes_into_array(arr, notes_collect, notes_onfly):
    if (notes_collect['second_note_first_char'] not in
            notes_collect['first_note'] and
            notes_collect['penultimate_note_fourth_char'] not in
            notes_collect['latest_note']):
        if notes_onfly['note_first_char'] in arr[len(arr) - 1]:
            arr.append(notes_onfly['note_with_bemol'])
        else:

            arr.append(notes_onfly['note_with_sharp'])
    elif (notes_onfly['note_fourth_char'] in notes_onfly['next_note'] and
          '#' not in notes_onfly['next_note'] or
          notes_collect['second_note_first_char'] not in
          notes_collect['first_note']):

        arr.append(notes_onfly['note_with_sharp'])
    else:
        '''(note_first_char in arr[len(arr) - 1] or
            second_note_first_char in first_note and
            penultimate_note_fourth_char not in latest_note)'''

        arr.append(notes_onfly['note_with_bemol'])

    return arr


def return_good_notes(short_list):
    reformated_notes_list = []
    notes_collect = {
        'first_note': short_list[0],
        'latest_note': short_list[-1],
        'second_note_first_char': short_list[1][0],
        'penultimate_note_fourth_char': short_list[-2][3]}

    for data in enumerate(short_list):
        if '.' in data[1]:
            notes_onfly = {
                'note_first_char': data[1][0],
                'note_fourth_char': data[1][3],
                'next_note': short_list[data[0] + 1],
                'note_with_sharp': data[1][0:2],
                'note_with_bemol': data[1][-2::]
            }

            reformated_notes_list = get_good_notes_into_array(reformated_notes_list,
                                                              notes_collect,
                                                              notes_onfly)
        else:
            reformated_notes_list.append(data[1])

    return reformated_notes_list


def fill_with_note_color(result, notes, first_note):
    list_of_color_notes = []
    for pos in range(result - 1):
        if '.' in notes[notes.index(first_note) + 1 + pos]:
            list_of_color_notes.append('black')

        else:
            list_of_color_notes.append('white')

    return list_of_color_notes



def get_the_steps_for(first_note, last_note, notes):
    if notes.index(last_note) - notes.index(first_note) < 0:
        return fill_with_note_color(
            listRightIndex(notes, last_note) - notes.index(first_note),
            notes,
            first_note)
    else:
        if notes.index(last_note) - notes.index(first_note) != 0:
            return fill_with_note_color(
                notes.index(last_note) - notes.index(first_note),
                notes,
                first_note)


def gen_double_note(_note):
    notes = init_all_notes()
    for note in notes:
        if _note in note:
            return note

def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) - 1


def standar_proccess(scale_list, tone, scale):
    out_scale = substract_scale(
        scan_duplicates(
            scan_duplicates(
                setup_scale(scale_list, tone), scale_list + scale_list),
            scale_list + scale_list),
        scale)

    if (is_there_any_duplicate(out_scale) and
            'cromatic' not in scale and
            'semitono_a_tono' not in scale and
            'tono_a_semitono' not in scale):

        return get_scale_fixed(out_scale,
                               substract_scale(scale_list + scale_list, scale),
                               tone,
                               scale)

    else:
        return out_scale
