# coding=utf-8
from .base import BaseGoal
from .user import UserGoal


class KickOffGoal(BaseGoal):
    next_goal = UserGoal()

    def check_goal_achieved(self):
        '''
        Проверяем выполнена ли цель в зависимости от условий.
        Если да, то меняем нужные настройки юзера.
        '''
        if self.some_conditions():
            self.make_new_template_meal_plan_args()
