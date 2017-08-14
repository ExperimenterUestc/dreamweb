from django.shortcuts import render
from BlogManage.models import Article
from BlogManage.forms import ArticleForm
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
            return HttpResponseRedirect(reverse('blog_read'))
    else:
        form = ArticleForm()

    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('BlogManage/blog.write.html', kwvars, RequestContext(request))


@login_required
# @PermissionVerify()
def ReadArticle(request):

    article_list = Article.objects.all()
    # lst = SelfPaginator(request, article_list, 20)
    kwvars = {
        # 'lPage': lst,
        'request': request,
        'article_list':article_list,
    }
    return render_to_response('BlogManage/blog.read.html', kwvars, RequestContext(request))