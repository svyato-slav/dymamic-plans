# coding=utf-8
from dymamic_plans.generators.content import PremiumContentGenerator, MaintenanceContentGenerator
from dymamic_plans.generators.plan import PremiumPlanGenerator, MaintenancePlanGenerator


class Generation:

    def __init__(self, user):
        self.user = user

    def run(self):
        '''
        Есть цель неделю и на этап.
        Если цели достигнута, то изменяются соответствующим образом:
        weight_class, gender, plan_type, week_number. Поэтому при генерации
        всегда правильные параметры передаются.
        '''
        print("Generation begins")
        self.user.week_goal.check_goal_achieved(self.user.checkin)
        self.user.current_goal.check_goal_achieved(self.user)
        weight_class, gender, plan_type, week_number = self.get_template_meal_plan_args()
        template_meal_plan = self.get_template_meal_plan(weight_class, gender, plan_type, week_number)
        self.generate(template_meal_plan, week_number)
        if template_meal_plan and week_number == template_meal_plan.start_week_number:
            self.generate(template_meal_plan, week_number+1)
        print("Generation ends")

    def generate(self, template_meal_plan, week_number):
        '''
        Тут собственно будет все генерироваться.
        '''
        plan_generator = self.get_plan_generator()
        plan_generator.generate()
        content_generator = self.get_content_generator()
        content_generator.generate()

    def get_template_meal_plan(self, weight_class, gender, plan_type, week_number):
        '''
        Шаблонный план в зависимости от покупок юзера.
        '''
        if self.user.has_active_module():
            print("User has active module")
            return
            # TODO: return get_module_meal_plan(weight_class, gender, plan_type, week_number)
        # TODO: return get_template_meal_plan(weight_class, gender, plan_type, week_number)
        print("User has common meal plan")

    def get_template_meal_plan_args(self):
        '''
        Получить данные юзера нужные для генерации данных
        '''
        return self.user.weight_class, self.user.gender, self.user.plan_type, self.user.checkin.week_number

    def get_plan_generator(self):
        '''
        Получить генератор мил-плана, смотря какой статус подписки юзера
        '''
        if self.user.has_active_subscription():
              return PremiumPlanGenerator()
        return MaintenancePlanGenerator()

    def get_content_generator(self):
        '''
        Получить генератор контента, смотря какой статус подписки юзера
        '''
        if self.user.has_active_subscription():
              return PremiumContentGenerator()
        return MaintenanceContentGenerator()
