# -*- coding: utf-8 -*-

import sys
from functions import *


def get_notes_of(scale_name, tone):
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


if __name__ == '__main__':
    for i in enumerate(get_notes_of(sys.argv[1], sys.argv[2])):
        print i[1]
