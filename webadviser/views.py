#from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import articlesForCouple
import json

class ArticleView(APIView):

    def post(self, request):       
        #get magic number
        man_date = request.data.get("man_date")
        woman_date = request.data.get("woman_date")
        MagicNumber = sum(int(i) for i in str(man_date + woman_date).replace(".",""))%9
        
        #get article
        article = articlesForCouple.objects.get(id = MagicNumber)
        
        #get data
        article_number = article.number
        article_title = article.title
        article_text = article.text
        
        json_string = {"article_num": article_number, "article_title":article_title, "article_text":article_text}
        
        
        return Response(json_string)

