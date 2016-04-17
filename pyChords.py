# -*- coding: utf-8 -*-

import json
import sys


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
                    pos_tone = x - 1
            else:
                if tone in notes[x]:
                    pos_tone = x

    elif alt == '#':
        for x in range(len(notes)):
            if tone in notes[x]:
                pos_tone = x + 1
    else:
        for x in range(len(notes)):
            if '.' in notes[x]:
                pass
            else:
                if tone in notes[x]:
                    pos_tone = x + 1

    return pos_tone


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
    if tone == 'Fb' or tone == 'Cb' or tone == 'E#' or tone == 'B#':
        pass
    else:
        pos_tone = return_pos_tone(tone, notes)
    try:
        return pos_tone - 1
    except UnboundLocalError:
        return 'Error: ', tone, ' no existe.'


def search_sure_notes(scale_list):
    sures = []
    for z in range(len(scale_list)):
        if "." not in scale_list[z]:
            sures.append(z)
    return sures


def setup_scale(scale, tone):
    out_list = scale + scale
    sures = search_sure_notes(out_list)

    if len(sures) != len(out_list):
        for n in range(len(out_list)):
            if '.' in out_list[n]:
                out_list[n] = out_list[n].split('.')[0]

    return out_list


def substract_scale(scale, name_of_scale):
    if name_of_scale in 'escala_cromatica':
        return [scale[0], scale[1], scale[2], scale[3], scale[4], scale[5], scale[6], scale[7], scale[8], scale[9], scale[10], scale[11]]
    else:
        return [scale[7], scale[8], scale[9], scale[10], scale[11], scale[12], scale[6]]


def substract_fixed_scale(scale):
    return [scale[7], scale[8], scale[9], scale[3], scale[11], scale[12], scale[6]]


def scan_duplicates_for_sost_scales(scale, scale_with_points):
    scale_relist = scale
    # Scan a duplicate in left note for first scale aproximation
    for n in range(len(scale)):
        if 13 > n > 0:
            if '.' in scale_with_points[n]:
                if scale_with_points[n][0:1] in scale[n - 1]:
                    scale_relist[n] = scale_with_points[n].split('.')[1]

    return scale_relist


def scan_duplicates_for_bemol_scales(scale, scale_with_points):
    scale_relist = scale
    # Scan a duplicate in left note for first aproximation
    for n in range(len(scale)):
        if 13 > n > 0:
            if '.' in scale_with_points[n]:
                if scale[n][0:1] in scale[n + 1] and scale_with_points[n][0:1] not in scale[n - 1]:
                    scale_relist[n] = scale_with_points[n].split('.')[0]

    return scale_relist


def get_dup_persist(scale):
    scales = scale
    arg = False
    # Scales that going to repeat some note need to be invested under new behaviours
    for n in range(len(scales)):
        if 6 > n > 0:
            if scales[n][0:1] in scales[n - 1]:
                arg = True

        else:
            if scales[0][0:1] in scales[6][0:1]:
                arg = True

    return arg


def get_list_of_sures(swp):
    sures = search_sure_notes(swp)
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


def get_some_notes_changed(scale, scale_with_points, tone):
    scl = scale + scale
    notes = take_all_notes_from(tone)
    swp = scale_with_points + scale_with_points
    sures = search_sure_notes(swp)
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

    list_with_changes = get_changes(get_the_count_for_each_color(steps), list_of_required_notes, scale, scale_with_points, tone)

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


def get_required_notes(short_scale):
    count = 0
    for note in short_scale:
        if '.' in note:
            count = count + 1

    return count


def get_short_list_of_notes(sure, next_sure, scale_with_points_double):
    short_list = []
    result = scale_with_points_double.index(next_sure) - scale_with_points_double.index(sure)
    if result < 0:
        result = listRightIndex(scale_with_points_double, next_sure) - scale_with_points_double.index(sure)

        for x in range(result + 1):
            short_list.append(scale_with_points_double[scale_with_points_double.index(sure) + x])

    else:
        if result != 0:
            for x in range(result + 1):
                short_list.append(scale_with_points_double[scale_with_points_double.index(sure) + x])

    return short_list


def get_changes(color_of_not_sure_notes, req, scale, swp, tone):
    scales_wp = swp + swp
    scl = scale + scale
    sures = search_sure_notes(scales_wp)
    not_processed_scale = take_all_notes_from(tone)
    not_processed_scale = not_processed_scale + not_processed_scale

    for n in range(len(scales_wp)):
        if '.' in scales_wp[n]:
            pass
        else:
            sure = scales_wp[n]
            next_sure = next_sure_note(sure, scales_wp)
            white_count = get_the_count_for_each_color(get_the_steps_for(sure, next_sure, not_processed_scale))
            short_list = get_short_list_of_notes(sure, next_sure, scales_wp)
            req = len(short_list) - 2

            if req > white_count[0]:
                good_notes = return_good_notes(short_list)
                for t in range(len(good_notes) - 1):
                    scl[scl.index(good_notes[0]) + t] = good_notes[t]

            result = substract_fixed_scale(scl)
    try:
        return result
    except UnboundLocalError:
        return result


def return_good_notes(short_list):
    lista_buena = []

    for x in range(len(short_list)):
        if '.' in short_list[x]:

            if short_list[1].split('.')[0][0:1] not in short_list[0] and short_list[len(short_list) - 2].split('.')[1][0:1] not in short_list[len(short_list) - 1]:
                lista_buena.append(short_list[x].split('.')[0])

            else:
                if short_list[1].split('.')[0][0:1] not in short_list[0] and short_list[len(short_list) - 2].split('.')[1][0:1] in short_list[len(short_list) - 1]:
                    lista_buena.append(short_list[x].split('.')[0])

                elif short_list[1].split('.')[0][0:1] in short_list[0] and short_list[len(short_list) - 2].split('.')[1][0:1] not in short_list[len(short_list) - 1]:
                    lista_buena.append(short_list[x].split('.')[1])

                else:
                    if short_list[x].split('.')[0][0:1] in short_list[x - 1] and short_list[x].split('.')[1][0:1] + '#' in short_list[x + 1].split('.')[0]:
                        if short_list[x].split('.')[0][0:1] in lista_buena[len(lista_buena) - 1]:
                            lista_buena.append(short_list[x].split('.')[1])
                        else:
                            lista_buena.append(short_list[x].split('.')[0])
                    else:
                        if short_list[x].split('.')[0][0:1] in lista_buena[len(lista_buena) - 1]:
                            if short_list[x].split('.')[1][0:1] in short_list[x + 1] and '.' not in short_list[x + 1]:
                                lista_buena.append(short_list[x].split('.')[0])
                            else:
                                lista_buena.append(short_list[x].split('.')[1])
                        else:
                            lista_buena.append(short_list[x].split('.')[0])
        else:
            lista_buena.append(short_list[x])

    return lista_buena


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


def read_scales_from_json():
    with open('scales.json', 'rb') as f:
        content = f.read()

    return content


def read_formula(scale):
    # read json scale file
    scales_dict = json.loads(read_scales_from_json())
    # get the formula

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

    if duplicate_persistance is True and 'cromatic' not in scale:
        out_scale_reconfigured = get_some_notes_changed(out_scale, substract_scale(scale_relisted, scale), tone)
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
            if 'b' in value[x] or '#' in value[x]:
                res = res + ' ' + value[x] + ' '
            else:
                res = res + '  ' + value[x] + ' '
        res = res + '\n'
    return res

if __name__ == '__main__':

    print '\n'
    print debug_scale(str(sys.argv[1]))
