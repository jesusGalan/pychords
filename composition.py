import sys

from scales import get_notes_of, get_scale_name_list, get_list_of_grades_by
from chords import get_chord_name


def get_scale_names_according_to(scale_name, mom_scale):
    position_of_selected_scale = get_list_of_grades_by(mom_scale).index(scale_name)
    result_list_first = []
    result_list_second = []

    for position in range(position_of_selected_scale):
        result_list_first.append(get_list_of_grades_by(mom_scale)[position])

    for grades in enumerate(get_list_of_grades_by(mom_scale)):
        if grades[0] >= position_of_selected_scale:
            result_list_second.append(grades[1])

    return result_list_second + result_list_first


def get_empty_dict_with_grades(json_data):
    return {json_data[0]: [],
            json_data[1]: [],
            json_data[2]: [],
            json_data[3]: [],
            json_data[4]: [],
            json_data[5]: [],
            json_data[6]: []}


def get_grades_correspondencies(json_data):
    return {0: json_data[0],
            1: json_data[1],
            2: json_data[2],
            3: json_data[3],
            4: json_data[4],
            5: json_data[5],
            6: json_data[6]}


def get_simple_table_with_grades_and_notes_by(mom_scale, note_selected):
    list_of_grades = get_list_of_grades_by(mom_scale)
    result_notes = get_empty_dict_with_grades(list_of_grades)
    result_grade_names = get_empty_dict_with_grades(list_of_grades)
    result = get_empty_dict_with_grades(list_of_grades)

    for scale in enumerate(get_list_of_grades_by(mom_scale)):
        notes = get_notes_of(get_list_of_grades_by(mom_scale)[0], note_selected)
        for note in enumerate(get_notes_of(scale[1], notes[scale[0]])):
            result_notes[scale[1]].append(note[1])
            result_grade_names[scale[1]].append(
                get_scale_names_according_to(scale[1], mom_scale)[note[0]])

        result[scale[1]].append((result_grade_names[scale[1]]))
        result[scale[1]].append((result_notes[scale[1]]))

    return result


def get_modal_interchange_data_by(mom_scale, note_selected):
    list_of_grades = get_list_of_grades_by(mom_scale)
    result_notes = get_empty_dict_with_grades(list_of_grades)
    result_grade_names = get_empty_dict_with_grades(list_of_grades)
    result = get_empty_dict_with_grades(list_of_grades)

    for scale in enumerate(get_list_of_grades_by(mom_scale)):
        for note in enumerate(get_notes_of(scale[1], note_selected)):
            result_notes[scale[1]].append(note[1])
            result_grade_names[scale[1]].append(
                get_scale_names_according_to(scale[1], mom_scale)[note[0]])

        result[scale[1]].append((result_grade_names[scale[1]]))
        result[scale[1]].append((result_notes[scale[1]]))

    return result


def fill_scale_data_in_object(result_dict, mom_scale, type_of_chord):
    list_of_grades = get_list_of_grades_by(mom_scale)
    correspondencies = get_grades_correspondencies(list_of_grades)
    result_correspondencies = {
        'scale_grades': [],
        'scale_notes': [],
        'scale_chords': []
    }

    for scale_result in correspondencies:
        result_correspondencies['scale_grades'].append(correspondencies[scale_result])

        result_correspondencies['scale_notes'].append(
            result_dict[correspondencies[scale_result]][1])

        result_correspondencies['scale_chords'].append([])

        for correspondency in enumerate(result_dict[correspondencies[scale_result]][1]):
            result_correspondencies['scale_chords'][scale_result].append(
                get_chord_name(correspondency[1],
                               get_scale_names_according_to(
                                   correspondencies[scale_result], mom_scale)[correspondency[0]], type_of_chord)
            )

    return result_correspondencies


def resort_scales(init_dict):
    chords_lists = init_dict['scale_chords']
    result = []

    for chord_list in enumerate(chords_lists):
        result.append(move_array_to_right(chord_list[1], chord_list[0]))

    init_dict['scale_chords'] = result

    return init_dict


def move_array_to_right(init_array, moves):
    correspondencies = {
        0: [init_array[0], init_array[1], init_array[2], init_array[3],
            init_array[4], init_array[5], init_array[6]],

        1: [init_array[6], init_array[0], init_array[1], init_array[2],
            init_array[3], init_array[4], init_array[5]],

        2: [init_array[5], init_array[6], init_array[0], init_array[1],
            init_array[2], init_array[3], init_array[4]],

        3: [init_array[4], init_array[5], init_array[6], init_array[0],
            init_array[1], init_array[2], init_array[3]],

        4: [init_array[3], init_array[4], init_array[5], init_array[6],
            init_array[0], init_array[1], init_array[2]],

        5: [init_array[2], init_array[3], init_array[4], init_array[5],
            init_array[6], init_array[0], init_array[1]],

        6: [init_array[1], init_array[2], init_array[3], init_array[4],
            init_array[5], init_array[6], init_array[0]]
    }

    return correspondencies[moves]


def get_data_to_visualize(filled_object, mark):
    note_wrapper = ''

    if 'vertical' in mark:
        note_wrapper += "\n --------------------------------------------------Vertical-----------------------------------------------------\n\n"
        note_wrapper += '|    jonicos    |    doricos    |    frigios    |    lidios     |  mixolidios   |    eolicos    |    locrios    |\n'
        note_wrapper += ' =============== =============== =============== =============== =============== =============== ==============='
    else:
        note_wrapper += "\n --------------------------------------------------Horizontal---------------------------------------------------\n"

    for chords in enumerate(filled_object['scale_chords']):
        note_wrapper += '\n'
        for chord in enumerate(chords[1]):
            if str(((15 - len(chord[1])) / 2.0)).split('.')[1] == '5':
                try:
                    note_wrapper += '|' + ' ' * (
                            (15 - len(chord[1])) / 2) + chord[1] + ' ' * ((16 - len(chord[1])) / 2)
                except TypeError:
                    note_wrapper += '|' + ' ' * (
                            (15 - len(chord[1][0])) / 2) + chord[1][0] + ' ' * ((16 - len(chord[1][0])) / 2)
            else:
                note_wrapper += '|' + ' ' * (
                        (15 - len(chord[1])) / 2) + chord[1] + ' ' * ((15 - len(chord[1])) / 2)

        note_wrapper += '|'

    return note_wrapper


def visualize_modal_vertical_sort():
    return get_data_to_visualize(
        resort_scales(
            fill_scale_data_in_object(
                get_modal_interchange_data_by(sys.argv[1], sys.argv[2]), sys.argv[1], int(sys.argv[3]))), 'vertical')


def visualize_modal_horizontal_sort():
    return get_data_to_visualize(
        fill_scale_data_in_object(
            get_modal_interchange_data_by(sys.argv[1], sys.argv[2]), sys.argv[1], int(sys.argv[3])), 'horizontal')


if __name__ == __name__:
    print(visualize_modal_vertical_sort())
    print(visualize_modal_horizontal_sort())
    print(
        '\n --------------------------------------------------------------------------------------------------------------- \n')
