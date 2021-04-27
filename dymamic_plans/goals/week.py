# coding=utf-8
from .base import BaseGoal


class WeekGoal(BaseGoal):

    def check_goal_achieved(self, checkin):
        print("Check WeekGoal conditions")
        if checkin.is_success():
            print("Checkin success")
            print(f"Checkin current week_number {checkin.week_number}")
            checkin.make_new_week_number()
            print(f"Checkin new week_number {checkin.week_number}")
