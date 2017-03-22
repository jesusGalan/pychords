# -*- coding: utf-8 -*-


from expects import *
from pychords.scaleNotes import get_notes_of


with description('Generating get_notes_of'):

        with context("escala mixta o hindu"):

            with it('escala_armonica_mayor'):
                note = "C"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['C', 'D', 'E', 'F', 'G', 'Ab', 'B']))

            with it('escala_armonica_mayor'):
                note = "C#"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Db', 'Eb', 'F', 'Gb', 'Ab', 'A', 'C']))

            with it('escala_armonica_mayor'):
                note = "Db"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Db', 'Eb', 'F', 'Gb', 'Ab', 'A', 'C']))

            with it('escala_armonica_mayor'):
                note = "D"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['D', 'E', 'F#', 'G', 'A', 'Bb', 'C#']))

            with it('escala_armonica_mayor'):
                note = "D#"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Eb', 'F', 'G', 'Ab', 'Bb', 'B', 'D']))

            with it('escala_armonica_mayor'):
                note = "Eb"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Eb', 'F', 'G', 'Ab', 'Bb', 'B', 'D']))

            with it('escala_armonica_mayor'):
                note = "E"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['E', 'F#', 'G#', 'A', 'B', 'C', 'D#']))

            with it('escala_armonica_mayor'):
                note = "F"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['F', 'G', 'A', 'Bb', 'C', 'Db', 'E']))

            with it('escala_armonica_mayor'):
                note = "F#"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Gb', 'Ab', 'A#', 'B', 'C#', 'D', 'F']))

            with it('escala_armonica_mayor'):
                note = "Gb"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Gb', 'Ab', 'A#', 'B', 'C#', 'D', 'F']))

            with it('escala_armonica_mayor'):
                note = "G"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['G', 'A', 'B', 'C', 'D', 'Eb', 'F#']))

            with it('escala_armonica_mayor'):
                note = "G#"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Ab', 'Bb', 'C', 'Db', 'Eb', 'E', 'G']))

            with it('escala_armonica_mayor'):
                note = "Ab"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Ab', 'Bb', 'C', 'Db', 'Eb', 'E', 'G']))

            with it('escala_armonica_mayor'):
                note = "A"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['A', 'B', 'C#', 'D', 'E', 'F', 'G#']))

            with it('escala_armonica_mayor'):
                note = "A#"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'A']))

            with it('escala_armonica_mayor'):
                note = "Bb"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'A']))

            with it('escala_armonica_mayor'):
                note = "B"
                scale = "escala_armonica_mayor"

                expect(get_notes_of(scale, note)).to(equal(['B', 'C#', 'D#', 'E', 'F#', 'G', 'A#']))

            with it('escala_locria_natural_2_6'):
                note = "C#"
                scale = "escala_locria_natural_2_6"

                expect(get_notes_of(scale, note)).to(equal(['C#', 'D#', 'E', 'F#', 'G', 'A#', 'B']))

            with it('escala_frigia_mayor_#9'):
                note = "D#"
                scale = "escala_frigia_mayor_#9"

                expect(get_notes_of(scale, note)).to(equal(['D#', 'E', 'F#', 'G', 'A#', 'B', 'C#']))

            with it('escala_lidia_menor'):
                note = "E"
                scale = "escala_lidia_menor"

                expect(get_notes_of(scale, note)).to(equal(['E', 'F#', 'G', 'A#', 'B', 'C#', 'D#']))

            with it('escala_mixolidia_b2'):
                note = "F#"
                scale = "escala_mixolidia_b2"

                expect(get_notes_of(scale, note)).to(equal(['F#', 'G', 'A#', 'B', 'C#', 'D#', 'E']))

            with it('escala_lidia_#2_#5'):
                note = "G"
                scale = "escala_lidia_#2_#5"

                expect(get_notes_of(scale, note)).to(equal(['G', 'A#', 'B', 'C#', 'D#', 'E', 'F#']))

            with it('escala_locria_bb7'):
                note = "A#"
                scale = "escala_locria_bb7"

                expect(get_notes_of(scale, note)).to(equal(['A#', 'B', 'C#', 'D#', 'E', 'F#', 'G']))
