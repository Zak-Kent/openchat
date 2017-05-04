from datetime import datetime
from django.test import TestCase, Client
from freezegun import freeze_time

from twote.models import OutgoingTweet, OutgoingConfig

class TestOutgoingTweetModelSaveMethod(TestCase):
    """
    Test to check that OutgoingTweet model calcs the scheduled_time 
    field when a tweet object is approved to be sent
    """
    def setUp(self):
        OutgoingConfig.objects.create(auto_send=True, 
                                      default_send_interval=1,
                                      ignore_users=[])

    @freeze_time("2017-03-03")
    def test_approved_tweet_gets_scheduled_time_auto_calculated(self):
        OutgoingTweet.objects.create(tweet="test tweet", approved=1)
        my_tweet = OutgoingTweet.objects.get(tweet="test tweet")

        start_time = datetime.utcnow()
        time_diff = my_tweet.scheduled_time - start_time

        self.assertEqual(bool(my_tweet.scheduled_time), True)
        # scheduled time should be 60 seconds into the future
        self.assertEqual(time_diff.seconds, 60)

    @freeze_time("2017-03-03")
    def test_no_default_send_interval_gets_sent_in_15_mins(self):
        # use OutgoingConfig's default interval withou override
        OutgoingConfig.objects.create(auto_send=True, 
                                      ignore_users=[])

        OutgoingTweet.objects.create(tweet="test tweet", approved=1)
        my_tweet = OutgoingTweet.objects.get(tweet="test tweet")

        start_time = datetime.utcnow()
        time_diff = my_tweet.scheduled_time - start_time

        # scheduled time should be 900 seconds (15mins) into the future
        self.assertEqual(time_diff.seconds, 900)

        
    def test_non_approved_tweet_gets_no_scheduled_time(self):
        OutgoingTweet.objects.create(tweet="non approved tweet", approved=0)
        pending_tweet = OutgoingTweet.objects.get(tweet="non approved tweet")

        self.assertEqual(bool(pending_tweet.scheduled_time), False)

    def test_tweet_gets_scheduled_time_when_approved_set_to_true(self):
        """
        A tweet object is created and is pending approval, later it is changed
        to approved and has it's scheduled time is calculated when approved.
        A tweets scheduled time will only be calculated when the model's save
        method is called.
        """
        pending_tweet = OutgoingTweet.objects.create(tweet="pending tweet", approved=0)
        self.assertEqual(bool(pending_tweet.scheduled_time), False)

        # pending_tweet is approved by user
        pending_tweet.approved = 1
        pending_tweet.save()

        self.assertEqual(bool(pending_tweet.scheduled_time), True)


class TestUserModelIgnoreInteractions(TestCase):
    """
    Test the interaction bewteen the OutgoingConfig model's ignore_users field
    and the user model save method that uses signal to update ignore_users 
    """

