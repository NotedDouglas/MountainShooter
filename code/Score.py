import sys
from datetime import datetime
from tkinter.ttk import Label

import pygame
from pygame.constants import K_RETURN, KEYDOWN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import COLOR_YELLOW, SCORE_POS, MENU_OPTION, COLOR_WHITE
from code.DB_Proxy import DBProxy


class Score:
    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)
        pass

    def save_score(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')  # Abre conexão com o banco
        name = ''
        self.window.blit(source=self.surf, dest=self.rect)

        while True:
            self.score_text(48, 'YOU WIN', COLOR_YELLOW, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Enter Player 1 enter name (4 Characters):'
            elif game_mode == MENU_OPTION[1]:
                score = player_score[0] + player_score[1] / 2
                text = 'Enter Team name (4 Characters):'
            elif game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name (4 Characters):'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 Characters):'

            self.score_text(20, text, COLOR_WHITE, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        # Salva no banco e fecha conexão
                        db_proxy.save({'name': name, 'score': int(score), 'date': get_formatted_date()})
                        db_proxy.close()
                        # Mostra a tela de score atualizada
                        self.show_score()
                        return  # Sai do loop após salvar e mostrar o score
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4 and event.unicode.isprintable():
                            name += event.unicode

            self.score_text(20, name, COLOR_WHITE, SCORE_POS['Name'])
            pygame.display.flip()

    def show_score(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', COLOR_YELLOW, SCORE_POS['Title'])
        self.score_text(20, 'NAME      SCORE            DATE', COLOR_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')

        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20, f'{name}    {score :05d}    {date}', COLOR_YELLOW,
                            SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.flip()

    def score_text(self, texte_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=texte_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
