import os
import logging

LOGLEVEL = os.environ.get('TTACC_LOGLEVEL', 'WARNING').upper()

logging.basicConfig(level=LOGLEVEL)

class TTACCLogger():

    def set(self, name):
        self._log = logging.getLogger(name)

    def __getattr__(self, name):
        def _forward_to_log(*args, **kwargs):
            return getattr(self._log, name)(*args, **kwargs)
        return _forward_to_log

log = TTACCLogger()
