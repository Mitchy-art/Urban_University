from unittest import TestCase
import unittest
import runner_and_tournament as rt


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = rt.Runner('Усэйн', 10)
        self.run_2 = rt.Runner('Андрей', 9)
        self.run_3 = rt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        dict_fin = {}
        for key, value in cls.all_results.items():
            print(f'Тест: {key}')
            for k, v in value.items():
                print(f'\t{k}: {v.name}')
                # dict_fin[k] = v.name
                # print(value)

    def test_Us_Nik(self):
        tour_1 = rt.Tournament(90, self.run_1, self.run_3)
        results = tour_1.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['test_turn1'] = results
        # TournamentTest.all_results.update(results)
        # self.assertTrue(results[2] == "Ник")

    def test_An_Nik(self):
        tour_2 = rt.Tournament(90, self.run_2, self.run_3)
        results = tour_2.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['test_turn2'] = results
        # TournamentTest.all_results.update(results)
        # self.assertTrue(results[2] == "Ник")

        # result = self.all_results
        # self.assertTrue(result[max(self.all_results.keys())] == "Ник")

    def test_Us_An_Nik(self):
        tour_3 = rt.Tournament(90, self.run_1, self.run_2, self.run_3)
        results = tour_3.start()
        self.assertTrue(results[list(results.keys())[-1]] == 'Ник')
        self.all_results['test_turn3'] = results
        # TournamentTest.all_results.update(results)
        # self.assertTrue(results[3] == "Ник")


if __name__ == '__main__':
    unittest.main()
