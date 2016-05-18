#  -*- coding: utf-8 -*-

import os
import sys
import wave

import pysynth
import pyaudio

import pychords.functions as pychord_module

octave = 4

# musical timing periods

n = 4
c = 2
sc = 1
b = 8
r = 16


def prepare_for_pysynth(_list):
    _new_list = []
    for elem in _list:
        _new_list.append(tuple([elem.lower() + str(octave), n]))

    _new_list.append(tuple([_list[0].lower() + str(int(octave) + 1), n]))

    return tuple(_new_list)


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
