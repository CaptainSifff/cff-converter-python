import os
import pytest
from test.contracts.bibtex_object import Contract
from cffconvert.behavior_1_1_x.bibtex_object import BibtexObject
from cffconvert import Citation


@pytest.fixture(scope="module")
def bibtex_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return BibtexObject(citation.cffobj, initialize_empty=True)


class TestBibtexObject(Contract):

    def test_as_string(self, bibtex_object):
        actual_bibtex = bibtex_object.add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "bibtex.bib")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_bibtex = f.read()
        assert actual_bibtex == expected_bibtex

    def test_author(self, bibtex_object):
        assert bibtex_object.add_author().author == 'author = {Van Zandt, Steven and van Zandt, Steven}'

    def test_check_cffobj(self, bibtex_object):
        bibtex_object.check_cffobj()
        # doesn't need an assert

    def test_doi(self, bibtex_object):
        assert bibtex_object.add_doi().doi is None

    def test_month(self, bibtex_object):
        assert bibtex_object.add_month().month == 'month = {1}'

    def test_title(self, bibtex_object):
        assert bibtex_object.add_title().title == 'title = {cff-converter-python}'

    def test_url(self, bibtex_object):
        assert bibtex_object.add_url().url is None

    def test_year(self, bibtex_object):
        assert bibtex_object.add_year().year == 'year = {2018}'
