''' chords specs'''

from mamba import *
from expects import *

from chords import *

with description('making chords'):
    with context('function get chord name must return chords'):
        with it('must return required chords'):
            expect(get_chord_name('C', 'escala_mayor_natural', 3)).to(equal('Cmaj7'))

        with it('must return required chords'):
            expect(get_chord_name('D', 'escala_dorica', 3)).to(equal('D-7'))

        with it('must return required chords'):
            expect(get_chord_name('C', 'escala_mayor_natural', 3)).to(equal('Cmaj7'))

        with it('must return required chords'):
            expect(get_chord_name('D', 'escala_dorica', 3)).to(equal('D-7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_frigia', 3)).to(equal('Gb-7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_lidia', 3)).to(equal('Gbmaj7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_mixolidia', 3)).to(equal('Gb7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_menor_natural', 3)).to(equal('Gb-7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_locria', 3)).to(equal('Gb-7b5'))

    with context('minor harmonic scale'):
        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_menor_armonica', 3)).to(equal('Gb-maj7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_locria_natural_6', 3)).to(equal('Gb-7b5'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_jonica_#5', 3)).to(equal('Gbmaj7+'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_menor_romana', 3)).to(equal('Gb-7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_frigia_mayor', 3)).to(equal('Gb7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_lidia_#2', 3)).to(equal('Gbmaj7'))

        with it('must return required chords'):
            expect(get_chord_name('Gb', 'escala_disminuida', 3)).to(equal('Gbdim'))

    with context('minor melodic scale'):
        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_menor_melodica', 3)).to(equal('G#-maj7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_java', 3)).to(equal('G#-7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_lidia_#5', 3)).to(equal('G#maj7+'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_lidia_b7', 3)).to(equal('G#7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_mixolidia_b6', 3)).to(equal('G#7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_locria_natural_2', 3)).to(equal('G#-7b5'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_alterada', 3)[0]).to(equal('G#7alt'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_alterada', 3)[1]).to(equal('G#7alt'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_alterada', 4)[0]).to(equal('G#7altb9'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_alterada', 4)[1]).to(equal('G#7alt#9'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_alterada', 5)[0]).to(equal('G#7altb9#11'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_alterada', 5)[1]).to(equal('G#7alt#9#11'))

    with context('major harmonic scale'):
        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_armonica_mayor', 3)).to(equal('G#maj7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_locria_natural_2_6', 3)).to(equal('G#-7b5'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_frigia_mayor_#9', 3)).to(equal('G#7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_lidia_menor', 3)).to(equal('G#-maj7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_mixolidia_b2', 3)).to(equal('G#7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_lidia_#2_#5', 3)).to(equal('G#maj7+'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_locria_bb7', 3)).to(equal('G#dim7'))

    with context('escalas simetricas'):
        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_tono_a_tono', 3)[0]).to(equal('G#7b5'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_semitono_a_tono', 3)[0]).to(equal('G#dim7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_tono_a_semitono', 3)).to(equal('G#dim7'))

        with it('must return required chords'):
            expect(get_chord_name('G#', 'escala_tono_a_semitono', 4)).to(equal('G#dim79'))
