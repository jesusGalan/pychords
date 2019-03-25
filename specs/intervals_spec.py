'''from mamba import *
from expects import *

from pychords.intervals import get_scale_by_selected_intervals

with description("App pySongs"):
    with context('showing scales for given positions'):

        with it('return the main scale'):

            expect(get_scale_by_selected_intervals(
                ["1", "2", "3", "4", "5", "6", "7"])).to(equal(
                    ['escala_mayor_natural']))

        with it('return differents scales'):

            expect(get_scale_by_selected_intervals(
                ["1", "2", "3", "4", "5", "6"])).to(equal(
                    ['escala_mixolidia', 'escala_mayor_natural']))

        with it('return differents scales'):

            expect(get_scale_by_selected_intervals(
                ["b2", "b3", "4", "5", "6", "b7"])).to(equal(
                    ['escala_java']))'''