import unittest

from scripts.build_map import ALL_TOPICS, CATEGORIES, EXCLUSIONS, SPECIFIC_TOPICS, TOPICS, specific_topics


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

    def test_new_subtopics_match_typical_titles(self):
        self.assertIn("Japanese Food", specific_topics("Japan's First Ramen Shop Reopens in Asakusa"))
        self.assertIn("Trains", specific_topics("Shinkansen to Have Private Booths by October"))
        self.assertIn("Anime & Manga", specific_topics("The Role of Anime in Manga's Worldwide Success"))
        self.assertIn("Baseball", specific_topics("Ohtani Hits Homer in First Exhibition Game for Dodgers"))
        self.assertIn("Weather & Disasters", specific_topics("European Countries Hit By Early Heat Wave"))

    def test_exclusions_avoid_known_false_matches(self):
        self.assertNotIn("Trains", specific_topics("Train Your Brain to Think in English"))
        self.assertNotIn("Mental Health", specific_topics("Lonely Planet Announces Top Places to Visit"))
        self.assertNotIn("Moon & Planets", specific_topics("Lonely Planet's Best in Travel 2025"))
        self.assertNotIn("Dinosaurs & Fossils", specific_topics("US Court Says Fossil Fuels Violate Rights"))
        self.assertNotIn("Royals", specific_topics("Burger King Uses Moldy Burgers in New Ads"))
        self.assertNotIn("Housing", specific_topics("Japan's Ishiba Loses Upper House Majority"))
        self.assertNotIn("Weather & Disasters", specific_topics("World's Hottest Pepper Sends Man to Hospital"))
        self.assertNotIn("Marathons", specific_topics("Running Out of Time to Save the Reef"))


class CategoryTest(unittest.TestCase):
    def test_every_topic_has_a_known_category_and_every_category_has_topics(self):
        for name, (_, category) in ALL_TOPICS.items():
            self.assertIn(category, CATEGORIES, name)
        self.assertEqual(set(CATEGORIES), {category for _, category in ALL_TOPICS.values()})

    def test_topic_names_are_unique_and_distinct_from_categories(self):
        self.assertFalse(set(TOPICS) & set(SPECIFIC_TOPICS))
        self.assertFalse(set(ALL_TOPICS) & set(CATEGORIES))
        self.assertLessEqual(set(EXCLUSIONS), set(SPECIFIC_TOPICS))


if __name__ == "__main__":
    unittest.main()
