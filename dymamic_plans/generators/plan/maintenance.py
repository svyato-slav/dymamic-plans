# coding=utf-8
from .base import BasePlanGenerator


class MaintenancePlanGenerator(BasePlanGenerator):
    def generate(self):
        '''
        Создание всего, что нужно в бесплатном милпане
        '''
        generate_categories_and_exchanges(user, template_meal_plan, week_number)
        generate_meal_items(user, template_meal_plan, week_number)

