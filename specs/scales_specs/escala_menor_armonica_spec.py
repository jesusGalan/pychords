# -*- coding: utf-8 -*-


from expects import *
from pychords.scales import get_notes_of


with description('Generating get_notes_of'):

        with context("escala menor armonica"):

            with it("escala_menor_armonica"):
                note = 'Gb'
                scale = 'escala_menor_armonica'

                expect(get_notes_of(scale, note)).to(equal(
                    ['Gb', 'G#', 'A', 'B', 'C#', 'D', 'F']))

            with it("escala_locria_natural_6"):
                note = 'G#'
                scale = 'escala_locria_natural_6'

                expect(get_notes_of(scale, note)).to(equal(
                    ['G#', 'A', 'B', 'C#', 'D', 'F', 'Gb']))

            with it("escala_jonica_#5"):
                note = 'A'
                scale = 'escala_jonica_#5'

                expect(get_notes_of(scale, note)).to(equal(
                    ['A', 'B', 'C#', 'D', 'F', 'Gb', 'G#']))

            with it('escala_menor_romana'):

                note = "C"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C', 'D', 'Eb', 'F#', 'G', 'A', 'Bb']))

            with it('escala_menor_romana'):
                note = "C#"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C#', 'D#', 'E', 'G', 'Ab', 'Bb', 'B']))

            with it('escala_menor_romana'):
                note = "Db"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C#', 'D#', 'E', 'G', 'Ab', 'Bb', 'B']))

            with it('escala_menor_romana'):
                note = "D"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['D', 'E', 'F', 'G#', 'A', 'B', 'C']))

            with it('escala_menor_romana'):
                note = "D#"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['Eb', 'F', 'Gb', 'A', 'Bb', 'C', 'Db']))

            with it('escala_menor_romana'):
                note = "Eb"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['Eb', 'F', 'Gb', 'A', 'Bb', 'C', 'Db']))

            with it('escala_menor_romana'):
                note = "E"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['E', 'F#', 'G', 'A#', 'B', 'C#', 'D']))

            with it('escala_menor_romana'):
                note = "F"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['F', 'G', 'Ab', 'B', 'C', 'D', 'Eb']))

            with it('escala_menor_romana'):
                note = "F#"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['F#', 'G#', 'A', 'C', 'Db', 'Eb', 'E']))

            with it('escala_menor_romana'):
                note = "Gb"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['F#', 'G#', 'A', 'C', 'Db', 'Eb', 'E']))

            with it('escala_menor_romana'):
                note = "G"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['G', 'A', 'Bb', 'C#', 'D', 'E', 'F']))

            with it('escala_menor_romana'):
                note = "G#"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['Ab', 'A#', 'B', 'D', 'Eb', 'F', 'Gb']))

            with it('escala_menor_romana'):
                note = "Ab"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['Ab', 'A#', 'B', 'D', 'Eb', 'F', 'Gb']))

            with it('escala_menor_romana'):
                note = "A"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['A', 'B', 'C', 'D#', 'E', 'F#', 'G']))

            with it('escala_menor_romana'):
                note = "A#"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'Db', 'E', 'F', 'G', 'Ab']))

            with it('escala_menor_romana'):
                note = "Bb"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['Bb', 'C', 'Db', 'E', 'F', 'G', 'Ab']))

            with it('escala_menor_romana'):
                note = "B"
                scale = "escala_menor_romana"

                expect(get_notes_of(scale, note)).to(equal(
                    ['B', 'C#', 'D', 'F', 'Gb', 'Ab', 'A']))

            with it('escala_frigia_mayor'):
                note = "C#"
                scale = "escala_frigia_mayor"

                expect(get_notes_of(scale, note)).to(equal(
                    ['C#', 'D', 'F', 'Gb', 'Ab', 'A', 'B']))

            with it('escala_lidia_#2'):
                note = "D"
                scale = "escala_lidia_#2"

                expect(get_notes_of(scale, note)).to(equal(
                    ['D', 'F', 'Gb', 'G#', 'A', 'B', 'C#']))

            with it("escala_superlocria_bb7"):
                note = 'Gb'
                scale = 'escala_disminuida'

                expect(get_notes_of(scale, note)).to(equal(
                    ['F#', 'G', 'A', 'Bb', 'C', 'D', 'Eb']))

            with it("escala_superlocrian_bb7"):
                note = 'C'
                scale = 'escala_disminuida'

                expect(get_notes_of(scale, note)).to(equal(
                    ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A']))

            with it("escala_superlocrian_bb7"):
                note = 'C'
                scale = 'escala_disminuida'

                expect(get_notes_of(scale, note)).to(equal(
                    ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A']))
