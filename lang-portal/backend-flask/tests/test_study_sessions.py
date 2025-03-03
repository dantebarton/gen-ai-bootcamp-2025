import unittest
import json
from app import create_app

class TestStudySessions(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_create_study_session_success(self):
        response = self.app.post('/api/study-sessions', 
                                 data=json.dumps({
                                     "group_id": 1,
                                     "activity_id": 2,
                                     "end_time": "2023-10-10T10:00:00",
                                     "review_items": [
                                         {"item_id": 1, "status": "correct"},
                                         {"item_id": 2, "status": "wrong"}
                                     ]
                                 }),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('session_id', response.json)

    def test_create_study_session_missing_group_id(self):
        response = self.app.post('/api/study-sessions', 
                                 data=json.dumps({
                                     "activity_id": 2,
                                     "end_time": "2023-10-10T10:00:00",
                                     "review_items": [
                                         {"item_id": 1, "status": "correct"},
                                         {"item_id": 2, "status": "wrong"}
                                     ]
                                 }),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

    def test_create_study_session_invalid_data(self):
        response = self.app.post('/api/study-sessions', 
                                 data=json.dumps({
                                     "group_id": "invalid",
                                     "activity_id": 2,
                                     "end_time": "2023-10-10T10:00:00",
                                     "review_items": [
                                         {"item_id": 1, "status": "correct"},
                                         {"item_id": 2, "status": "wrong"}
                                     ]
                                 }),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json)

if __name__ == '__main__':
    unittest.main()