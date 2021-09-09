from abc import abstractmethod


class RisAuthorShared:

    def __init__(self, author_cff):
        self._author_cff = author_cff
        self._behaviors = {
            'GFAN': self._from_given_and_last,
            'GFA_': self._from_given_and_last,
            'GF_N': self._from_given_and_last,
            'GF__': self._from_given_and_last,
            'G_AN': self._from_name,
            'G_A_': self._from_alias,
            'G__N': self._from_name,
            'G__': self._from_given,
            '_FAN': self._from_last,
            '_FA_': self._from_last,
            '_F_N': self._from_last,
            '_F__': self._from_last,
            '__AN': self._from_name,
            '__A_': self._from_alias,
            '___N': self._from_name,
            '____': RisAuthorShared._from_thin_air
        }

    def _exists_nonempty(self, key):
        value = self._author_cff.get(key, None)
        return value is not None and value != ''

    def _from_alias(self):
        return 'AU  - ' + self._author_cff.get('alias') + '\n'

    def _from_given_and_last(self):
        return 'AU  - ' + self._get_full_last_name() + ', ' + self._author_cff.get('given-names') + '\n'

    def _from_given(self):
        return 'AU  - ' + self._author_cff.get('given-names') + '\n'

    def _from_last(self):
        return 'AU  - ' + self._get_full_last_name() + '\n'

    def _from_name(self):
        return 'AU  - ' + self._author_cff.get('name') + '\n'

    @staticmethod
    def _from_thin_air():
        return None

    def _get_full_last_name(self):
        nameparts = [
            self._author_cff.get('name-particle'),
            self._author_cff.get('family-names'),
            self._author_cff.get('name-suffix')
        ]
        return ' '.join([n for n in nameparts if n is not None])

    @abstractmethod
    def as_string(self):
        pass

