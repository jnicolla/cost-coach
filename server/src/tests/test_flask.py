from app import calculate
from app import ret_app
import unittest
app = ret_app()
class FlaskTestCase(unittest.TestCase):

    #Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response= tester.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

# if __name__ == '__main__':
#     unittest.main()