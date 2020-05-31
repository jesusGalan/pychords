''' scales specs'''

from mamba import *
from expects import *
from scales import *


with description('making chords'):
    with context('function get chord name must return chords'):
        with it('must return required chords'):
            expect(get_list_of_grades_by('escala_natural')).to(equal(['escala_mayor_natural',
                                                                      'escala_dorica',
                                                                       'escala_frigia',
                                                                       'escala_lidia',
                                                                       'escala_mixolidia',
                                                                       'escala_menor_natural',
                                                                       'escala_locria']))