from osext.test import pushdtest
import unittest

suite = unittest.TestLoader().loadTestsFromModule(pushdtest)
unittest.TextTestRunner(verbosity=2).run(suite)
