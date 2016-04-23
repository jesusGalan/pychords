# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context("escala menor armonica"):

            with it("must return Gb minor harmonic"):
                note = 'Gb'
                scale = 'escala_menor_armonica'

                expect(scales(scale, note)).to(equal(
                    ['Gb', 'G#', 'A', 'B', 'C#', 'D', 'F']))

            with it("escala_locria_natural_6"):
                note = 'G#'
                scale = 'escala_locria_natural_6'

                expect(scales(scale, note)).to(equal(
                    ['G#', 'A', 'B', 'C#', 'D', 'F', 'Gb']))

            with it("escala_jonica_#5"):
                note = 'A'
                scale = 'escala_jonica_#5'

                expect(scales(scale, note)).to(equal(
                    ['A', 'B', 'C#', 'D', 'F', 'Gb', 'G#']))

            with it('must return dorian #4'):

                note = "C"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['C', 'D', 'Eb', 'F#', 'G', 'A', 'Bb']))

            with it('must return dorian #4'):
                note = "C#"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D#', 'E', 'G', 'Ab', 'Bb', 'B']))

            with it('must return dorian #4'):
                note = "Db"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D#', 'E', 'G', 'Ab', 'Bb', 'B']))

            with it('must return dorian #4'):
                note = "D"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['D', 'E', 'F', 'G#', 'A', 'B', 'C']))

            with it('must return dorian #4'):
                note = "D#"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['Eb', 'F', 'Gb', 'A', 'Bb', 'C', 'Db']))

            with it('must return dorian #4'):
                note = "Eb"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['Eb', 'F', 'Gb', 'A', 'Bb', 'C', 'Db']))

            with it('must return dorian #4'):
                note = "E"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['E', 'F#', 'G', 'A#', 'B', 'C#', 'D']))

            with it('must return dorian #4'):
                note = "F"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['F', 'G', 'Ab', 'B', 'C', 'D', 'Eb']))

            with it('must return dorian #4'):
                note = "F#"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['F#', 'G#', 'A', 'C', 'Db', 'Eb', 'E']))

            with it('must return dorian #4'):
                note = "Gb"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['F#', 'G#', 'A', 'C', 'Db', 'Eb', 'E']))

            with it('must return dorian #4'):
                note = "G"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['G', 'A', 'Bb', 'C#', 'D', 'E', 'F']))

            with it('must return dorian #4'):
                note = "G#"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['Ab', 'A#', 'B', 'D', 'Eb', 'F', 'Gb']))

            with it('must return dorian #4'):
                note = "Ab"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['Ab', 'A#', 'B', 'D', 'Eb', 'F', 'Gb']))

            with it('must return dorian #4'):
                note = "A"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['A', 'B', 'C', 'D#', 'E', 'F#', 'G']))

            with it('must return dorian #4'):
                note = "A#"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'Db', 'E', 'F', 'G', 'Ab']))

            with it('must return dorian #4'):
                note = "Bb"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'Db', 'E', 'F', 'G', 'Ab']))

            with it('must return dorian #4'):
                note = "B"
                scale = "escala_menor_romana"

                expect(scales(scale, note)).to(equal(
                    ['B', 'C#', 'D', 'F', 'Gb', 'Ab', 'A']))

            with it('escala_frigia_mayor'):
                note = "C#"
                scale = "escala_frigia_mayor"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D', 'F', 'Gb', 'Ab', 'A', 'B']))

            with it('escala_lidia_#2'):
                note = "D"
                scale = "escala_lidia_#2"

                expect(scales(scale, note)).to(equal(
                    ['D', 'F', 'Gb', 'G#', 'A', 'B', 'C#']))

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
