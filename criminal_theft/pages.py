from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1


class Quiz(Page):

    def is_displayed(self):
        return self.subsession.round_number == 1

    form_model = 'player'
    form_fields = ['quiz1', 'quiz2']

    def quiz1_error_message(self, value):
        if value != 2:
            return 'Question 1 is incorrect. Please try again.'

    def quiz2_error_message(self, value):
        if value != 2:
            return 'Question 2 is incorrect. Please try again.'


class Decisions(Page):

    form_model = 'group'
    form_fields = ['ThiefChoice']

    def ThiefChoice_choices(self):
        choices = [
            [1, 'Report Truthfully'],
            [2, 'Take ${0:.2f} of your counterpart\'s money.'.format(self.participant.vars['xdraws'][self.subsession.round_number - 1])],
            [3, 'Take ${0:.2f} of your counterpart\'s money.'.format(self.participant.vars['ydraws'][self.subsession.round_number - 1])],
            [4, 'Take ${0:.2f} of your counterpart\'s money.'.format(self.participant.vars['zdraws'][self.subsession.round_number - 1])],
        ]
        return choices

    def vars_for_template(self):
        return {'W': format(self.participant.vars['Wdraws'][self.subsession.round_number - 1], '.2f'),
                '10W': format(10 - self.participant.vars['Wdraws'][self.subsession.round_number - 1], '.2f'),
                'x': format(self.participant.vars['xdraws'][self.subsession.round_number - 1], '.2f'),
                'y': format(self.participant.vars['ydraws'][self.subsession.round_number - 1], '.2f'),
                'z': format(self.participant.vars['zdraws'][self.subsession.round_number - 1], '.2f')}


page_sequence = [
    Instructions,
    Quiz,
    Decisions
]
