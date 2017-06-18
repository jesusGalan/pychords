Welcome to pyChords!



USAGE EXAMPLES:

>python pychords/functions.py b2 3 '#4' 7

	escala_heptatonica_de_blues_quinto_grado
    escala_locria_mayor_sus_4_add_7
    escala_hexatonica_de_blues_cuarto_grado




- You can draw notes on fret with the module showfret as below:

>python pychords/showfret.py G B D

    0                    3             5             7             9
------------------------------------------------------------------------------------
    ||      |      |  G   |      |      |      |  B   |      |      |  D   |      |
 B  ||      |      |  D   |      |      |      |      |  G   |      |      |      |
 G  ||      |      |      |  B   |      |      |  D   |      |      |      |      |
 D  ||      |      |      |      |  G   |      |      |      |  B   |      |      |
    ||      |  B   |      |      |  D   |      |      |      |      |  G   |      |
    ||      |      |  G   |      |      |      |  B   |      |      |  D   |      |
------------------------------------------------------------------------------------




- So you could use the module called scalenotes for draw scales on fret:

>python pychords/showfret.py $(python pychords/scalenotes.py escala_mayor_natural C)

 0                    3             5             7             9
------------------------------------------------------------------------------------
 E  ||  F   |      |  G   |      |  A   |      |  B   |  C   |      |  D   |      |  
 B  ||  C   |      |  D   |      |  E   |  F   |      |  G   |      |  A   |      |  
 G  ||      |  A   |      |  B   |  C   |      |  D   |      |  E   |  F   |      |  
 D  ||      |  E   |  F   |      |  G   |      |  A   |      |  B   |  C   |      |  
 A  ||      |  B   |  C   |      |  D   |      |  E   |  F   |      |  G   |      |  
 E  ||  F   |      |  G   |      |  A   |      |  B   |  C   |      |  D   |      |  
------------------------------------------------------------------------------------



In addition you can create wav files of the scale via pychords/pysong.py SCALE_NAME NOTE (beta feature)

NOTE: You need to do pip install pyaudio while virtual enviroment(recommended) is running

Here an example:

>python pychords/pysong.py escala_mayor_natural C

	Writing to file test.wav

	[1/8]

	[5/8]

	want to keep this wav file? y/n: y


	The file is already in the current directory. No changes applied.


Copyright (C) 2016  jgalanc


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

Translations as soon as possible.