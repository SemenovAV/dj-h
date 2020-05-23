from random import randint

from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import GameForm
from .models import Game, PlayerGameInfo, Player


def new_number():
    return randint(0, 100)


# query from session


def get_data_from_the_session(request):
    return request.session.get('game')


def set_data_to_the_session(request, data):
    request.session['game'] = data


def remove_data_to_session(request):
    return request.session.pop('game')


# query from db


def is_author(game, player):
    return game.author == player


def get_player(*args):
    if args:
        player = Player.objects.get(id=args[0])
    else:
        player = Player.objects.create()
    player.save()
    return player


def get_active_game():
    active_game = Game.objects.filter(is_active=True)
    if active_game:
        return active_game[0]


def get_game(game_id):
    game = Game.objects.get(id=game_id)
    return game


def start_game(number, author):
    game = Game.objects.create(number=number, author=author)
    game.save()
    return game


def stop_game(game):
    game.is_active = False
    game.save()
    return game


def set_game_info(game, player, attempt, is_true):
    info = PlayerGameInfo(player=player, game=game, attempt=attempt, is_true=is_true)
    info.save()
    return info

def get_all_stat_game(game):
    return PlayerGameInfo.objects.filter(game=game).select_related('game')


class ShowHome(FormView):
    template_name = 'home.html'
    form_class = GameForm
    success_url = '/'
    is_new_game = None
    is_new_player = None
    is_author = None
    is_new_attempts = None
    game = None
    player = None
    number = None
    game_state = None

    def dispatch(self, request, *args, **kwargs):
        self.game = get_active_game()
        session_data = get_data_from_the_session(request)
        self.is_new_game = not session_data and not self.game
        self.is_new_player = not session_data and self.game and self.game.is_active
        if self.is_new_game:
            self.number = new_number()
            self.player = get_player()
            if self.number and self.player:
                self.game = start_game(number=self.number, author=self.player)
                set_data_to_the_session(request, {
                    'player_id': self.player.id,
                    'game_id': self.game.id
                })
                self.is_author = True

        elif self.is_new_player:
            self.player = get_player()
            if self.game and self.player:
                set_data_to_the_session(request, {
                    'player_id': self.player.id,
                    'game_id': self.game.id
                })
        else:
            player_id = session_data['player_id']
            game_id = session_data['game_id']
            if player_id and game_id:
                self.player = get_player(player_id)
                self.game = get_game(game_id)
                self.is_author = is_author(self.game, self.player)
        if not self.game.is_active:
            remove_data_to_session(request)
        self.game_state = get_all_stat_game(self.game).values()
        return super(ShowHome, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        number = form.cleaned_data['number']
        context = self.get_context_data()
        if self.game.number == number:
            stop_game(self.game)
            set_game_info(game=self.game, player=self.player, attempt=number, is_true=True)
            context['win'] = True
        else:
            if self.game.number < number:
                context['more'] = True
            elif self.game.number > number:
                context['less'] = True
            set_game_info(game=self.game, player=self.player, attempt=number, is_true=False)
            context['is_new_attempts'] = True
            context['form'] = self.form_class

        return render(request=self.request, template_name=self.template_name, context=context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(kwargs)
        context['is_new_game'] = self.is_new_game
        context['is_new_player'] = self.is_new_player
        context['is_author'] = self.is_author
        context['number'] = self.number
        context['is_new_attempts'] = self.is_new_attempts
        context['game'] = self.game
        context['game_state'] = self.game_state
        return context
