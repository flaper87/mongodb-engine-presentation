from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('mongodb_engine_presentation.presentation.views',
    url(r'^$', 'home', name="home"),
)
