from django.views.generic import ListView, DetailView, CreateView, \
                                 DeleteView, UpdateView, \
                                 ArchiveIndexView, DateDetailView, \
                                 DayArchiveView, MonthArchiveView, \
                                 TodayArchiveView, WeekArchiveView, \
                                 YearArchiveView


from interviews.models import Interview


class InterviewView(object):
    model = Interview

    def get_template_names(self):
        """Nest templates within interview directory."""
        tpl = super(InterviewView, self).get_template_names()[0]
        app = self.model._meta.app_label
        mdl = 'interview'
        self.template_name = tpl.replace(app, '{0}/{1}'.format(app, mdl))
        return [self.template_name]


class InterviewDateView(InterviewView):
    date_field = 'date'
    month_format = '%m'


class InterviewBaseListView(InterviewView):
    paginate_by = 10


class InterviewArchiveIndexView(InterviewDateView, InterviewBaseListView, ArchiveIndexView):
    pass


class InterviewCreateView(InterviewView, CreateView):
    pass


class InterviewDeleteView(InterviewView, DeleteView):

    def get_success_url(self):
        from django.core.urlresolvers import reverse
        return reverse('interviews_interview_list')


class InterviewDetailView(InterviewView, DetailView):
    pass


class InterviewListView(InterviewBaseListView, ListView):
    pass


class InterviewMonthArchiveView(InterviewDateView, InterviewBaseListView, MonthArchiveView):
    pass


class InterviewUpdateView(InterviewView, UpdateView):
    pass


class InterviewYearArchiveView(InterviewDateView, InterviewBaseListView, YearArchiveView):
    make_object_list = True
