from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import urllib
import json

class MyPage(Page):
    form_model = 'player'
    form_fields = ['answer']

    def before_next_page(self):
        self.player.answer = urllib.parse.unquote(self.player.answer)


class Results(Page):
    def vars_for_template(self) -> dict:
        return dict(answer=json.loads(self.player.answer))


page_sequence = [MyPage, Results]
