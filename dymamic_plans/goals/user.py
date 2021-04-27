# coding=utf-8
from .base import BaseGoal
from .maintain import MaintainGoal


class UserGoal(BaseGoal):
    next_goal = MaintainGoal()

    def check_goal_achieved(self, user):
        if self.some_conditions():
            self.set_next_goal(user)
            self.make_new_template_meal_plan_args(user)

    def make_new_template_meal_plan_args(self, user):
        print('New template plan have set')

    def some_conditions(self):
        print("Check UserGoal conditions")
        print("UserGoal achieved")
        return True
