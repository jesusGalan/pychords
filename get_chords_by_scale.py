from chords import get_chord_name

from scales import get_list_of_grades_by, get_notes_of, parse_scales_json_to_python


def own_sort(grades_list, grade):
    # random list
    while (grades_list[0] != grade):
        poped_item = grades_list.pop(0)
        grades_list.append(poped_item)

    return grades_list


def get_data_by(note_selected, scale, deep):
    '''
        Saco chords con get_chord_name(note, scale, type_of_chord):
    '''

    list_of_notes = get_notes_of(scale, note_selected)

    json = parse_scales_json_to_python()
    for _scale in json:

        list_grades = get_list_of_grades_by(_scale)

        for _grade in list_grades:
            if (scale == _grade):
                _good_list = own_sort(list_grades, _grade)

    _result = []

    for x in range(0, len(_good_list)):
        _result.append(get_chord_name(list_of_notes[x], _good_list[x], deep))

    return _result


'''if __name__ == __name__:
    get_data_by(sys.argv[2], sys.argv[1])'''
