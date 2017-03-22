from mamba import *
from expects import *
from pyChords import *

with description("App pyChords"):

    with context('function for take the int of required notes must do it'):

        with it('must return required scale note'):

            scale = ['C', 'C#.Db', 'D#.Eb', 'F#.Gb', 'G']

            expect(get_required_notes(scale)).to(equal(3))

        with it('must return required scale note'):

            scale = ['C', 'C#.Db', 'D']

            expect(get_required_notes(scale)).to(equal(1))

    with context('function for take required notes must do it'):

        with it('must return required scale notes'):

            scale = ['A#.Bb', 'B', 'C', 'C#.Db', 'D#.Eb', 'E', 'F', 'F#.Gb', 'G', 'G#.Ab', 'A']
            sure = 'C'
            next_sure = 'E'

            expect(get_short_list_of_notes(sure, next_sure, scale)).to(equal(['C', 'C#.Db', 'D#.Eb', 'E']))

        with it('must return required scale notes'):

            scale = ['A#.Bb', 'C', 'D', 'E', 'F#.Gb', 'G', 'A', 'A#.Bb', 'C', 'D', 'E', 'F#.Gb', 'G', 'A']
            sure = 'E'
            next_sure = 'G'

            expect(get_short_list_of_notes(sure, next_sure, scale)).to(equal(['E', 'F#.Gb', 'G']))

    with context('function for take all notes must do it'):

        with it('must return a list from Bb'):

            note = 'Bb'

            expect(take_all_notes_from(note)).to(equal(
                ['A#.Bb', 'B', 'C', 'C#.Db', 'D', 'D#.Eb', 'E', 'F', 'F#.Gb', 'G', 'G#.Ab', 'A']))

        with it('must return a list from B'):

            note = 'B'

            expect(take_all_notes_from(note)).to(equal(
                ['B', 'C', 'C#.Db', 'D', 'D#.Eb', 'E', 'F', 'F#.Gb', 'G', 'G#.Ab', 'A', 'A#.Bb']))

    with context("must return scales. "):

        with it("must return major scale"):
            note = "C"
            scale = "escala_mayor_natural"

            expect(scales(scale, note)).to(equal(
                ['C', 'D', 'E', 'F', 'G', 'A', 'B']))

        with it("must return C minor scale"):
            note = "C"
            scale = "escala_menor_natural"

            expect(scales(scale, note)).to(equal(
                ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']))

        with it("must return D dorian scale"):
            note = "D"
            dscale = "escala_dorica"

            expect(scales(dscale, note)).to(equal(
                ['D', 'E', 'F', 'G', 'A', 'B', 'C']))

        with it("must return C# minor scale"):
            note = "C#"
            scale = "escala_menor_natural"

            expect(scales(scale, note)).to(equal(
                ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']))

        with it("must return C# frigian scale"):
            note = "C#"
            scale = "escala_frigia"

            expect(scales(scale, note)).to(equal(
                ['C#', 'D', 'E', 'F#', 'G#', 'A', 'B']))

        with it("must return Gb lidian scale"):
            note = "Gb"
            scale = "escala_lidia"

            expect(scales(scale, note)).to(equal(
                ['Gb', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F']))

        with it("must return Bb minor melodic"):
            note = 'Bb'
            scale = 'escala_menor_melodica'

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'Db', 'Eb', 'F', 'G', 'A']))

        with it("must return A# dorian b9"):
            note = 'A#'
            scale = 'escala_dorica_b9'

            expect(scales(scale, note)).to(equal(
                ['A#', 'B', 'C#', 'D#', 'F', 'G', 'Ab']))

        with it("must return Bb lidian #5"):
            note = 'Bb'
            scale = 'escala_lidia_#5'

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'D', 'E', 'F#', 'G', 'A']))

        with it("must return Bb lidian #5"):
            note = 'A#'
            scale = 'escala_lidia_#5'

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'D', 'E', 'F#', 'G', 'A']))

        with it("must return Bb lidian b7"):
            note = 'Bb'
            scale = 'escala_lidia_b7'

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'D', 'E', 'F', 'G', 'Ab']))

        with it("must return A# lidian b7"):
            note = 'A#'
            scale = 'escala_lidia_b7'

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'D', 'E', 'F', 'G', 'Ab']))

        with it("must return Bb lidian b7"):
            note = 'Bb'
            scale = 'escala_mixolidia_b6'

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'Ab']))

        with it("must return A# lidian b7"):
            note = 'A#'
            scale = 'escala_mixolidia_b6'

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'Ab']))

        with it("must return Bb eolian b5"):
            note = 'Bb'
            scale = 'escala_eolica_b5'

            expect(scales(scale, note)).to(equal(
                ['A#', 'C', 'Db', 'D#', 'E', 'F#', 'G#']))

        with it("must return A# eolian b5"):
            note = 'A#'
            scale = 'escala_eolica_b5'

            expect(scales(scale, note)).to(equal(
                ['A#', 'C', 'Db', 'D#', 'E', 'F#', 'G#']))

        with it("must return Gb minor harmonic"):
            note = 'Gb'
            scale = 'escala_menor_armonica'

            expect(scales(scale, note)).to(equal(
                ['Gb', 'G#', 'A', 'B', 'C#', 'D', 'F']))

        with it("must return Gb superlocrian bb7"):
            note = 'Gb'
            scale = 'escala_superlocria_bb7'

            expect(scales(scale, note)).to(equal(
                ['F#', 'G', 'A', 'Bb', 'C', 'D', 'Eb']))

        with it("must return C superlocrian bb7"):
            note = 'C'
            scale = 'escala_superlocria_bb7'

            expect(scales(scale, note)).to(equal(
                ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A']))

        with it("must return C superlocrian bb7"):
            note = 'C'
            scale = 'escala_superlocria_bb7'

            expect(scales(scale, note)).to(equal(
                ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A']))

        with it('must return dorian #4'):

            note = "C"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['C', 'D', 'Eb', 'F#', 'G', 'A', 'Bb']))

        with it('must return dorian #4'):
            note = "C#"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['C#', 'D#', 'E', 'G', 'Ab', 'Bb', 'B']))

        with it('must return dorian #4'):
            note = "Db"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['C#', 'D#', 'E', 'G', 'Ab', 'Bb', 'B']))

        with it('must return dorian #4'):
            note = "D"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['D', 'E', 'F', 'G#', 'A', 'B', 'C']))

        with it('must return dorian #4'):
            note = "D#"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['Eb', 'F', 'Gb', 'A', 'Bb', 'C', 'Db']))

        with it('must return dorian #4'):
            note = "Eb"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['Eb', 'F', 'Gb', 'A', 'Bb', 'C', 'Db']))

        with it('must return dorian #4'):
            note = "E"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['E', 'F#', 'G', 'A#', 'B', 'C#', 'D']))

        with it('must return dorian #4'):
            note = "F"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['F', 'G', 'Ab', 'B', 'C', 'D', 'Eb']))

        with it('must return dorian #4'):
            note = "F#"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['F#', 'G#', 'A', 'C', 'Db', 'Eb', 'E']))

        with it('must return dorian #4'):
            note = "Gb"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['F#', 'G#', 'A', 'C', 'Db', 'Eb', 'E']))

        with it('must return dorian #4'):
            note = "G"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['G', 'A', 'Bb', 'C#', 'D', 'E', 'F']))

        with it('must return dorian #4'):
            note = "G#"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['Ab', 'A#', 'B', 'D', 'Eb', 'F', 'Gb']))

        with it('must return dorian #4'):
            note = "Ab"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['Ab', 'A#', 'B', 'D', 'Eb', 'F', 'Gb']))

        with it('must return dorian #4'):
            note = "A"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['A', 'B', 'C', 'D#', 'E', 'F#', 'G']))

        with it('must return dorian #4'):
            note = "A#"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'Db', 'E', 'F', 'G', 'Ab']))

        with it('must return dorian #4'):
            note = "Bb"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['Bb', 'C', 'Db', 'E', 'F', 'G', 'Ab']))

        with it('must return dorian #4'):
            note = "B"
            scale = "escala_dorica_#4"

            expect(scales(scale, note)).to(equal(
                ['B', 'C#', 'D', 'F', 'Gb', 'Ab', 'A']))

        with it('must return escala mixta'):
            note = "C"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['C', 'D', 'E', 'F', 'G', 'Ab', 'B']))

        with it('must return escala mixta'):
            note = "C#"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Db', 'Eb', 'F', 'Gb', 'Ab', 'A', 'C']))

        with it('must return escala mixta'):
            note = "Db"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Db', 'Eb', 'F', 'Gb', 'Ab', 'A', 'C']))

        with it('must return escala mixta'):
            note = "D"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['D', 'E', 'F#', 'G', 'A', 'Bb', 'C#']))

        with it('must return escala mixta'):
            note = "D#"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Eb', 'F', 'G', 'Ab', 'Bb', 'B', 'D']))

        with it('must return escala mixta'):
            note = "Eb"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Eb', 'F', 'G', 'Ab', 'Bb', 'B', 'D']))

        with it('must return escala mixta'):
            note = "E"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['E', 'F#', 'G#', 'A', 'B', 'C', 'D#']))

        with it('must return escala mixta'):
            note = "F"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['F', 'G', 'A', 'Bb', 'C', 'Db', 'E']))

        with it('must return escala mixta'):
            note = "F#"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Gb', 'Ab', 'A#', 'B', 'C#', 'D', 'F']))

        with it('must return escala mixta'):
            note = "Gb"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Gb', 'Ab', 'A#', 'B', 'C#', 'D', 'F']))

        with it('must return escala mixta'):
            note = "G"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['G', 'A', 'B', 'C', 'D', 'Eb', 'F#']))

        with it('must return escala mixta'):
            note = "G#"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Ab', 'Bb', 'C', 'Db', 'Eb', 'E', 'G']))

        with it('must return escala mixta'):
            note = "Ab"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Ab', 'Bb', 'C', 'Db', 'Eb', 'E', 'G']))

        with it('must return escala mixta'):
            note = "A"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['A', 'B', 'C#', 'D', 'E', 'F', 'G#']))

        with it('must return escala mixta'):
            note = "A#"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'A']))

        with it('must return escala mixta'):
            note = "Bb"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'A']))

        with it('must return escala mixta'):
            note = "B"
            scale = "escala_mixta"

            expect(scales(scale, note)).to(equal(['B', 'C#', 'D#', 'E', 'F#', 'G', 'A#']))








        with it("must return C cromatic scale"):
            note = "C"
            scale = "escala_cromatica"

            expect(scales(scale, note)).to(equal(
                ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']))

    with context('must return good notes'):

        with it("must return good notes with a short list"):

            short_list = ['C', 'C#.Db', 'D#.Eb', 'F#.Gb', 'G']

            expect(return_good_notes(short_list)).to(equal(['C', 'Db', 'Eb', 'F#', 'G']))

        with it("must return good notes with a short list"):

            short_list = ['C', 'D#.Eb', 'F#.Gb', 'A']

            expect(return_good_notes(short_list)).to(equal(['C', 'D#', 'F#', 'A']))

        with it("must return good notes with a short list"):

            short_list = ['C', 'C#.Db', 'D#.Eb', 'F#.Gb', 'A']

            expect(return_good_notes(short_list)).to(equal(['C', 'Db', 'Eb', 'Gb', 'A']))

        with it("must return good notes with a short list"):

            short_list = ['C', 'D#.Eb', 'F#.Gb', 'G#.Ab', 'A']

            expect(return_good_notes(short_list)).to(equal(['C', 'D#', 'F#', 'G#', 'A']))

        with it("must return good notes with a short list"):

            short_list = ['F', 'F#.Gb', 'G#.Ab', 'A']

            expect(return_good_notes(short_list)).to(equal(['F', 'Gb', 'G#', 'A']))