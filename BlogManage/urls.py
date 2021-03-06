from django.conf.urls import patterns, include, url
from .views import WriteArticle,ReadArticle,PublicArticle,ManageArticle
urlpatterns = patterns('BlogManage.views',
#     url(r'^login/$', 'user.LoginUser', name='loginurl'),
#     url(r'^logout/$', 'user.LogoutUser', name='logouturl'),
url(r'write/$',WriteArticle,name='blog_write'),
url(r'read/(?P<username>[a-zA-Z0-9]+)/$',ReadArticle,name='blog_read'),
url(r'public/$',PublicArticle,name='public_article'),
url(r'manage/$',ManageArticle,name='blog_manage')
)
