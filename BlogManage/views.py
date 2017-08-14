from django.shortcuts import render
from BlogManage.models import Article
from BlogManage.forms import ArticleForm
from UserManage.models import User
from django.contrib.auth.decorators import login_required
from UserManage.views.permission import PermissionVerify
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response,RequestContext
from website.common.CommonPaginator import SelfPaginator


@login_required
# @PermissionVerify()
def WriteArticle(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.author = request.user
            form.save()
            return HttpResponseRedirect(reverse('blog_read',kwargs={'username':request.user.username}))
    else:
        form = ArticleForm()

    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('BlogManage/blog.write.html', kwvars, RequestContext(request))


# @login_required
# @PermissionVerify()
def ReadArticle(request,username):
    author_list = User.objects.filter(username=username)
    if(len(author_list)!=1):
        return render_to_response("Not a useful adress.")
    article_list = Article.objects.filter(author=author_list[0])
    # lst = SelfPaginator(request, article_list, 20)
    kwvars = {
        # 'lPage': lst,
        'request': request,
        'article_list':article_list,
        'author':author_list[0]
    }
    return render_to_response('BlogManage/blog.read.html', kwvars, RequestContext(request))


def PublicArticle(request):

    import random
    article_list  =Article.objects.all()
    if(len(article_list)>10):
        article_list = random.sample(article_list,10)

    kwvars = {
        # 'lPage': lst,
        'request': request,
        'article_list':article_list,
    }

    return render_to_response("BlogManage/blog.public.html",kwvars,RequestContext(request))