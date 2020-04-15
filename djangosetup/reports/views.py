from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import Report, Comment


class IndexView(generic.ListView):
    template_name = 'reports/index.html'
    context_object_name = 'latest_reports_list'

    def get_queryset(self):
        """
        Return the last five published reports (not including those set to be
        published in the future).
        """
        return Report.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Report
    template_name = 'reports/detail.html'

    def get_queryset(self):
        """
        Excludes any reports that aren't published yet.
        """
        return Report.objects.filter(pub_date__lte=timezone.now())


def like(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    report.report_likes += 1
    report.save()
    return HttpResponseRedirect(reverse('reports:detail', args=(report.id,)))


def comment(request, report_id):
    report = get_object_or_404(Report, pk=report_id)
    comm = request.POST['comm']
    new_comm = Comment(report=report, comment_text=comm)
    new_comm.save()
    return HttpResponseRedirect(reverse('reports:detail', args=(report.id,)))
