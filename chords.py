''' chords formatter from json '''

# -*- coding: utf-8 -*-

import os
import sys
import json

from functions import read_scales_from_json


CHORDS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'scales_repository/chords.json')

def get_chords_from_json():
    return json.loads(read_scales_from_json(CHORDS_JSON_PATH))

def get_dict_of_alternatives(type_of_chord, intervals):
    alternatives = {'0': [],
                    '1': []}

    for alts in range(2):
        for pos in range(type_of_chord):
            alternatives[str(alts)].append(intervals[alts][pos])

    return alternatives

def get_string_of_nomenclature(type_of_chord, intervals):
    chord_nomenclature = ''
    for pos in range(type_of_chord):
        try:
            chord_nomenclature += intervals[pos]
        except IndexError:
            chord_nomenclature += intervals[pos][0]

    return chord_nomenclature

def get_alternative_results(note, alternatives, type_of_chord):
    result = []

    for pose in range(len(alternatives)):
        result.append('')

    chord = []
    for pose in range(len(alternatives)):
        chord.append("")
        for type_pos in range(type_of_chord):
            chord[pose] += alternatives[str(pose)][type_pos]

        result[pose] += note + chord[pose]

    return result


def show_chords_names_for_scale(scale_selected):
    ''' Can return a list with the names of chords'''
    scales_dict = get_chords_from_json()
    _list = []

    for key in scales_dict.items():
        for scale_values in scales_dict[key[0]].items():
            if scale_values[0] == scale_selected:
                for i in enumerate(scale_values[1]):
                    _list.append(scale_values[1][i[0]])

    return _list


def get_chord_name(note, scale, type_of_chord):
    ''' Can get chords of a selected scale and selected tenses'''
    intervals = show_chords_names_for_scale(scale)
    have_scale_alternative = (scale == 'escala_alterada' or
                              scale == 'escala_tono_a_tono' or
                              scale == 'escala_semitono_a_tono')

    if have_scale_alternative:
        alternatives = get_dict_of_alternatives(type_of_chord, intervals)
        result = get_alternative_results(note, alternatives, type_of_chord)

        return result

    else:
        chord_nomenclature = get_string_of_nomenclature(type_of_chord, intervals)

        return note + chord_nomenclature

if __name__ == '__main__':
    print(get_chord_name(sys.argv[2], sys.argv[1], int(sys.argv[3])))
