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
@PermissionVerify()
def WriteArticle(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('ReadArticle'))
    else:
        form = ArticleForm()

    kwvars = {
        'form': form,
        'request': request,
    }
    return render_to_response('BlogManage/blog.write.html', kwvars, RequestContext(request))


@login_required
@PermissionVerify()
def ReadArticle(request):
    mArticle = Article.objects.all()
    lst = SelfPaginator(request, mArticle, 20)
    kwvars = {
        'lPage': lst,
        'request': request,
    }

    return render_to_response('BlogManage/blog.read.html', kwvars, RequestContext(request))