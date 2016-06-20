from django.conf.urls import patterns, include, url
from . import views




urlpatterns = [
    url(r'^$', views.exam_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
	url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
	url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
	url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^question/new/(?P<pk>[0-9]+)/$', views.question_new, name='question_new'),
    url(r'^question/(?P<pk>[0-9]+)/$', views.question_detail),
    url(r'^question/(?P<pk>[0-9]+)/edit/$', views.question_edit, name='question_edit'),
    url(r'^option/new/(?P<pk>[0-9]+)/$', views.option_new, name='option_new'),
    url(r'^option/(?P<pk>[0-9]+)/edit/$', views.option_edit, name='option_edit'),
    url(r'^exam/new/$', views.exam_new, name='exam_new'),
    url(r'^exam/choose/$', views.choose_exam, name='choose_exam'),
    url(r'^exam/(?P<pk>[0-9]+)/$', views.question_list, name='question_list'),
    url(r'^exam/(?P<pk>[0-9]+)/edit/$', views.exam_edit, name='exam_edit'),
    url(r'^examtemplate/new/$', views.exam_template_new, name='exam_template_new'),
    url(r'^examtemplate/(?P<pk>[0-9]+)/$', views.exam_template_detail),
    url(r'^examtemplate/(?P<pk>[0-9]+)/edit/$', views.exam_template_edit, name='exam_template_edit'),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^exam/notfinished/', views.notfinished_exams, name='not_finished_exams'),
    url(r'^exam/finished/', views.finished_exams, name='finished_exams'),
    url(r'^texto-alternativo/', views.show_error, name='show_error'),

]
