from rest_framework.throttling import AnonRateThrottle


class VoteAnonRateThrottle(AnonRateThrottle):
	rate = '5/hour'
