from unittest import TestCase


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(TestCase):
    def test_walk(self):
        run_1 = Runner('test_1')
        for i in range(10):
            Runner.walk(run_1)
        self.assertEqual(run_1.distance, 50)

    def test_run(self):
        run_2 = Runner('test_2')
        for i in range(10):
            Runner.run(run_2)
        self.assertEqual(run_2.distance, 100)

    def test_challenge(self):
        run_3 = Runner('test_3')
        run_4 = Runner('test_4')
        for i in range(10):
            Runner.walk(run_3)
            for j in range(10):
                Runner.run(run_4)
        self.assertNotEqual(run_3.distance, run_4.distance)
