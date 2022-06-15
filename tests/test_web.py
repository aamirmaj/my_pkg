import unittest
import modules.web.get_site
from modules.web.get_site import get_site

class TestWeb(unittest.TestCase):
    def test_get_url_OK(self):
        url = 'www.archlinux.org'
        response = get_site(url)
        self.assertEqual(response.status_code, 200)

    def test_get_url_NOK(self):
        url = 'NOT_A_WEBSITE'
        response = None
        try:
            response = get_site(url)
        except Exception as err:
            print(str(err))
        if response:
            print(str(response))
            raise Exception("URL passed?")

if __name__ == '__main__':
    unittest.main()
