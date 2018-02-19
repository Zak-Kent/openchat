from datetime import datetime, timedelta

from openspaces import models

def get_ignored_users():
    """
    Check app config table to get list of ignored twitter ids
    """
    config_obj = models.OutgoingConfig.objects.latest("id")
    ignore_list = [tw_id for tw_id in config_obj.ignore_users]
    return ignore_list

def get_or_create_user_and_tweet(status):
    """
    Take a status from twitter and either create or update info for tweet & user
    """
    user, created = models.User.objects.get_or_create(id_str=str(status.user.id))
    user.screen_name = status.user.screen_name
    user.save()

    # save tweet record to StreamedTweet model
    tweet_record, created = models.StreamedTweet.objects.get_or_create(id_str=status.id_str)
    tweet_record.id_str = status.id_str
    tweet_record.user = user
    tweet_record.text = status.text
    tweet_record.source = status.source
    tweet_record.save() 

def check_for_auto_send():
    """
    Check config table and return auto send value
    """
    config_obj = models.OutgoingConfig.objects.latest("id")
    approved = 1 if config_obj.auto_send else 0
    return approved

def save_outgoing_tweet(**kwargs):
    """
    Save a tweet object to the outgoing tweet table triggering celery stuff
    """
    models.OutgoingTweet.objects.create(**kwargs)

def check_time_room_conflict(a_time, a_room, mins_before=15, mins_after=30):
    """
    Check to see if there is already a tweet scheduled to go out about 
    an event in the same time and room. Helps avoid duplicate retweets
    about the same event sent by multiple users. Currently the retweets
    from bot are first come first serve for a unqiue room and time stamp. 
    """
    start_time = a_time - timedelta(minutes=mins_before)
    end_time = a_time + timedelta(minutes=mins_after)
    event_conflict = models.OpenspacesEvent.objects.filter(location=a_room) \
                           .filter(start__range=(start_time, end_time))
    return True if event_conflict else False

def create_event(**kwargs):
    """
    Create event record with a description, creator, time, and room
    """
    models.OpenspacesEvent.objects.create(**kwargs)

def setup_outgoing_config():
    models.OutgoingConfig.objects.create(auto_send=True,
                                         default_send_interval=15,
                                         ignore_users=[])
