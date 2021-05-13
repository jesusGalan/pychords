import sys
from scales import get_notes_of


def debug_scale(scale):
    notes = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']
    result = {}

    for note in notes:
        result[scale + ' tone ' + note + ':'] = get_notes_of(scale, note)

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


if __name__ == '__main__':
    print('\n')
    print(debug_scale(str(sys.argv[1])))
