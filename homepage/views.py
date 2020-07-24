import json
import os

import googleapiclient.discovery
import googleapiclient.errors
import requests

from django.http import HttpResponse
from .models import firsttable
from .models import byindians
from django.shortcuts import render
from django.db import IntegrityError


def firstview(request):
    return render(request,'index.html')


def index(request):
   # scopes = ["https://www.googleapis.com/auth/youtube.force-ssl", "https://www.googleapis.com/auth/youtube"]

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    developer_key = 'AIzaSyBo-V2OWdtUNmT__PTy5xRjSKngUOYStps'

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=developer_key)
    request_search = youtube.search().list(
        part="snippet",
        maxResults=50,
        order="viewCount",
        publishedAfter="2014-01-01T00:00:00Z",
        q="most viewed standup comedy",
        type="video",
        videoDuration="medium"
    )
    response = request_search.execute()


    #return HttpResponse(response)
    parser = json.loads(json.dumps(response))

    all_videos = parser['items']
    #return HttpResponse(all_videos)
    for each_video in all_videos:
        video_parser = json.loads(json.dumps(each_video))
        video_id = video_parser['id']['videoId']
        video_endpoint_snippet = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id=" + video_id + "&key=" + developer_key
        r = requests.get(url=video_endpoint_snippet)
        response_parser = json.loads(json.dumps(r.json()))
        title = response_parser['items'][0]['snippet']['title']
        published_at = response_parser['items'][0]['snippet']['publishedAt']
        description = response_parser['items'][0]['snippet']['description'][0:100]
        channel = response_parser['items'][0]['snippet']['channelTitle']
        try:
            tags = response_parser['items'][0]['snippet']['tags']
        except KeyError:
            tags = ""
        try:
            language = response_parser['items'][0]['snippet']['defaultAudioLanguage']
        except KeyError:
            language = ""

        video_content_details = "https://www.googleapis.com/youtube/v3/videos?part=contentDetails&id=" + video_id + "&key=" + developer_key
        r = requests.get(url=video_content_details)
        response_parser = json.loads(json.dumps(r.json()))
        try:
            duration = response_parser['items'][0]['contentDetails']['duration']
        except KeyError:
            duration=""
        video_endpoint_statistics = "https://www.googleapis.com/youtube/v3/videos?part=statistics&id=" + video_id + "&key=" + developer_key
        r = requests.get(url=video_endpoint_statistics)
        response_parser = json.loads(json.dumps(r.json()))
        try:
            view_count = response_parser['items'][0]['statistics']['viewCount']
        except KeyError:
            view_count=""
        try:
            like_count = response_parser['items'][0]['statistics']['likeCount']
        except KeyError:
            like_count=""
        try:
            dislike_count = response_parser['items'][0]['statistics']['dislikeCount']
        except KeyError:
            dislike_count=""
        try:
            favorite_count = response_parser['items'][0]['statistics']['favoriteCount']
        except KeyError:
            favorite_count=""
        try:
            comment_count = response_parser['items'][0]['statistics']['commentCount']
        except KeyError:
            comment_count=""
        video_endpoint_topics = "https://www.googleapis.com/youtube/v3/videos?part=topicDetails&id=" + video_id + "&key=" + developer_key
        r = requests.get(url=video_endpoint_topics)
        response_parser = json.loads(json.dumps(r.json()))
        try:
            categories = response_parser['items'][0]['topicDetails']['topicCategories']
        except KeyError:
            categories = []
        categories = [category.split("https://en.wikipedia.org/wiki/") for category in categories]
        link="https://www.youtube.com/watch?v="+video_id

        try:
            byindians.objects.create(title=title, published_at=published_at, duration=duration,description=description, channel=channel, view_count=view_count, like_count=like_count,dislike_count=dislike_count,
                                 favorite_count=favorite_count, comment_count=comment_count, language=language,
                                 tags=tags, categories=categories,type="Most Viewed Standup Comedy",
                                 video_id=video_id)
        except Exception:
           ""


    res=byindians.objects.all()
    #return render(request,'firstpage.html',{'res':res})
    return HttpResponse("HELLO")

def indians(request):
    res=""

    if 'indians' in request.POST:
        res = byindians.objects.filter(type="Indian Standup Comedy")
    elif 'americans' in request.POST:
        res = byindians.objects.filter(type="American Standup Comedy")
    elif 'kids' in request.POST:
        res = byindians.objects.filter(type="Kids Standup Comedy")
    elif 'classics' in request.POST:
        res = byindians.objects.filter(type="Classic Standup Comedy")
    elif 'mostviewed' in request.POST:
        res = byindians.objects.filter(type="Most Viewed Standup Comedy")
    elif 'short' in request.POST:
        res = byindians.objects.filter(type="Short Standup Comedy")
    elif 'medium' in request.POST:
        res = byindians.objects.filter(type="Medium Length Standup Comedy")
    elif 'long' in request.POST:
        res = byindians.objects.filter(type="Long Standup Comedy")


    return render(request, 'firstpage.html', {'res': res})



'''def americans(request):
    res=""
    if 'americans' in request.POST:
        res = byindians.objects.filter(type="American Standup Comedy")
    return render(request,'firstpage.html',{'res':res})

def kids(request):
    res = byindians.objects.filter(type="Kids Standup Comedy")
    return render(request,'firstpage.html',{'res':res})

def classics(request):
    res = byindians.objects.filter(type="Classic Standup Comedy")
    return render(request,'firstpage.html',{'res':res})

def mostviewed(request):
    res = byindians.objects.filter(type="Most Viewed Standup Comedy")
    return render(request,'firstpage.html',{'res':res})'''




