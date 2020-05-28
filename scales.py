import os
import sys
import json
from collections import OrderedDict

from functions import read_scales_from_json, take_all_notes_from, standar_proccess
from intervals import get_identic_nomenclature

SCALES_JSON_PATH = os.path.join(os.path.dirname(__file__), 'scales_repository/scales.json')


def get_notes_of(scale_name, tone):
    if ("%" in tone):
        tone = tone.replace('%', '#').capitalize()

    """This method can get all notes of a scale from a tone center"""
    note_list = take_all_notes_from(tone)
    
    note_list = note_list + note_list
    scale_list = config_scale(note_list, scale_name, tone)

    return scale_list


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


def read_formula(scale):
    scales_dict = json.loads(read_scales_from_json(SCALES_JSON_PATH), object_pairs_hook=OrderedDict)
    for key in scales_dict.items():
        if scale in key[1]:
            scale_formula = key[1][scale]

    return scale_formula


def get_list_of_grades_by(mom_scale):
    scales_dict = json.loads(read_scales_from_json(SCALES_JSON_PATH), object_pairs_hook=OrderedDict)
    scales_resulted = []
    for key in scales_dict.items():
        if mom_scale in key[0]:
            for scale in key[1]:
                scales_resulted.append(scale)

    return scales_resulted


def parse_scales_json_to_python():
    with open(SCALES_JSON_PATH, 'rb') as _file:
        json_content = json.loads(_file.read(), object_pairs_hook=OrderedDict)

        _file.close()

    return json_content


def get_scale_name_list():
    json_content = parse_scales_json_to_python()

    scale_name_list = []
    for key in json_content:
        scale_name_list.append(key.replace('_', ' '))

    return scale_name_list


def get_grade_name_list_of_scale(scale):
    """I think that should remove it"""
    json_content = parse_scales_json_to_python()

    grade_name_list = []
    for k in json_content.get(scale):
        grade_name_list.append(k.replace('_', ' '))

    return grade_name_list


def scales(scale_name, tone):
    note_list = take_all_notes_from(tone)
    note_list = note_list + note_list
    scale_list = config_scale(note_list, scale_name, tone)

    return scale_list


def get_tone_name_list_of_grade(grade):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    result = []
    for note in notes:
        result.append({note: scales(grade, note)})
    return result


if __name__ == '__main__':
    for note in enumerate(get_notes_of(sys.argv[1], sys.argv[2])):
        print(note[1])
