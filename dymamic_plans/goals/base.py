# coding=utf-8

class BaseGoal:
    next_goal = None

    def check_goal_achieved(self, *args, **kwargs):
        raise

    def set_next_goal(self, user):
        print(f'New goal set to user: {self.next_goal.__class__.__name__}')
        user.current_goal = self.next_goal
