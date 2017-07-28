
import os
import sys
import json

from pychords.functions import read_scales_from_json

INTERVALS_JSON_PATH = os.path.join(os.path.dirname(__file__), 'scales_repository/intervals.json')

def get_intervals_from_json():
    return json.loads(read_scales_from_json(INTERVALS_JSON_PATH))

def get_nomenclatures():
    '''List of possible nomenclatures'''
    return {'1': '1', 'b2': 'b9', '2': 'bb3', '#2': 'b3',
            'bb3': '2', 'b3': '#2', '3': 'b4', '#3': '4',
            'b4': '3', '4': 'bb5', '#4': 'b5', 'b5': '#4',
            '5': 'bb6', '#5': 'b6', 'b6': '#5', '6': 'bb7',
            '#6': 'b7', 'b7': '#6', '8': '1', 'b9': 'b2',
            '9': '2', '#9': '#2', 'bb10': 'bb3', 'b10': 'b3',
            '10': '3', '#10': '#3', 'b11': 'b4', '11': '4',
            '#11': '#4', 'b12': 'b5', '12': '5', '#12': '#5',
            'b13': 'b6', '13': '6', '#13': '#6', 'b14': 'b7',
            '14': '7'}

def get_identic_nomenclature(element):
    '''Search enarmonics.'''
    try:
        return get_nomenclatures()[element]

    except KeyError:
        if element == '7':
            return element
        print 'no se que es ', element
        exit()

def get_scale_by_selected_intervals(position_list):
    ''' Get the grades implicated on the selected intervals'''
    
    scales_dict = get_intervals_from_json()
    _list = []

    for key in scales_dict.items():
        for scale in range(len(scales_dict[key[0]].items())):
            count = count_positions(scales_dict[key[0]].items()[scale][1], position_list)

            if (count == len(position_list) and
                    'cromatic' not in scales_dict[key[0]].items()[scale][0]):
                _list.append(scales_dict[key[0]].items()[scale][0])

    return _list
    
def count_positions(key, position_list):
    count = 0

    for position in key:
        for element in position_list:
            if position != element:
                if position == get_identic_nomenclature(element):
                    count += 1

            else:
                count += 1

    return count

if __name__ == '__main__':
    _list = []
    for argument in range(len(sys.argv)):
        if argument > 0:
            _list.append(sys.argv[argument])

    print '\n'
    for x in get_scale_by_selected_intervals(_list):
        print x
    print '\n'