Welcome to pyChords!



USAGE EXAMPLES:

>> python pychords/intervals.py b2 3 '#4' 7

	escala_heptatonica_de_blues_quinto_grado
    escala_locria_mayor_sus_4_add_7
    escala_hexatonica_de_blues_cuarto_grado


- You can draw notes on fret with the module visualize as below:

>> python pychords/visualize.py G B D

    0                    3             5             7             9
------------------------------------------------------------------------------------
    ||      |      |  G   |      |      |      |  B   |      |      |  D   |      |
 B  ||      |      |  D   |      |      |      |      |  G   |      |      |      |
 G  ||      |      |      |  B   |      |      |  D   |      |      |      |      |
 D  ||      |      |      |      |  G   |      |      |      |  B   |      |      |
    ||      |  B   |      |      |  D   |      |      |      |      |  G   |      |
    ||      |      |  G   |      |      |      |  B   |      |      |  D   |      |
------------------------------------------------------------------------------------


- So you could use the module called scales for draw scales on fret:

>> python pychords/visualize.py $(python pychords/scales.py escala_mayor_natural C)

 0                    3             5             7             9
------------------------------------------------------------------------------------
 E  ||  F   |      |  G   |      |  A   |      |  B   |  C   |      |  D   |      |  
 B  ||  C   |      |  D   |      |  E   |  F   |      |  G   |      |  A   |      |  
 G  ||      |  A   |      |  B   |  C   |      |  D   |      |  E   |  F   |      |  
 D  ||      |  E   |  F   |      |  G   |      |  A   |      |  B   |  C   |      |  
 A  ||      |  B   |  C   |      |  D   |      |  E   |  F   |      |  G   |      |  
 E  ||  F   |      |  G   |      |  A   |      |  B   |  C   |      |  D   |      |  
------------------------------------------------------------------------------------


In addition you can do composition map based on modal interchange of a tonal center as below:

>> python pychords/composition.py GROUP_OF_SCALES TONE NUMBER_OF_CHORD_TENSES

>> python pychords/composition.py escala_natural C 4

 --------------------------------------------------Vertical-----------------------------------------------------

|    jonicos    |    doricos    |    frigios    |    lidios     |  mixolidios   |    eolicos    |    locrios    |
 =============== =============== =============== =============== =============== =============== ===============
|    Cmaj79     |     D-79      |     E-7b9     |    Fmaj79     |      G79      |     A-79      |    B-7b5b9    |
|    Bbmaj79    |     C-79      |     D-7b9     |    Ebmaj79    |      F79      |     G-79      |    A-7b5b9    |
|    Abmaj79    |     Bb-79     |     C-7b9     |    Dbmaj79    |     Eb79      |     F-79      |    G-7b5b9    |
|    Gmaj79     |     A-79      |     B-7b9     |    Cmaj79     |      D79      |     E-79      |   F#-7b5b9    |
|    Fmaj79     |     G-79      |     A-7b9     |    Bbmaj79    |      C79      |     D-79      |    E-7b5b9    |
|    Ebmaj79    |     F-79      |     G-7b9     |    Abmaj79    |     Bb79      |     C-79      |    D-7b5b9    |
|    Dbmaj79    |     Eb-79     |     F-7b9     |    Gbmaj79    |     Ab79      |     Bb-79     |    C-7b5b9    |

 --------------------------------------------------Horizontal---------------------------------------------------

|    Cmaj79     |     D-79      |     E-7b9     |    Fmaj79     |      G79      |     A-79      |    B-7b5b9    |
|     C-79      |     D-7b9     |    Ebmaj79    |      F79      |     G-79      |    A-7b5b9    |    Bbmaj79    |
|     C-7b9     |    Dbmaj79    |     Eb79      |     F-79      |    G-7b5b9    |    Abmaj79    |     Bb-79     |
|    Cmaj79     |      D79      |     E-79      |   F#-7b5b9    |    Gmaj79     |     A-79      |     B-7b9     |
|      C79      |     D-79      |    E-7b5b9    |    Fmaj79     |     G-79      |     A-7b9     |    Bbmaj79    |
|     C-79      |    D-7b5b9    |    Ebmaj79    |     F-79      |     G-7b9     |    Abmaj79    |     Bb79      |
|    C-7b5b9    |    Dbmaj79    |     Eb-79     |     F-7b9     |    Gbmaj79    |     Ab79      |     Bb-79     |

 --------------------------------------------------------------------------------------------------------------- 


You can search the chord of a specific scale:

>> python pychords/chords.py escala_mayor_natural C 4

    Cmaj79


Pretty easy to install requirements:

    >> python setup.py develop

    (an activated virtualenv is recommended)

tested with expects and mamba:

	- Expects: pip install expects

	- Mamba: pip install mamba

    >> mamba

Translations as soon as possible.