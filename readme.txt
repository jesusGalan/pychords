Welcome to pyChords!

USAGE EXAMPLE:

>python pychords/functions.py b2 3 '#4' 7

	escala heptatonica de blues quinto grado
	escala englimatic primer grado
	escala alterada
	escala hexatonica de blues cuarto grado

>python pychords/functions.py 2 3 b5 6 '#6'

	escala turca septimo grado
	escala turca tercer grado
	escala lidia b7

You can create wav files of the scale via pychords/pysong.py SCALE_NAME NOTE

NOTE: You need to do pip install pyaudio while virtual enviroment(recommended) is running

Here an example:

>python pychords/pysong.py escala_mayor_natural C

	Writing to file test.wav
	[1/8]
	[5/8]

	want to keep this wav file? y/n: y


	The file is already in the current directory. No changes applied.


Copyright (C) 2016  jgalanc

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

for install the requirements you can do:

    >> python setup.py develop

    (an activated virtualenv is recommended)

tested with expects and mamba:

	- Expects: pip install expects

	- Mamba: pip install mamba

    >> mamba

Stream scales on fly with pyaudio:

    >> pip install pyaudio

Sounds synth provided with pysynth:

    >> pip install PySynth-1.1.tar.gz

    NOTE: This file is the main folder