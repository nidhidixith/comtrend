from youtube_search import YoutubeSearch

results=YoutubeSearch('Standup Comedy',max_result=10).to_dict()
a=results.get("link")
print(a)






<ul>
    {% for item in result %}
        <li ><h3>Comedian name:{{item.name}}</h3></h3>
        <h3>Genre:{{item.genre}}</h3></h3> </li>
        <p align="center">
        <iframe width="420" height="200" src="https://www.youtube.com/embed/{{item.link}}" allowfullscreen></iframe>
        </p>
    {% endfor %}

</ul>













search_url='https://www.googleapis.com/youtube/v3/search'
    params={
        'part':'snippet',
        'q':'learn python',
        'key': settings.YOUTUBE_DATA_API_KEY
    }
    video_ids=[]
























connection = pymysql.connect(host='localhost',database='mainschema',user='root', password='root123')
    mysql_insert_query = """INSERT INTO byindians(link) VALUES("https") """

    cursor = connection.cursor()
    cursor.execute(mysql_insert_query)
    connection.commit()
    result=byindians.objects.all()
    return render(request,'firstpage.html',{'result':result})




















query_string = urllib.parse.urlencode({"standup comedy": input()})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return HttpResponse("http://www.youtube.com/watch?v=" + search_results[0])
