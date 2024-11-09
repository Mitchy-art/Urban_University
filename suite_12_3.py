import unittest
import tests_12_1
import tests_12_2

Test_suite = unittest.TestSuite()
Test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
Test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

text_t_r = unittest.TextTestRunner(verbosity=2)
text_t_r.run(Test_suite)