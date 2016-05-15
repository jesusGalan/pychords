# -*- coding: utf-8 -*-

import json
import sys
import os
from collections import OrderedDict


SCALES_JSON_PATH = os.path.join(os.path.dirname(__file__), 'scales.json')
POSITIONS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'positions.json')


def scales(scale_name, tone):
    note_list = take_all_notes_from(tone)
    note_list = note_list + note_list
    scale_list = config_scale(note_list, scale_name, tone)

    return scale_list


def take_all_notes_from(tone):
    notes = ['C', 'C#.Db', 'D', 'D#.Eb', 'E', 'F', 'F#.Gb', 'G', 'G#.Ab', 'A', 'A#.Bb', 'B']
    pos_tone = take_position(tone, notes)
    notes = notes + notes
    new_notes = []
    for x in range(len(notes)):
        if(x >= pos_tone and x < pos_tone + 12):
            new_notes.append(notes[x])

    return new_notes


def config_scale(note_list, scale, tone):
    scales_dict = read_formula(scale)
    scale_list = []
    ref = 0

    for e in range(len(scales_dict)):

        try:
            scale_list.append(note_list[ref])

        except IndexError:
            return 'Error: ', tone, ' no existe.'

        ref = ref + scales_dict[e]

    out_scale = standar_proccess(scale_list, tone, scale)

    return out_scale


def get_the_pos_for(alt, tone, notes):

    if alt == 'b':
        for x in range(len(notes)):
            if '.' in notes[x]:
                if tone in notes[x] and ('b' in tone or '#' not in tone):
                    _pos_tone = x - 1
            else:
                if tone in notes[x]:
                    _pos_tone = x

    elif alt == '#':
        for x in range(len(notes)):
            if tone in notes[x]:
                _pos_tone = x + 1
    else:
        for x in range(len(notes)):
            if '.' in notes[x]:
                pass
            else:
                if tone in notes[x]:
                    _pos_tone = x + 1

    return _pos_tone


def return_pos_tone(tone, notes):
    if "b" in tone:
        tone = tone[0:1]
        pos_tone = get_the_pos_for('b', tone, notes)

    elif "#" in tone:
        tone = tone[0:1]
        pos_tone = get_the_pos_for('#', tone, notes)

    else:
        pos_tone = get_the_pos_for(None, tone, notes)

    return pos_tone


def take_position(tone, notes):
    tones_to_not_take_position = ['Fb', 'Cb', 'E#', 'B#']

    if tone not in tones_to_not_take_position:
        pos_tone = return_pos_tone(tone, notes) - 1

        return pos_tone

def get_index_of_notes_without_sharps_or_bemols(scale_list):
    return [scale_list.index(i) for i in scale_list if '#' not in i]


def setup_scale(scale, tone):
    out_list = scale + scale
    sures = get_index_of_notes_without_sharps_or_bemols(out_list)

    if len(sures) != len(out_list):
        for n in range(len(out_list)):
            if '.' in out_list[n]:
                out_list[n] = out_list[n].split('.')[0]

    return out_list


def substract_scale(scale, name_of_scale):
    if name_of_scale in 'escala_cromatica':
        return [scale[0], scale[1], scale[2], scale[3], scale[4], scale[5], scale[6], scale[7], scale[8], scale[9], scale[10], scale[11]]

    elif name_of_scale in 'escala_tono_a_tono' or 'escala_hexatonica_de_blues' in name_of_scale:
        return [scale[6], scale[7], scale[8], scale[9], scale[10], scale[5]]

    elif name_of_scale in 'escala_semitono_a_tono' or name_of_scale in 'escala_tono_a_semitono':
        return [scale[8], scale[9], scale[10], scale[11], scale[12], scale[13], scale[14], scale[15]]

    else:
        return [scale[7], scale[8], scale[9], scale[10], scale[11], scale[12], scale[6]]


