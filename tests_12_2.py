from unittest import TestCase
import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.run_1 = Runner('Усэйн', 10)
        self.run_2 = Runner('Андрей', 9)
        self.run_3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        dict_fin = {}
        for key, value in cls.all_results.items():
            for k, v in value.items():
                dict_fin[k] = str(v)
                print(value)

    def test_Us_Nik(self):
        tour_1 = Tournament(90, self.run_1, self.run_3)
        results = tour_1.start()
        TournamentTest.all_results.update(results)
        self.assertTrue(results[2] == "Ник")

    def test_An_Nik(self):
        tour_2 = Tournament(90, self.run_2, self.run_3)
        results = tour_2.start()
        TournamentTest.all_results.update(results)
        self.assertTrue(results[2] == "Ник")

        # result = self.all_results
        # self.assertTrue(result[max(self.all_results.keys())] == "Ник")

    def test_Us_An_Nik(self):
        tour_3 = Tournament(90, self.run_1, self.run_2, self.run_3)
        results = tour_3.start()
        TournamentTest.all_results.update(results)
        self.assertTrue(results[3] == "Ник")


if __name__ == '__main__':
    unittest.main()
