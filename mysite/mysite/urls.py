from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
     
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$','myapp.views.search',name='add'),
    url(r'^$','myapp.views.home'),
    url(r'^anime/$','myapp.views.anime',name='anime'),
    url(r'^comic/$','myapp.views.comic',name='comic'),
    url(r'^book/$','myapp.views.book',name='book'),
    url(r'^accounts/',include('users.urls')),
    url(r'^updata/$','myapp.views.check',name='update'),

    url(r'^updata/anime/add/$','myapp.views.updata_anime_add'),
    url(r'^updata/anime/del/$','myapp.views.updata_anime_del'),
    url(r'^updata/anime/cha/$','myapp.views.updata_anime_cha'),
    url(r'^updata/comic/add/$','myapp.views.updata_comic_add'),
    url(r'^updata/comic/del/$','myapp.views.updata_comic_del'),
    url(r'^updata/comic/cha/$','myapp.views.updata_comic_cha'),
    url(r'^updata/books/add/$','myapp.views.updata_book_add'),
    url(r'^updata/books/del/$','myapp.views.updata_book_del'),
    url(r'^updata/books/cha/$','myapp.views.updata_book_cha'),

    url(r'^anime/(.+)/$','myapp.views.exact_anime'),
    url(r'^comic/(.+)/$','myapp.views.exact_comic'),
    url(r'^book/(.+)/$','myapp.views.exact_book'),

    url(r'^register/$','myapp.views.register'),
    url(r'^login/$','myapp.views.login'),
    #url(r'^logout/$','myapp.views.logout'),
    url(r'^comment/$','myapp.views.comment'),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),

)
