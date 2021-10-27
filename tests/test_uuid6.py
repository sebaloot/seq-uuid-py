from unittest import TestCase

import seq_uuid


class TestUUID6(TestCase):

    def test_sequence(self):
        items = [seq_uuid.uuid6() for i in range(0, 10)]

        for i in range(1, len(items)):
            self.assertTrue(items[i - 1] < items[i])

    def test_version(self):
        value = seq_uuid.uuid6()
        self.assertEqual(value.version, 6)
