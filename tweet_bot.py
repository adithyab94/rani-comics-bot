# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 14:12:41 2021

@author: DELL
"""
import twitter
from imgurpython import ImgurClient
import time
from os import environ
import random
from apscheduler.schedulers.blocking import BlockingScheduler

def post_image(image_url, consumer_key, consumer_secret, access_token_key, access_token_secret):
    api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)
    api.VerifyCredentials()
    api.PostUpdate("", media=image_url)
    

def get_images(album_id, client_id, client_secret):
    client = ImgurClient(client_id, client_secret)
    return client.get_album_images(album_id)

album_id = ['sbgCnpx','HACfOjF','1MAbcit']

imgur_client_id = environ['CLIENT_ID']
imgur_client_secret = environ['CLIENT_SECRET']

twitter_consumer_key = environ['CONSUMER_KEY']
twitter_consumer_secret = environ['CONSUMER_SECRET']
twitter_access_token_key = environ['ACCESS_KEY']
twitter_access_token_secret = environ['ACCESS_SECRET']


sched = BlockingScheduler()
    
@sched.scheduled_job('interval', hours=8)
def timed_job():
    images = get_images(album_id[0], imgur_client_id, imgur_client_secret)
    image = random.choice(images)
    post_image(image.link, twitter_consumer_key, twitter_consumer_secret, twitter_access_token_key, twitter_access_token_secret)

@sched.scheduled_job('interval', hours=14)
def timed_job2():
    images = get_images(album_id[1], imgur_client_id, imgur_client_secret)
    image = random.choice(images)
    post_image(image.link, twitter_consumer_key, twitter_consumer_secret, twitter_access_token_key, twitter_access_token_secret)

@sched.scheduled_job('interval', hours=18)
def timed_job2():
    images = get_images(album_id[2], imgur_client_id, imgur_client_secret)
    image = random.choice(images)
    post_image(image.link, twitter_consumer_key, twitter_consumer_secret, twitter_access_token_key, twitter_access_token_secret)    
    
sched.start()
