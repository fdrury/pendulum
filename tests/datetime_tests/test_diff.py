from datetime import datetime
from contextlib import contextmanager
from pendulum import DateTime

from .. import AbstractTestCase


class DiffTest(AbstractTestCase):

    @contextmanager
    def wrap_with_test_now(self, dt=None):
        if dt is None:
            dt = DateTime.create(2012, 1, 1, 1, 2, 3)

        DateTime.set_test_now(dt)

        yield

        DateTime.set_test_now()

    def test_diff_in_years_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(1, dt.diff(dt.copy().add(years=1)).in_years())

    def test_diff_in_years_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(-1, dt.diff(dt.copy().subtract(years=1), False).in_years())

    def test_diff_in_years_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(1, dt.diff(dt.copy().subtract(years=1)).in_years())

    def test_diff_in_years_vs_default_now(self):
        with self.wrap_with_test_now():
            self.assertEqual(1, DateTime.now().subtract(years=1).diff().in_years())

    def test_diff_in_years_ensure_is_truncated(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(1, dt.diff(dt.copy().add(years=1).add(months=7)).in_years())

    def test_diff_in_months_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(13, dt.diff(dt.copy().add(years=1).add(months=1)).in_months())

    def test_diff_in_months_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(-11, dt.diff(dt.copy().subtract(years=1).add(months=1), False).in_months())

    def test_diff_in_months_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(11, dt.diff(dt.copy().subtract(years=1).add(months=1)).in_months())

    def test_diff_in_months_vs_default_now(self):
        with self.wrap_with_test_now():
            self.assertEqual(12, DateTime.now().subtract(years=1).diff().in_months())

    def test_diff_in_months_ensure_is_truncated(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(1, dt.diff(dt.copy().add(months=1).add(days=16)).in_months())

    def test_diff_in_days_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(366, dt.diff(dt.copy().add(years=1)).in_days())

    def test_diff_in_days_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(-365, dt.diff(dt.copy().subtract(years=1), False).in_days())

    def test_diff_in_days_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(365, dt.diff(dt.copy().subtract(years=1)).in_days())

    def test_diff_in_days_vs_default_now(self):
        with self.wrap_with_test_now():
            self.assertEqual(7, DateTime.now().subtract(weeks=1).diff().in_days())

    def test_diff_in_days_ensure_is_truncated(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(1, dt.diff(dt.copy().add(days=1).add(hours=13)).in_days())

    def test_diff_in_weekdays_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(21, dt.diff(dt.end_of('month')).in_weekdays())

    def test_diff_in_weekdays_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 31)
        self.assertEqual(21, dt.diff(dt.start_of('month')).in_weekdays())

    def test_diff_in_weekdays_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 31)
        self.assertEqual(-21, dt.diff(dt.start_of('month'), False).in_weekdays())

    def test_diff_in_weekend_days_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(10, dt.diff(dt.end_of('month')).in_weekend_days())

    def test_diff_in_weekend_days_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 31)
        self.assertEqual(10, dt.diff(dt.start_of('month')).in_weekend_days())

    def test_diff_in_weekend_days_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 31)
        self.assertEqual(-10, dt.diff(dt.start_of('month'), False).in_weekend_days())

    def test_diff_in_weeks_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(52, dt.diff(dt.copy().add(years=1)).in_weeks())

    def test_diff_in_weeks_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(-52, dt.diff(dt.copy().subtract(years=1), False).in_weeks())

    def test_diff_in_weeks_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(52, dt.diff(dt.copy().subtract(years=1)).in_weeks())

    def test_diff_in_weeks_vs_default_now(self):
        with self.wrap_with_test_now():
            self.assertEqual(1, DateTime.now().subtract(weeks=1).diff().in_weeks())

    def test_diff_in_weeks_ensure_is_truncated(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(0, dt.diff(dt.copy().add(weeks=1).subtract(days=1)).in_weeks())

    def test_diff_in_hours_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(26, dt.diff(dt.copy().add(days=1).add(hours=2)).in_hours())

    def test_diff_in_hours_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(-22, dt.diff(dt.copy().subtract(days=1).add(hours=2), False).in_hours())

    def test_diff_in_hours_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(22, dt.diff(dt.copy().subtract(days=1).add(hours=2)).in_hours())

    def test_diff_in_hours_vs_default_now(self):
        with self.wrap_with_test_now(DateTime.create(2012, 1, 15)):
            self.assertEqual(48, DateTime.now().subtract(days=2).diff().in_hours())

    def test_diff_in_hours_ensure_is_truncated(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(1, dt.diff(dt.copy().add(hours=1).add(minutes=31)).in_hours())

    def test_diff_in_minutes_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(62, dt.diff(dt.copy().add(hours=1).add(minutes=2)).in_minutes())

    def test_diff_in_minutes_positive_big(self):
        dt = DateTime(2000, 1, 1)
        self.assertEqual(1502, dt.diff(dt.copy().add(hours=25).add(minutes=2)).in_minutes())

    def test_diff_in_minutes_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(-58, dt.diff(dt.copy().subtract(hours=1).add(minutes=2), False).in_minutes())

    def test_diff_in_minutes_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(58, dt.diff(dt.copy().subtract(hours=1).add(minutes=2)).in_minutes())

    def test_diff_in_minutes_vs_default_now(self):
        with self.wrap_with_test_now():
            self.assertEqual(60, DateTime.now().subtract(hours=1).diff().in_minutes())

    def test_diff_in_minutes_ensure_is_truncated(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(1, dt.diff(dt.copy().add(minutes=1).add(seconds=59)).in_minutes())

    def test_diff_in_seconds_positive(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(62, dt.diff(dt.copy().add(minutes=1).add(seconds=2)).in_seconds())

    def test_diff_in_seconds_positive_big(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(7202, dt.diff(dt.copy().add(hours=2).add(seconds=2)).in_seconds())

    def test_diff_in_seconds_negative_with_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(-58, dt.diff(dt.copy().subtract(minutes=1).add(seconds=2), False).in_seconds())

    def test_diff_in_seconds_negative_no_sign(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(58, dt.diff(dt.copy().subtract(minutes=1).add(seconds=2)).in_seconds())

    def test_diff_in_seconds_vs_default_now(self):
        with self.wrap_with_test_now():
            self.assertEqual(3600, DateTime.now().subtract(hours=1).diff().in_seconds())

    def test_diff_in_seconds_ensure_is_truncated(self):
        dt = DateTime.create(2000, 1, 1)
        self.assertEqual(1, dt.diff(dt.copy().add(seconds=1.9)).in_seconds())

    def test_diff_in_seconds_with_timezones(self):
        dt_ottawa = DateTime(2000, 1, 1, 13, tzinfo='America/Toronto')
        dt_vancouver = DateTime(2000, 1, 1, 13, tzinfo='America/Vancouver')
        self.assertEqual(3 * 60 * 60, dt_ottawa.diff(dt_vancouver).in_seconds())

    def test_diff_for_humans_now_and_second(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 second ago', DateTime.now().diff_for_humans())

    def test_diff_for_humans_now_and_second_with_timezone(self):
        van_now = DateTime.now('America/Vancouver')
        here_now = van_now.in_timezone(DateTime.now().timezone)

        with self.wrap_with_test_now(here_now):
            self.assertEqual('1 second ago', here_now.diff_for_humans())

    def test_diff_for_humans_now_and_seconds(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 seconds ago', DateTime.now().subtract(seconds=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_minute(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 seconds ago', DateTime.now().subtract(seconds=59).diff_for_humans())

    def test_diff_for_humans_now_and_minute(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 minute ago', DateTime.now().subtract(minutes=1).diff_for_humans())

    def test_diff_for_humans_now_and_minutes(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 minutes ago', DateTime.now().subtract(minutes=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_hour(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 minutes ago', DateTime.now().subtract(minutes=59).diff_for_humans())

    def test_diff_for_humans_now_and_hour(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 hour ago', DateTime.now().subtract(hours=1).diff_for_humans())

    def test_diff_for_humans_now_and_hours(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 hours ago', DateTime.now().subtract(hours=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_day(self):
        with self.wrap_with_test_now():
            self.assertEqual('23 hours ago', DateTime.now().subtract(hours=23).diff_for_humans())

    def test_diff_for_humans_now_and_day(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 day ago', DateTime.now().subtract(days=1).diff_for_humans())

    def test_diff_for_humans_now_and_days(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 days ago', DateTime.now().subtract(days=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_week(self):
        with self.wrap_with_test_now():
            self.assertEqual('6 days ago', DateTime.now().subtract(days=6).diff_for_humans())

    def test_diff_for_humans_now_and_week(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 week ago', DateTime.now().subtract(weeks=1).diff_for_humans())

    def test_diff_for_humans_now_and_weeks(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 weeks ago', DateTime.now().subtract(weeks=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_month(self):
        with self.wrap_with_test_now():
            self.assertEqual('3 weeks ago', DateTime.now().subtract(weeks=3).diff_for_humans())

    def test_diff_for_humans_now_and_month(self):
        with self.wrap_with_test_now():
            self.assertEqual('4 weeks ago', DateTime.now().subtract(weeks=4).diff_for_humans())
            self.assertEqual('1 month ago', DateTime.now().subtract(months=1).diff_for_humans())

    def test_diff_for_humans_now_and_months(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 months ago', DateTime.now().subtract(months=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_year(self):
        with self.wrap_with_test_now():
            self.assertEqual('11 months ago', DateTime.now().subtract(months=11).diff_for_humans())

    def test_diff_for_humans_now_and_year(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 year ago', DateTime.now().subtract(years=1).diff_for_humans())

    def test_diff_for_humans_now_and_years(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 years ago', DateTime.now().subtract(years=2).diff_for_humans())

    def test_diff_for_humans_now_and_future_second(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 second from now', DateTime.now().add(seconds=1).diff_for_humans())

    def test_diff_for_humans_now_and_future_seconds(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 seconds from now', DateTime.now().add(seconds=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_future_minute(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 seconds from now', DateTime.now().add(seconds=59).diff_for_humans())

    def test_diff_for_humans_now_and_future_minute(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 minute from now', DateTime.now().add(minutes=1).diff_for_humans())

    def test_diff_for_humans_now_and_future_minutes(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 minutes from now', DateTime.now().add(minutes=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_future_hour(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 minutes from now', DateTime.now().add(minutes=59).diff_for_humans())

    def test_diff_for_humans_now_and_future_hour(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 hour from now', DateTime.now().add(hours=1).diff_for_humans())

    def test_diff_for_humans_now_and_future_hours(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 hours from now', DateTime.now().add(hours=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_future_day(self):
        with self.wrap_with_test_now():
            self.assertEqual('23 hours from now', DateTime.now().add(hours=23).diff_for_humans())

    def test_diff_for_humans_now_and_future_day(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 day from now', DateTime.now().add(days=1).diff_for_humans())

    def test_diff_for_humans_now_and_future_days(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 days from now', DateTime.now().add(days=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_future_week(self):
        with self.wrap_with_test_now():
            self.assertEqual('6 days from now', DateTime.now().add(days=6).diff_for_humans())

    def test_diff_for_humans_now_and_future_week(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 week from now', DateTime.now().add(weeks=1).diff_for_humans())

    def test_diff_for_humans_now_and_future_weeks(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 weeks from now', DateTime.now().add(weeks=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_future_month(self):
        with self.wrap_with_test_now():
            self.assertEqual('3 weeks from now', DateTime.now().add(weeks=3).diff_for_humans())

    def test_diff_for_humans_now_and_future_month(self):
        with self.wrap_with_test_now():
            self.assertEqual('4 weeks from now', DateTime.now().add(weeks=4).diff_for_humans())
            self.assertEqual('1 month from now', DateTime.now().add(months=1).diff_for_humans())

    def test_diff_for_humans_now_and_future_months(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 months from now', DateTime.now().add(months=2).diff_for_humans())

    def test_diff_for_humans_now_and_nearly_future_year(self):
        with self.wrap_with_test_now():
            self.assertEqual('11 months from now', DateTime.now().add(months=11).diff_for_humans())

    def test_diff_for_humans_now_and_future_year(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 year from now', DateTime.now().add(years=1).diff_for_humans())

    def test_diff_for_humans_now_and_future_years(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 years from now', DateTime.now().add(years=2).diff_for_humans())

    def test_diff_for_humans_other_and_second(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 second before', DateTime.now().diff_for_humans(DateTime.now().add(seconds=1)))

    def test_diff_for_humans_other_and_seconds(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 seconds before', DateTime.now().diff_for_humans(DateTime.now().add(seconds=2)))

    def test_diff_for_humans_other_and_nearly_minute(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 seconds before', DateTime.now().diff_for_humans(DateTime.now().add(seconds=59)))

    def test_diff_for_humans_other_and_minute(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 minute before', DateTime.now().diff_for_humans(DateTime.now().add(minutes=1)))

    def test_diff_for_humans_other_and_minutes(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 minutes before', DateTime.now().diff_for_humans(DateTime.now().add(minutes=2)))

    def test_diff_for_humans_other_and_nearly_hour(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 minutes before', DateTime.now().diff_for_humans(DateTime.now().add(minutes=59)))

    def test_diff_for_humans_other_and_hour(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 hour before', DateTime.now().diff_for_humans(DateTime.now().add(hours=1)))

    def test_diff_for_humans_other_and_hours(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 hours before', DateTime.now().diff_for_humans(DateTime.now().add(hours=2)))

    def test_diff_for_humans_other_and_nearly_day(self):
        with self.wrap_with_test_now():
            self.assertEqual('23 hours before', DateTime.now().diff_for_humans(DateTime.now().add(hours=23)))

    def test_diff_for_humans_other_and_day(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 day before', DateTime.now().diff_for_humans(DateTime.now().add(days=1)))

    def test_diff_for_humans_other_and_days(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 days before', DateTime.now().diff_for_humans(DateTime.now().add(days=2)))

    def test_diff_for_humans_other_and_nearly_week(self):
        with self.wrap_with_test_now():
            self.assertEqual('6 days before', DateTime.now().diff_for_humans(DateTime.now().add(days=6)))

    def test_diff_for_humans_other_and_week(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 week before', DateTime.now().diff_for_humans(DateTime.now().add(weeks=1)))

    def test_diff_for_humans_other_and_weeks(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 weeks before', DateTime.now().diff_for_humans(DateTime.now().add(weeks=2)))

    def test_diff_for_humans_other_and_nearly_month(self):
        with self.wrap_with_test_now():
            self.assertEqual('3 weeks before', DateTime.now().diff_for_humans(DateTime.now().add(weeks=3)))

    def test_diff_for_humans_other_and_month(self):
        with self.wrap_with_test_now():
            self.assertEqual('4 weeks before', DateTime.now().diff_for_humans(DateTime.now().add(weeks=4)))
            self.assertEqual('1 month before', DateTime.now().diff_for_humans(DateTime.now().add(months=1)))

    def test_diff_for_humans_other_and_months(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 months before', DateTime.now().diff_for_humans(DateTime.now().add(months=2)))

    def test_diff_for_humans_other_and_nearly_year(self):
        with self.wrap_with_test_now():
            self.assertEqual('11 months before', DateTime.now().diff_for_humans(DateTime.now().add(months=11)))

    def test_diff_for_humans_other_and_year(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 year before', DateTime.now().diff_for_humans(DateTime.now().add(years=1)))

    def test_diff_for_humans_other_and_years(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 years before', DateTime.now().diff_for_humans(DateTime.now().add(years=2)))

    def test_diff_for_humans_other_and_future_second(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 second after', DateTime.now().diff_for_humans(DateTime.now().subtract(seconds=1)))

    def test_diff_for_humans_other_and_future_seconds(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 seconds after', DateTime.now().diff_for_humans(DateTime.now().subtract(seconds=2)))

    def test_diff_for_humans_other_and_nearly_future_minute(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 seconds after', DateTime.now().diff_for_humans(DateTime.now().subtract(seconds=59)))

    def test_diff_for_humans_other_and_future_minute(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 minute after', DateTime.now().diff_for_humans(DateTime.now().subtract(minutes=1)))

    def test_diff_for_humans_other_and_future_minutes(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 minutes after', DateTime.now().diff_for_humans(DateTime.now().subtract(minutes=2)))

    def test_diff_for_humans_other_and_nearly_future_hour(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 minutes after', DateTime.now().diff_for_humans(DateTime.now().subtract(minutes=59)))

    def test_diff_for_humans_other_and_future_hour(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 hour after', DateTime.now().diff_for_humans(DateTime.now().subtract(hours=1)))

    def test_diff_for_humans_other_and_future_hours(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 hours after', DateTime.now().diff_for_humans(DateTime.now().subtract(hours=2)))

    def test_diff_for_humans_other_and_nearly_future_day(self):
        with self.wrap_with_test_now():
            self.assertEqual('23 hours after', DateTime.now().diff_for_humans(DateTime.now().subtract(hours=23)))

    def test_diff_for_humans_other_and_future_day(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 day after', DateTime.now().diff_for_humans(DateTime.now().subtract(days=1)))

    def test_diff_for_humans_other_and_future_days(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 days after', DateTime.now().diff_for_humans(DateTime.now().subtract(days=2)))

    def test_diff_for_humans_other_and_nearly_future_week(self):
        with self.wrap_with_test_now():
            self.assertEqual('6 days after', DateTime.now().diff_for_humans(DateTime.now().subtract(days=6)))

    def test_diff_for_humans_other_and_future_week(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 week after', DateTime.now().diff_for_humans(DateTime.now().subtract(weeks=1)))

    def test_diff_for_humans_other_and_future_weeks(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 weeks after', DateTime.now().diff_for_humans(DateTime.now().subtract(weeks=2)))

    def test_diff_for_humans_other_and_nearly_future_month(self):
        with self.wrap_with_test_now():
            self.assertEqual('3 weeks after', DateTime.now().diff_for_humans(DateTime.now().subtract(weeks=3)))

    def test_diff_for_humans_other_and_future_month(self):
        with self.wrap_with_test_now():
            self.assertEqual('4 weeks after', DateTime.now().diff_for_humans(DateTime.now().subtract(weeks=4)))
            self.assertEqual('1 month after', DateTime.now().diff_for_humans(DateTime.now().subtract(months=1)))

    def test_diff_for_humans_other_and_future_months(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 months after', DateTime.now().diff_for_humans(DateTime.now().subtract(months=2)))

    def test_diff_for_humans_other_and_nearly_future_year(self):
        with self.wrap_with_test_now():
            self.assertEqual('11 months after', DateTime.now().diff_for_humans(DateTime.now().subtract(months=11)))

    def test_diff_for_humans_other_and_future_year(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 year after', DateTime.now().diff_for_humans(DateTime.now().subtract(years=1)))

    def test_diff_for_humans_other_and_future_years(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 years after', DateTime.now().diff_for_humans(DateTime.now().subtract(years=2)))

    def test_diff_for_humans_absolute_seconds(self):
        with self.wrap_with_test_now():
            self.assertEqual('59 seconds', DateTime.now().diff_for_humans(DateTime.now().subtract(seconds=59), True))
            self.assertEqual('59 seconds', DateTime.now().diff_for_humans(DateTime.now().add(seconds=59), True))

    def test_diff_for_humans_absolute_minutes(self):
        with self.wrap_with_test_now():
            self.assertEqual('30 minutes', DateTime.now().diff_for_humans(DateTime.now().subtract(minutes=30), True))
            self.assertEqual('30 minutes', DateTime.now().diff_for_humans(DateTime.now().add(minutes=30), True))

    def test_diff_for_humans_absolute_hours(self):
        with self.wrap_with_test_now():
            self.assertEqual('3 hours', DateTime.now().diff_for_humans(DateTime.now().subtract(hours=3), True))
            self.assertEqual('3 hours', DateTime.now().diff_for_humans(DateTime.now().add(hours=3), True))

    def test_diff_for_humans_absolute_days(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 days', DateTime.now().diff_for_humans(DateTime.now().subtract(days=2), True))
            self.assertEqual('2 days', DateTime.now().diff_for_humans(DateTime.now().add(days=2), True))

    def test_diff_for_humans_absolute_weeks(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 weeks', DateTime.now().diff_for_humans(DateTime.now().subtract(weeks=2), True))
            self.assertEqual('2 weeks', DateTime.now().diff_for_humans(DateTime.now().add(weeks=2), True))

    def test_diff_for_humans_absolute_months(self):
        with self.wrap_with_test_now():
            self.assertEqual('2 months', DateTime.now().diff_for_humans(DateTime.now().subtract(months=2), True))
            self.assertEqual('2 months', DateTime.now().diff_for_humans(DateTime.now().add(months=2), True))

    def test_diff_for_humans_absolute_years(self):
        with self.wrap_with_test_now():
            self.assertEqual('1 year', DateTime.now().diff_for_humans(DateTime.now().subtract(years=1), True))
            self.assertEqual('1 year', DateTime.now().diff_for_humans(DateTime.now().add(years=1), True))

    def test_diff_for_humans_accuracy(self):
        now = DateTime.now('utc')

        with self.wrap_with_test_now(now.add(microseconds=200)):
            self.assertEqual('1 year', now.add(years=1).diff_for_humans(absolute=True))
            self.assertEqual('11 months', now.add(months=11).diff_for_humans(absolute=True))
            self.assertEqual('4 weeks', now.add(days=27).diff_for_humans(absolute=True))
            self.assertEqual('1 year', now.add(years=1, months=3).diff_for_humans(absolute=True))
            self.assertEqual('2 years', now.add(years=1, months=8).diff_for_humans(absolute=True))

        # DST
        now = DateTime.create(2017, 3, 7, tz='America/Toronto')
        with self.wrap_with_test_now(now):
            self.assertEqual('6 days', now.add(days=6).diff_for_humans(absolute=True))

    def test_seconds_since_midnight(self):
        d = DateTime.create(2016, 7, 5, 12, 32, 25, 0)
        self.assertEqual(25 + 32 * 60 + 12 * 3600, d.seconds_since_midnight())

    def test_seconds_until_end_of_day(self):
        d = DateTime.create(2016, 7, 5, 12, 32, 25, 0)
        self.assertEqual(34 + 27 * 60 + 11 * 3600, d.seconds_until_end_of_day())

    def test_subtraction(self):
        d = DateTime.create(2016, 7, 5, 12, 32, 25, 0)
        future_dt = datetime(2016, 7, 5, 13, 32, 25, 0)
        future = d.add(hours=1)

        self.assertEqual(3600, (future - d).total_seconds())
        self.assertEqual(3600, (future_dt - d).total_seconds())
