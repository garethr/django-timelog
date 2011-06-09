from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

from timelog.lib import generate_table_from, analyze_log_file, PATTERN


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--file',
            dest='file',
            default=settings.TIMELOG_LOG,
            help='Specify file to use'),
        make_option('--noreverse',
            dest='reverse',
            action='store_false',
            default=True,
            help='Show paths instead of views'),
        )

    def handle(self, *args, **options):
        # --date-from YY-MM-DD
        #   specify a date filter start
        #   default to first date in file
        # --date-to YY-MM-DD
        #   specify a date filter end
        #   default to now

        LOGFILE = options.get('file')

        try:
            data = analyze_log_file(LOGFILE, PATTERN, reverse_paths=options.get('reverse'))
        except IOError:
            print "File not found"
            exit(2)

        print generate_table_from(data)
