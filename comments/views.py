from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from blogp.models import Post
# Create your views here.
from django.core.validators import validate_email
from .models import Comment

def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    print(post)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        url = request.POST.get('url')
        comment = request.POST.get('comment')
        # validate_email(email)校验邮箱 正确返回None,错误返回提示
        if not name or not email or not comment or validate_email(email):
            # 根据post找出所有的评论
            comment_list = post.comment.all()
            context = {'post': post, 'comment_list': comment_list}
            print('comment not ok')
            return render(request, 'blogp/detial.html', context=context)
        Comment.objects.create(name=name,email=email,url=url,text=comment,post=post)
        return redirect(reverse('blog:detial', kwargs={'id': post_id}))
    else:
        return redirect(reverse('blog:detial', kwargs={'id': post_id}))
