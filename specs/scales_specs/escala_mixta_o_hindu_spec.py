# -*- coding: utf-8 -*-


from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context("escala mixta o hindu"):

            with it('must return escala mixta'):
                note = "C"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['C', 'D', 'E', 'F', 'G', 'Ab', 'B']))

            with it('must return escala mixta'):
                note = "C#"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Db', 'Eb', 'F', 'Gb', 'Ab', 'A', 'C']))

            with it('must return escala mixta'):
                note = "Db"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Db', 'Eb', 'F', 'Gb', 'Ab', 'A', 'C']))

            with it('must return escala mixta'):
                note = "D"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['D', 'E', 'F#', 'G', 'A', 'Bb', 'C#']))

            with it('must return escala mixta'):
                note = "D#"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Eb', 'F', 'G', 'Ab', 'Bb', 'B', 'D']))

            with it('must return escala mixta'):
                note = "Eb"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Eb', 'F', 'G', 'Ab', 'Bb', 'B', 'D']))

            with it('must return escala mixta'):
                note = "E"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['E', 'F#', 'G#', 'A', 'B', 'C', 'D#']))

            with it('must return escala mixta'):
                note = "F"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['F', 'G', 'A', 'Bb', 'C', 'Db', 'E']))

            with it('must return escala mixta'):
                note = "F#"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Gb', 'Ab', 'A#', 'B', 'C#', 'D', 'F']))

            with it('must return escala mixta'):
                note = "Gb"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Gb', 'Ab', 'A#', 'B', 'C#', 'D', 'F']))

            with it('must return escala mixta'):
                note = "G"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['G', 'A', 'B', 'C', 'D', 'Eb', 'F#']))

            with it('must return escala mixta'):
                note = "G#"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Ab', 'Bb', 'C', 'Db', 'Eb', 'E', 'G']))

            with it('must return escala mixta'):
                note = "Ab"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Ab', 'Bb', 'C', 'Db', 'Eb', 'E', 'G']))

            with it('must return escala mixta'):
                note = "A"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['A', 'B', 'C#', 'D', 'E', 'F', 'G#']))

            with it('must return escala mixta'):
                note = "A#"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'A']))

            with it('must return escala mixta'):
                note = "Bb"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'A']))

            with it('must return escala mixta'):
                note = "B"
                scale = "escala_armonica_mayor"

                expect(scales(scale, note)).to(equal(['B', 'C#', 'D#', 'E', 'F#', 'G', 'A#']))
