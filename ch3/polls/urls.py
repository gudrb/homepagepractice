from django.conf.urls import url
from polls import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<question_id>\d+)/$',views.detail,name='detail'),
    url(r'^(?P<question_id>\d+)/vote/$',views.vote,name='vote'), # detail.html 제출시 호출됨
    url(r'^(?P<question_id>\d+)/results/$',views.results,name='results'),
]#(?P<question_id>\d+) 파라미터 추출 식, 뷰에 전달