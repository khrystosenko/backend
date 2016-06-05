from django.test import TestCase
from django.conf import settings

from rest_framework.views import APIView

from libs.decorators import APIThrottleWrapper


class APIThrottleWrapperTest(TestCase):

    class TestThrottle(object):
        pass

    class TestThrottle1(object):
        pass

    throttle_classes = [TestThrottle, TestThrottle1]

    def get_class(self):
        @APIThrottleWrapper(self.throttle_classes)
        class TestView(APIView): pass

        return TestView

    def test_throttles_are_not_bounded(self):
        with self.settings(TEST_SERVER=True):
            self.assertEqual(self.get_class().throttle_classes, [])

    def test_throtles_are_bounded(self):
        with self.settings(TEST_SERVER=False):
            self.assertEqual(self.get_class().throttle_classes, self.throttle_classes)
