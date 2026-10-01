import unittest

from scripts.build_map import specific_topics


class SpecificTopicsTest(unittest.TestCase):
    def test_sleep_and_smoking_are_independent_labels(self):
        self.assertIn("Sleep", specific_topics("Smokers Get Less Sleep, Study Finds"))
        self.assertIn("Smoking", specific_topics("Smokers Get Less Sleep, Study Finds"))

    def test_water_is_not_alcohol_and_wildfire_smoke_is_not_tobacco(self):
        self.assertNotIn("Alcohol", specific_topics("Drinking Water Improves Health"))
        self.assertNotIn("Smoking", specific_topics("Smoke from Wildfires Reaches Europe"))

    def test_word_boundaries_avoid_accidental_matches(self):
        self.assertNotIn("Pets", specific_topics("Catalog of New Products"))
        self.assertNotIn("Books", specific_topics("Booking Flights Is Getting Easier"))
        self.assertNotIn("Pets", specific_topics("Americans Eat More Hot Dogs"))

    def test_specific_labels_can_cross_subjects(self):
        self.assertEqual(set(specific_topics("Remote Workers Drink More Coffee")), {"Remote Work", "Coffee"})


if __name__ == "__main__":
    unittest.main()
