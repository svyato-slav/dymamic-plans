from dymamic_plans.generation import Generation
from dymamic_plans.goals import WeekGoal, UserGoal


class Checkin:
    week_number = 3

    def is_success(self):
        return True

    def make_new_week_number(self):
        self.week_number += 1


class User:
    checkin = Checkin()
    current_goal = UserGoal()
    gender = 'male'
    week_goal = WeekGoal()
    weight_class = '200-250'
    plan_type = 'premium'

    def has_active_module(self):
        return False

    def has_active_subscription(self):
        return True


user = User()
Generation(user).run()

# Output:
'''
Generation begins
Check WeekGoal conditions
Checkin success
Checkin current week_number 3
Checkin new week_number 4
Check UserGoal conditions
UserGoal achieved
New goal set to user: MaintainGoal
New template plan have set
User has common meal plan
Generate premium meal plan for week
Generate premium content for week
Generation ends
'''
