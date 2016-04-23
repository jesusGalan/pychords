from expects import *
from pychords.functions import scales


with description('Generating scales'):

        with context("escala natural"):

            with it("must return major scale"):
                note = "C"
                scale = "escala_mayor_natural"

                expect(scales(scale, note)).to(equal(
                    ['C', 'D', 'E', 'F', 'G', 'A', 'B']))

            with it("must return D dorian scale"):
                note = "D"
                dscale = "escala_dorica"

                expect(scales(dscale, note)).to(equal(
                    ['D', 'E', 'F', 'G', 'A', 'B', 'C']))

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

            with it("must return Gb mixolidian scale"):
                note = "G"
                scale = "escala_mixolidia"

                expect(scales(scale, note)).to(equal(
                    ['G', 'A', 'B', 'C', 'D', 'E', 'F']))

            with it("must return C minor scale"):
                note = "C"
                scale = "escala_menor_natural"

                expect(scales(scale, note)).to(equal(
                    ['C', 'D', 'Eb', 'F', 'G', 'Ab', 'Bb']))

            with it("must return C# minor scale"):
                note = "C#"
                scale = "escala_menor_natural"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D#', 'E', 'F#', 'G#', 'A', 'B']))

            with it("escala_locria"):
                note = "C#"
                scale = "escala_locria"

                expect(scales(scale, note)).to(equal(
                    ['C#', 'D', 'E', 'F#', 'G', 'A', 'B']
                ))

        with context('escala menor melodica'):

            with it("menor_melodica"):
                note = 'Bb'
                scale = 'escala_menor_melodica'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'Db', 'Eb', 'F', 'G', 'A']))

            with it("escala_java"):
                note = 'A#'
                scale = 'escala_java'

                expect(scales(scale, note)).to(equal(
                    ['A#', 'B', 'C#', 'D#', 'F', 'G', 'Ab']))

            with it("escala_lidian_#5"):
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
                scale = 'escala_hindustan'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'Ab']))

            with it("must return A# lidian b7"):
                note = 'A#'
                scale = 'escala_hindustan'

                expect(scales(scale, note)).to(equal(
                    ['Bb', 'C', 'D', 'Eb', 'F', 'Gb', 'Ab']))

            with it("must return Bb eolian b5"):
                note = 'Bb'
                scale = 'escala_locria_natural_2'

                expect(scales(scale, note)).to(equal(
                    ['A#', 'C', 'Db', 'D#', 'E', 'F#', 'G#']))

            with it("must return A# eolian b5"):
                note = 'A#'
                scale = 'escala_locria_natural_2'

                expect(scales(scale, note)).to(equal(
                    ['A#', 'C', 'Db', 'D#', 'E', 'F#', 'G#']))

            with it("escala_alterada"):
                note = 'C'
                scale = 'escala_alterada'

                expect(scales(scale, note)).to(equal(
                    ['C', 'Db', 'Eb', 'E', 'F#', 'G#', 'A#']))

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

        with context("escala mixta o hindú"):

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

        with context("escala hungara mayor"):

            with it("escala_hungara_mayor_primer_grado"):

                note = 'C'
                scale = 'escala_hungara_mayor_primer_grado'

                expect(scales(scale, note)).to(equal(["C", "D#", "E", "F#", "G", "A", "Bb"]))

            with it("escala_hungara_mayor_segundo_grado"):

                note = 'D#'
                scale = 'escala_hungara_mayor_segundo_grado'

                expect(scales(scale, note)).to(equal(["D#", "E", "F#", "G", "A", "Bb", "C"]))

            with it("escala_hungara_mayor_tercer_grado"):

                note = 'E'
                scale = 'escala_hungara_mayor_tercer_grado'

                expect(scales(scale, note)).to(equal(["E", "F#", "G", "A", "Bb", "C", "D#"]))

            with it("escala_hungara_mayor_cuarto_grado"):

                note = 'F#'
                scale = 'escala_hungara_mayor_cuarto_grado'

                expect(scales(scale, note)).to(equal(["F#", "G", "A", "Bb", "C", "D#", "E"]))

            with it("escala_hungara_mayor_quinto_grado"):

                note = 'G'
                scale = 'escala_hungara_mayor_quinto_grado'

                expect(scales(scale, note)).to(equal(["G", "A", "Bb", "C", "D#", "E", "F#"]))

            with it("escala_hungara_mayor_sexto_grado"):

                note = 'A'
                scale = 'escala_hungara_mayor_sexto_grado'

                expect(scales(scale, note)).to(equal(["A", "Bb", "C", "D#", "E", "F#", "G"]))

        with context('escala hexatónica de blues'):

            with it('escala_hexatonica_de_blues_primer_grado'):
                note = "B"
                scale = "escala_hexatonica_de_blues_primer_grado"

                expect(scales(scale, note)).to(equal(['B', 'D', 'E', 'F', 'Gb', 'A']))

            with it('escala_hexatonica_de_blues_segundo_grado'):
                note = "D"
                scale = "escala_hexatonica_de_blues_segundo_grado"

                expect(scales(scale, note)).to(equal(['D', 'E', 'F', 'Gb', 'A', 'B']))

            with it('escala_hexatonica_de_blues_tercer_grado'):
                note = "E"
                scale = "escala_hexatonica_de_blues_tercer_grado"

                expect(scales(scale, note)).to(equal(['E', 'F', 'Gb', 'A', 'B', 'D']))

            with it('escala_hexatonica_de_blues_cuarto_grado'):
                note = "F"
                scale = "escala_hexatonica_de_blues_cuarto_grado"

                expect(scales(scale, note)).to(equal(['F', 'Gb', 'A', 'B', 'D', 'E']))

            with it('escala_hexatonica_de_blues_quinto_grado'):
                note = "Gb"
                scale = "escala_hexatonica_de_blues_quinto_grado"

                expect(scales(scale, note)).to(equal(['Gb', 'A', 'B', 'D', 'E', 'F']))

            with it('escala_hexatonica_de_blues_sexto_grado'):
                note = "A"
                scale = "escala_hexatonica_de_blues_sexto_grado"

                expect(scales(scale, note)).to(equal(['A', 'B', 'D', 'E', 'F', 'Gb']))


            with it('escala_hexatonica_de_blues_primer_grado'):
                note = "C"
                scale = "escala_hexatonica_de_blues_primer_grado"

                expect(scales(scale, note)).to(equal(['C', 'D#', 'F', 'F#', 'G', 'A#']))

        with context('escalas simétricas'):

            with it('must return escala tono a tono'):
                note = "B"
                scale = "escala_tono_a_tono"

                expect(scales(scale, note)).to(equal(['B', 'C#', 'D#', 'F', 'G', 'A']))

            with it("must return E semitone a tone scale"):
                note = "E"
                scale = "escala_semitono_a_tono"

                expect(scales(scale, note)).to(equal(
                    ['E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D']))

            with it("must return E semitone a tone scale"):
                note = "E"
                scale = "escala_semitono_a_tono"

                expect(scales(scale, note)).to(equal(
                    ['E', 'F', 'G', 'Ab', 'Bb', 'B', 'C#', 'D']))

            with it("must return C cromatic scale"):
                note = "C"
                scale = "escala_cromatica"

                expect(scales(scale, note)).to(equal(
                    ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']))