def substract_fixed_scale(scale, scale_name):
    if 'escala_hexatonica_de_blues' in scale_name:
        return [scale[6], scale[7], scale[8], scale[3], scale[10], scale[5]]

    else:
        return [scale[7], scale[8], scale[9], scale[3], scale[11], scale[12], scale[6]]


def scan_duplicates_for_sost_scales(scale, scale_with_points):
    scale_relist = scale
    # Scan a duplicate in left note for first scale aproximation
    for n in range(len(scale) - 1):
        if '.' in scale_with_points[n]:
            if scale_with_points[n][0:1] in scale[n - 1]:
                scale_relist[n] = scale_with_points[n].split('.')[1]

    return scale_relist


def scan_duplicates_for_bemol_scales(scale, scale_with_points):
    scale_relist = scale
    # Scan a duplicate in left note for first aproximation
    for n in range(len(scale) - 1):
        if '.' in scale_with_points[n]:
            if scale[n][0:1] in scale[n + 1] and scale_with_points[n][0:1] not in scale[n - 1]:
                scale_relist[n] = scale_with_points[n].split('.')[0]

    return scale_relist


def get_dup_persist(scale):
    scales = scale
    arg = False
    # Scales that going to repeat some note need to be invested under new behaviours
    for n in range(len(scales) - 1):
        if 6 > n > 0:
            if scales[n][0:1] in scales[n - 1]:
                arg = True

        else:
            if scales[0][0:1] in scales[len(scales) - 1][0:1]:
                arg = True

    return arg


def get_list_of_sures(swp):
    sures = get_index_of_notes_without_sharps_or_bemols(swp)
    result_list = []

    for n in range(len(sures) - 1):
        if n == 0:
            append = str(0) + '-' + str(sures[n] + 1)
            result_list.append(append)

        elif n == len(sures) - 1:
            append = str(sures[n - 1]) + '-' + str(13)
            result_list.append(append)

        else:
            append = str(sures[n - 1] + 1) + '-' + str(sures[n] + 1)
            result_list.append(append)

    return result_list


def get_some_notes_changed(scale, scale_with_points, tone, scale_name):
    scl = scale + scale
    notes = take_all_notes_from(tone)
    swp = scale_with_points + scale_with_points
    sures = get_index_of_notes_without_sharps_or_bemols(swp)
    list_of_required_notes = []

    list_of_sure_notes = []

    for n in range(len(sures)):
        list_of_sure_notes.append(scl[sures[n]])

    steps = []
    new_sure_list = get_list_of_sures(swp)

    for n in range(len(new_sure_list)):
        try:
            steps.append(get_the_steps_for(swp[int(new_sure_list[n].split('-')[1]) - 1], swp[int(new_sure_list[n + 1].split('-')[1]) - 1], notes + notes))

        except IndexError:
            pass

    for n in range(len(new_sure_list)):
        if n > 0:
            list_of_required_notes.append(int(new_sure_list[n].split('-')[1]) - int(new_sure_list[n].split('-')[0]) - 1)

    list_with_changes = get_changes(get_the_count_for_each_color(steps), list_of_required_notes, scale, scale_with_points, tone, scale_name)

    return list_with_changes


def get_the_count_for_each_color(color_note_list):
    count_w = 0
    count_b = 0

    for n in range(len(color_note_list)):
        if 'blanca' in color_note_list[n]:
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


def get_short_list_procedure(result, scale, sure, next_sure):
    if result < 0:
        short_list = get_short_list_of_notes_reverse(scale, sure, next_sure)

    else:
        if result != 0:
            short_list = get_short_list(result, scale, sure, next_sure)
            return short_list

    return short_list


def get_short_list_of_notes(sure, next_sure, scale):
    result = scale.index(next_sure) - scale.index(sure)
    short_list = get_short_list_procedure(result, scale, sure, next_sure)

    return short_list


