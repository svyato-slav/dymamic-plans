# coding=utf-8
from .base import BaseGoal


class MaintainGoal(BaseGoal):

    def check_goal_achieved(self):
        if self.some_conditions():
            self.make_new_template_meal_plan_args()
