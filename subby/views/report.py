import difflib

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from subby.decorators.loginrequiredmessage import message_login_required
from subby.models.report import Report
from subby.models.sublet import Sublet

User = get_user_model()


@message_login_required
def create_report(request, user_id, sublet_id):
    if request.method == 'POST':
        if request.POST.get('issue', None) and request.POST['description']:
            user = User.objects.get(id=user_id)
            sublet = Sublet.objects.get(id=sublet_id)

            Report.objects.create_report(user=user,
                                         sublet=sublet,
                                         issue=request.POST['issue'],
                                         description=request.POST['description'],
                                         )
            messages.add_message(request, messages.SUCCESS, 'You have successfully left a report.')
            return redirect('subby:SubletDetail', sublet_id)
        else:
            messages.add_message(request, messages.ERROR, 'All fields must be checked/filled in.')
            return redirect('subby:SubletDetail', sublet_id)

    report_dict = {
        'user_id': user_id,
        'sublet_id': sublet_id,
    }
    return render(request, 'report/report_page.html', report_dict)


def report_list(request):
    reports = Report.objects.all()
    return render(request, "report/report_list.html", {'reports': reports})


def search_report(request):
    if request.method == 'POST':
        reports = Report.objects.all()
        if request.POST['query']:
            filtered_reports = []
            for r in reports:
                if difflib.SequenceMatcher(None, r.user.email, request.POST['query']).ratio() > 0.3:
                    filtered_reports.append(r)
            messages.add_message(request, messages.INFO, 'Total results: ' + str(len(filtered_reports)))
            return render(request, "report/report_list.html", {'reports': filtered_reports})
        else:
            return render(request, "report/report_list.html", {'reports': reports})
