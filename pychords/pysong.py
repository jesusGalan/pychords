#  -*- coding: utf-8 -*-

import os
import sys
import wave

import pysynth
import pyaudio

import functions as pychord_module

octave = 4

# musical timing periods

n = 4
c = 2
sc = 1
b = 8
r = 16


def prepare_for_pysynth(_list):
    _new_list = []
    if _list[0] == 'C':
        for elem in _list:
            _new_list.append(tuple([elem.lower() + str(octave), n]))

        _new_list.append(tuple([_list[0].lower() + str(int(octave) + 1), n]))
    else:
        pos_c = search_c_position(_list)
        for elem in range(len(_list)):
            if elem < pos_c:
                _new_list.append(tuple([str(_list[elem]).lower() + str(octave), n]))
            elif elem >= pos_c:
                _new_list.append(tuple([str(_list[elem]).lower() + str(int(octave) + 1), n]))

        _new_list.append(tuple([_list[0].lower() + str(int(octave) + 1), n]))

    return tuple(_new_list)


def search_c_position(_list):
    count = 0
    res = 0

    if 'C' in _list:
        for elem in _list:
            if elem == 'C':
                res = count
                count = count + 1

            else:
                count = count + 1

    else:
        for elem in _list:
            try:
                if 'C' in pychord_module.get_the_notes_between(elem, _list[_list.index(elem) + 1]):
                    count = count + 1
                    res = count
                elif 'C' not in pychord_module.get_the_notes_between(elem, _list[_list.index(elem) + 1]):
                    count = count + 1

            except IndexError:
                count = count + 1
                print 'final de lista'

    return res

if __name__ == '__main__':

    scale_grade = sys.argv[1]
    note = sys.argv[2]
    escala = pychord_module.scales(scale_grade, note)
    octave = 4

    test = prepare_for_pysynth(escala)

    pysynth.make_wav(test, fn="test.wav")

    # define stream chunk
    chunk = 1024

    # open a wav format music
    _root = ''
    _name = ''
    path = ''
    for root, dirs, files in os.walk('.'):
        for name in files:
            if 'test.wav' in name:
                _root = root
                _name = name
                path = os.path.realpath(os.path.join(root, name))

    f = wave.open(path, "rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    # read data
    data = f.readframes(chunk)

    # paly stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)

    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()
    f.close()
    x = raw_input('want to keep this wav file? y/n: ')

    if x == 'y':
        try:
            os.rename(os.path.realpath(os.path.join(_root, _name)), os.path.realpath(os.path.join(_root, scale_grade + '_in_' + note + '.wav')))

        except WindowsError:
            print '\n'
            print 'The file is already in the current directory. No changes applied.'
            print '\n'

    elif x == 'n':
        os.remove(os.path.realpath(os.path.join(_root, _name)))

    else:
        print 'mmmakey'
        os.remove(os.path.realpath(os.path.join(_root, _name)))
