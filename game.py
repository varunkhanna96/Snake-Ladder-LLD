from typing import List

from board import Board
from dice import Dice, SixSideDice
from entity import Snake, Ladder
from player import GamePlayer


class Game:

    def __init__(self, board: Board, players: List[GamePlayer], dice: Dice):
        self.board = board
        self.active_players = players
        self.dice = dice
        # game ends at only one player winning
        self.no_of_winners_game_ends_at = 3
        self.winner = None
        self.completed_players = []
        self.turn = 0

    def _can_play(self) -> bool:
        return self.no_of_winners_game_ends_at > len(self.completed_players)

    def _get_next_player(self) -> GamePlayer:
        return self.active_players[self.turn % len(self.active_players)]

    def _change_turn(self, dice_result: int) -> None:
        if dice_result != 6:
            self.turn += 1

    def _move_player(self, position: int, player: GamePlayer) -> None:
        player.position = position
        if not self.board.reached_end(position=position):
            return
        player.rank = len(self.completed_players) + 1
        self.completed_players.append(player)
        self.active_players.pop(self.turn % len(self.active_players))

    def play(self) -> None:
        while self._can_play():
            curr_player = self._get_next_player()
            dice_result = self.dice.roll()
            if curr_player.rank == -1 and self.board.can_move(position=curr_player.position + dice_result):
                next_pos = self.board.get_next_pos(position=curr_player.position + dice_result)
                self._move_player(position=next_pos, player=curr_player)
            self._change_turn(dice_result=dice_result)
        self.print_game_result()

    def print_game_result(self):
        # Print final game result with ranks of each player
        print('-------------final result-------------')
        for _p in sorted(self.active_players + self.completed_players, key=lambda x: x.rank):
            print(f'Player: {_p._id + 1} , Rank: {_p.rank}')


def sample_run():
    board = Board(10)
    board.entity_pos[7] = Snake(2)
    board.entity_pos[4] = Ladder(6)
    players = [GamePlayer(1), GamePlayer(2), GamePlayer(3)]
    game = Game(board=board, players=players, dice=SixSideDice())
    game.play()


sample_run()
