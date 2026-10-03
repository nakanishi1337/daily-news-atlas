import unittest

import numpy as np

from scripts.build_map import place_new


def unit(vectors):
    vectors = np.array(vectors, dtype=float)
    return vectors / np.linalg.norm(vectors, axis=1, keepdims=True)


class PlaceNewTest(unittest.TestCase):
    def setUp(self):
        # Two clusters: "food" titles near (0.2, 0.2) and "space" titles near (0.8, 0.8).
        self.points = np.array([[0.2, 0.2], [0.21, 0.2], [0.2, 0.21], [0.8, 0.8], [0.81, 0.8], [0.8, 0.81]])
        self.embeddings = unit([[1, 0.1, 0], [1, 0, 0.1], [1, 0.05, 0.05], [0, 1, 0.1], [0, 1, 0], [0.1, 1, 0]])

    def test_new_article_lands_in_the_cluster_of_similar_articles(self):
        placed = place_new(self.points, self.embeddings, unit([[1, 0.02, 0.02]]), ["food"])
        self.assertLess(np.linalg.norm(placed[0] - [0.2, 0.2]), 0.03)

    def test_split_neighbors_choose_a_cluster_instead_of_the_empty_middle(self):
        # Most similar to one space article, but the food cluster carries more total similarity.
        points = np.vstack([self.points, [[0.5, 0.95]]])
        embeddings = np.vstack([self.embeddings, unit([[0.9, 0.3, 0.3]])])
        placed = place_new(points, embeddings, unit([[0.9, 0.3, 0.3]]), ["mixed"])
        self.assertLess(np.linalg.norm(placed[0] - [0.2, 0.2]), 0.03)

    def test_placement_is_deterministic_and_does_not_stack_points(self):
        new = unit([[1, 0.02, 0.02], [1, 0.02, 0.02]])
        first = place_new(self.points, self.embeddings, new, ["a", "b"])
        np.testing.assert_array_equal(first, place_new(self.points, self.embeddings, new, ["a", "b"]))
        self.assertGreater(np.linalg.norm(first[0] - first[1]), 0)
        self.assertTrue(((first >= 0) & (first <= 1)).all())


if __name__ == "__main__":
    unittest.main()
