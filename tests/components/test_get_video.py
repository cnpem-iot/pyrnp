import unittest

from pyrnp import RNP
import responses


def suite():
    """Define all the tests of the module."""
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(GetVideoTestCase))
    return suite


class GetVideoTestCase(unittest.TestCase):
    def setUp(self):
        self.client = RNP(client_id="ID", client_key="KEY", json=False)

    @responses.activate
    def test_can_get_video(self):
        responses.add(responses.GET, "https://eduplay.rnp.br/services/video/origin/versions/video_id")
        self.client.get_video(id="video_id")


if __name__ == "__main__":
    unittest.main()
