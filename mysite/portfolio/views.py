from django.conf import settings
from django.contrib.sites.models import get_current_site
import datetime

from utils.functions import response
from mysite.models import DEPARTMENT_CHOICES
from aboutme.models import Source
from models import Project, Education, Course, Assignment


# Portfolio page view
def portfolio(request):
    errors = []
    sources = Source.objects.order_by('priority', 'type', 'title' )
    projects = Project.objects.order_by('date').reverse()
    education = []
    departments = DEPARTMENT_CHOICES
    institution = Education.objects.order_by('graduation_date').reverse()
    for i in institution:
        dept_courses = []
        for d in departments:
            courses = Course.objects.filter(department=d[0]).order_by('number').reverse()
            course_asgs = []
            if courses:
                for c in courses:
                    asgs = Assignment.objects.filter(course=c).order_by('identification')
                    course_asgs.append((c, asgs))
            if course_asgs:
                dept_courses.append((d[-1], course_asgs))
        education.append((i, dept_courses))

    template = 'portfolio.html'
    context = {
        'errors': errors,
        'sources': sources,
        'projects': projects,
        'education': education,
    }
    return response(request, template, context)