def get_changes(color_of_not_sure_notes, req, scale, swp, tone, scale_name):
    scales_wp = swp * 2
    scl = scale * 2
    sures = get_index_of_notes_without_sharps_or_bemols(scales_wp)
    not_processed_scale = take_all_notes_from(tone)
    not_processed_scale = not_processed_scale + not_processed_scale

    for i in range(len(scales_wp)):
        if '.' not in scales_wp[i]:
            sure = scales_wp[i]
            next_sure = next_sure_note(sure, scales_wp)
            white_count = get_the_count_for_each_color(get_the_steps_for(sure, next_sure, not_processed_scale))
            short_list = get_short_list_of_notes(sure, next_sure, scales_wp)
            req = len(short_list) - 2

            if req > white_count[0]:
                good_notes = return_good_notes(short_list)
                good_notes.append(i for i in short_list if not '#' in i)

                for e in range(len(good_notes) - 1):
                    scl[scl.index(good_notes[0]) + e] = good_notes[e]

        result = substract_fixed_scale(scl, scale_name)

    return result


def return_good_notes(short_list):
    reformated_notes_list = []

    first_note = short_list[0]
    latest_note = short_list[-1]
    second_note_first_char = short_list[1][0]
    penultimate_note_fourth_char = short_list[-2][3]

    for x in range(len(short_list)):
        if '#' in short_list[x]:
            note_first_char = short_list[x][0]
            note_fourth_char = short_list[x][3]
            previous_note = short_list[x - 1]
            next_note = short_list[x + 1]
            note_with_sharp = short_list[x][0:2]
            note_with_bemol = short_list[x][-2::]

            if second_note_first_char not in first_note and penultimate_note_fourth_char not in latest_note:

                if note_first_char in reformated_notes_list[len(reformated_notes_list) - 1]:
                    reformated_notes_list.append(note_with_bemol)

                else:
                    reformated_notes_list.append(note_with_sharp)

            elif note_fourth_char in next_note and '#' not in next_note:
                reformated_notes_list.append(note_with_sharp)

            elif note_first_char in reformated_notes_list[len(reformated_notes_list) - 1]:
                reformated_notes_list.append(note_with_bemol)

            elif second_note_first_char not in first_note:

                reformated_notes_list.append(note_with_sharp)

            elif penultimate_note_fourth_char in latest_note:
                reformated_notes_list.append(note_with_sharp)

            elif second_note_first_char in first_note and penultimate_note_fourth_char not in latest_note:
                reformated_notes_list.append(note_with_bemol)

            else:
                reformated_notes_list.append(note_with_sharp)

        else:
            reformated_notes_list.append(short_list[x])

    return reformated_notes_list


def get_the_steps_for(first_note, last_note, notes):
    color = None
    list_of_color_notes = []
    result = notes.index(last_note) - notes.index(first_note)

    if result < 0:
        result = listRightIndex(notes, last_note) - notes.index(first_note)

        for x in range(result - 1):
            if '.' in notes[notes.index(first_note) + 1 + x]:
                list_of_color_notes.append('negra')

            else:
                list_of_color_notes.append('blanca')

    else:
        if result == 0:
            list_of_color_notes = []

        else:
            for x in range(result - 1):
                if '.' in notes[notes.index(first_note) + 1 + x]:
                    list_of_color_notes.append('negra')
                else:
                    list_of_color_notes.append('blanca')

    return list_of_color_notes


def listRightIndex(alist, value):
    return len(alist) - alist[-1::-1].index(value) - 1


def read_scales_from_json(SCALES_JSON_PATH):
    with open(SCALES_JSON_PATH, 'rb') as f:
        content = f.read()

    return content


def read_formula(scale):
    scales_dict = json.loads(read_scales_from_json(SCALES_JSON_PATH), object_pairs_hook=OrderedDict)
    for key, value in scales_dict.items():
        if scale in value:
            scale_formula = value[scale]

    return scale_formula


