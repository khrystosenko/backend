from django.conf import settings


class APIThrottleWrapper(object):

    def __init__(self, throttle_classes):
        self.throttle_classes = throttle_classes

    def __call__(self, cls):
        if not settings.TEST_SERVER:
            cls.throttle_classes = self.throttle_classes

        return cls
