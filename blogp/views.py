from django.http import HttpResponse,JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import *
import markdown
# 导入分页模块
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db.models import F
# Create your views here.


def index(request):
    # 按照文章创建时间降序
    post_list = Post.objects.all()
    # a = Post.objects.filter(create_time__month='02')
    pagintar = Paginator(post_list,8)
    page = pagintar.page(1)
    a = Post.objects.filter(create_time__year='2020', create_time__month='02')
    return render(request, 'blogp/index.html', locals())


def detial(request, id):
    post = Post.objects.filter(id=id)
    if not post:
        return render(request,'404.html')
    post.update(views=F('views')+1)
    post=post[0]
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    comment_list = post.comment.all().order_by('-created_time')
    paginator = Paginator(comment_list, 3)
    cur_page = int(request.GET.get('page', 1))
    page = paginator.page(cur_page)
    context = {
        'page': page,
        'post': post,
    }
    return render(request, 'blogp/detial.html', context=context)

def archives(request, year, month):
    """
    根据归档日期查询博客
    :param request:
    :param year: 年
    :param month: 月
    :return:
    """
    # filter过滤时间注意时区的问题
    post_list = Post.objects.filter(create_time__year='2020', create_time__month=month)
    return render(request, 'blogp/index.html', locals())


def category(request, id):
    """根据分类查询博客"""
    cate = get_object_or_404(Category, id=id)
    post_list = cate.post.order_by('-create_time')
    return render(request, 'blogp/index.html', context={'post_list': post_list})