def standar_proccess(scale_list, tone, scale):
    scale_only_sost = setup_scale(scale_list, tone)
    scale_relisted = scale_list + scale_list
    list_reconfigured = scan_duplicates_for_sost_scales(scale_only_sost, scale_relisted)

    list_last_config = scan_duplicates_for_bemol_scales(list_reconfigured, scale_relisted)
    out_scale = substract_scale(list_last_config, scale)
    duplicate_persistance = get_dup_persist(out_scale)

    if duplicate_persistance is True and 'cromatic' not in scale and 'semitono_a_tono' not in scale and 'tono_a_semitono' not in scale:
        out_scale_reconfigured = get_some_notes_changed(out_scale, substract_scale(scale_relisted, scale), tone, scale)
    else:
        out_scale_reconfigured = out_scale

    return out_scale_reconfigured


def debug_scale(scale):
    notes = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']
    result = {}

    for note in notes:
        result[scale + ' tone ' + note + ':'] = scales(scale, note)

    return display_debug(result)


def display_debug(result):
    res = ''
    for key, value in result.items():
        res = res + key
        for x in range(len(value)):
            if 'b' in value[x] or '' in value[x]:
                res = res + ' ' + value[x] + ' '
            else:
                res = res + '  ' + value[x] + ' '
        res = res + '\n'
    return res


def get_scale_name_list():
    json_content = parse_scales_json_to_python()

    scale_name_list = []
    for key in json_content:
        scale_name_list.append(key.replace('_', ' '))

    return scale_name_list


def get_grade_name_list_of_scale(scale):
    json_content = parse_scales_json_to_python()

    grade_name_list = []
    for k in json_content.get(scale):
        grade_name_list.append(k.replace('_', ' '))

    return grade_name_list


def parse_scales_json_to_python():
    with open(SCALES_JSON_PATH, 'rb') as _file:
        json_content = json.loads(_file.read(), object_pairs_hook=OrderedDict)

        # sanitize check
        _file.close()

    return json_content


def get_tone_name_list_of_grade(grade):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    result = []

    for note in notes:
        result.append({note: scales(grade, note)})

    return result


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
def get_identic_nomenclature(element):
    if element == '1':
        return '1'

    elif element == 'b2':
        return 'b9'

    elif element == '2':
        return 'bb3'

    elif element == 'b3':
        return '#2'

    elif element == '3':
        return 'b4'

    elif element == '4':
        return 'bb5'

    elif element == 'b5':
        return '#4'

    elif element == '5':
        return 'bb6'

    elif element == 'b6':
        return '#5'

    elif element == '6':
        return 'bb7'

    elif element == 'b7':
        return '#6'

    elif element == '7':
        return '7'

    elif element == 'b9':
        return 'b2'

    elif element == 'bb3':
        return '2'

    elif element == '#2':
        return 'b3'

    elif element == 'b4':
        return '3'

    elif element == 'bb5':
        return '4'

    elif element == '#4':
        return 'b5'

    elif element == 'bb6':
        return '5'

    elif element == '#5':
        return 'b6'

    elif element == 'bb7':
        return '6'

    elif element == '#6':
        return 'b7'

    else:
        return None


def show_scale_for_positions(position_list):
    scales_dict = json.loads(read_scales_from_json(POSITIONS_JSON_PATH))
    _list = []

    for key, value in scales_dict.items():

        for scale in range(len(value.items())):
            count = 0

            for position in value.items()[scale][1]:

                for element in position_list:

                    if position == element:
                        count = count + 1

                    else:
                        identic_element = get_identic_nomenclature(element)
                        if identic_element == None:
                            print 'No se que es: ', element
                            print '\n'
                            exit()
                        if position == identic_element:
                            count = count + 1


            if count == len(position_list):

                if 'cromatic' not in value.items()[scale][0]:
                    _list.append(value.items()[scale][0])

            else:
                pass

    return _list


def show_scale_for_notes(note_list):
    pass

if __name__ == '__main__':
    _list = []
    for argument in range(len(sys.argv)):
        if argument > 0:
            _list.append(sys.argv[argument])

    print '\n'
    for x in show_scale_for_positions(_list):
        print x
    print '\n'
