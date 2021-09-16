from cffconvert.behavior_1_0_x.ris_author import RisAuthor
from cffconvert.behavior_1_0_x.ris_url import RisUrl
from cffconvert.behavior_shared.ris_object_shared import RisObjectShared as Shared


class RisObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty)

    def add_author(self):
        authors_cff = self.cffobj.get('authors', list())
        authors_bibtex = [RisAuthor(a).as_string() for a in authors_cff]
        authors_bibtex_filtered = [a for a in authors_bibtex if a is not None]
        self.author = ''.join(authors_bibtex_filtered)
        return self

    def add_date(self):
        if 'date-released' in self.cffobj.keys():
            self.date = "DA  - {:d}-{:02d}-{:02d}\n".format(self.cffobj['date-released'].year,
                                                            self.cffobj['date-released'].month,
                                                            self.cffobj['date-released'].day)
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = 'DO  - {}\n'.format(self.cffobj['doi'])
        return self

    def add_url(self):
        self.url = RisUrl(self.cffobj).as_string()
        return self

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = 'PY  - {}\n'.format(self.cffobj['date-released'].year)
        return self
