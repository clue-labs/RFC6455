# Run wstest with a full GC between fuzzingclient cases, so finalizers free the
# zlib streams of the finished case before the next one starts.
import gc, sys
from autobahntestsuite import fuzzing

_orig = fuzzing.FuzzingClientFactory.clientConnectionLost

def _clientConnectionLost(self, connector, reason):
    gc.collect()
    return _orig(self, connector, reason)

fuzzing.FuzzingClientFactory.clientConnectionLost = _clientConnectionLost

from autobahntestsuite.wstest import run
sys.argv[0] = 'wstest'
run()
