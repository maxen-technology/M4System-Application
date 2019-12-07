from django.core.management.base import BaseCommand, CommandError
from webview.models import UserProfile, Widgets, UserView
from scheduler.models import Hosts, HostChecks, Historical, EventLog, Sla, SlaLog
from django.contrib.auth.models import Group, User
# from tools import dbg, setmd, getmd, loadmd, savemd, getMetadata, setMetadata
# import datetime
# from django.template.loader import render_to_string
# from django.core.mail import send_mass_mail
from django.utils import timezone


class Command(BaseCommand):
    help = 'Group Report'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Group membership report.'))

        for g in Group.objects.filter():

            self.stdout.write(self.style.SUCCESS(g.name))
            for u in g.user_set.filter(is_active=True):
                self.stdout.write("     " + u.userprofile.notifemail)


