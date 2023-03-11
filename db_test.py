import unittest
import sqlite3

# get the function to store items to db and also to retrive
from db import populate_ta_feedback, retrive_ta_feedback, cursor_obj, clear_table
class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        clear_table()
        self.c.execute('''CREATE TABLE IF NOT EXISTS ta_feedback
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      feedback TEXT,
                      prompt TEXT, polarity TEXT)
                      ''')

    def test_insert_feedback(self):
        populate_ta_feedback('Great lesson today!', 'What topics did you cover?', "ta_feedback")
        result = retrive_ta_feedback()
        self.assertEqual(result[0][0], 'Great lesson today!')
        self.assertEqual(result[0][1], 'What topics did you cover?')

    def test_retrieve_feedback(self):
        populate_ta_feedback('Great lesson today!', 'What topics did you cover?', "ta_feedback")
        populate_ta_feedback('Not my best class...', 'What could you improve on next time?', "ta_feedback")
        res = retrive_ta_feedback("ta_feedback")
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0][1], 'What topics did you cover?')
        self.assertEqual(res[1][1], 'What could you improve on next time?')

    def tearDown(self):
        clear_table()
        self.conn.close()

if __name__ == '__main__':
    unittest.main()
