from django.conf.urls import url
from interviews.views import interview_views, other_views

urlpatterns = (
    url(
        regex=r'^$',
        view=interview_views.InterviewListView.as_view(),
        name='interviews_interview_list'
    ),
    url(
        regex=r'^interview/(?P<slug>.+?)/$',
        view=interview_views.InterviewDetailView.as_view(),
        name='interviews_interview_detail'
    ),
    url(
        regex=r'^interviews/$',
        view=interview_views.InterviewArchiveIndexView.as_view(),
        name='interviews_interview_archive_index'
    ),
    url(
        regex=r'^interview/archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        view=interview_views.InterviewMonthArchiveView.as_view(),
        name='interviews_interview_month_archive'
    ),
    url(
        regex=r'^interview/archive/(?P<year>\d{4})/$',
        view=interview_views.InterviewYearArchiveView.as_view(),
        name='interviews_interview_year_archive'
    ),
    url(
        regex=r'^about/$',
        view=other_views.AboutView.as_view(),
        name='interviews_other_about'
    ),
)
