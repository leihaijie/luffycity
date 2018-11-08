from django.conf.urls import url, include

from api.views import course, account


urlpatterns = [
    url(r'^course/$', course.CourseView.as_view({"get": "list"})),
    url(r'^course/(?P<pk>\d+)/$', course.CourseView.as_view({'get': 'retrieve'})),

    url(r'^auth/$', account.AuthView.as_view()),
    url(r'^micro/$', course.MicroView.as_view()),

]
