from expects import equal, expect
from mamba import describe, description, it, context

from get_chords_by_scale import get_data_by

with description("App pyChords"):
    with context('must return chord list:'):
        with it('must return chord list by a given note and scale'):
            note = 'C'
            scale = 'escala_mayor_natural'
            chord_deep = 1
            expect(get_data_by(note, scale, chord_deep)).to(equal(['C', 'D-', 'E-', 'F', 'G', 'A-', 'B-']))
        with it('must return chord list by a given note and scale'):
            note = 'D'
            scale = 'escala_dorica'
            chord_deep = 1
            expect(get_data_by(note, scale, chord_deep)).to(equal(['D-', 'E-', 'F', 'G', 'A-', 'B-', 'C']))
