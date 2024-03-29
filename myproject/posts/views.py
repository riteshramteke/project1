from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize
# Create your views here.
from django.core.paginator import Paginator
from .models import Post

def get_posts(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    page_obj=serialize ("python",paginator.get_page(page))
    return JsonResponse ({"data":page_obj})
    
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="python",
        user_id='1',
        default_version='v1',
        body="python learning",
        
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
