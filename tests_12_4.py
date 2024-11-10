import traceback
from unittest import TestCase
import rt_excep
import unittest
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename='runner_tests.log',
                    encoding='UTF-8', format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest(TestCase):
    is_frozen = False

    @unittest.skipIf(False, '')
    def test_walk(self):
        try:
            run_1 = rt_excep.Runner('test_1', speed=-5)
            logging.info('"test_walk" выполнен успешно')
            for i in range(10):
                rt_excep.Runner.walk(run_1)
            self.assertEqual(run_1.distance, 50)
        except ValueError as err:
            logging.warning("Неверная скорость для Runner")
            logging.error(traceback.format_exc())

    @unittest.skipIf(False, '')
    def test_run(self):
        try:
            run_2 = rt_excep.Runner(20, 3.4)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                rt_excep.Runner.run(run_2)
            self.assertEqual(run_2.distance, 100)
        except TypeError as err:
            logging.warning('Неверный тип данных для объекта Runner')
            logging.error(traceback.format_exc())
