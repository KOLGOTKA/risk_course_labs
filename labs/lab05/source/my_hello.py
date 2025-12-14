"""
Модуль для приветствия пользователя
"""
import random
from typing import Optional
import typer
import pygame


app = typer.Typer(help="Утилита для приветствия пользователя.")


COLORS = [
    "\033[31m",
    "\033[32m",
    "\033[33m",
    "\033[34m",
    "\033[35m",
    "\033[36m",
    "\033[91m",
    "\033[92m",
    "\033[93m",
    "\033[94m",
    "\033[95m",
    "\033[96m",
]

RESET = "\033[0m"


def rainbow_print(text: str):
    """Выводит строку, в которой каждая буква случайного цвета"""
    out = []
    for ch in text:
        color = random.choice(COLORS)
        out.append(f"{color}{ch}{RESET}")
    print("".join(out))


def show_pygame_window(text: str = "Hello appsec world*"):
    """
    Открывает окно pygame и выводит в нём текст.
    Используется только для стилизации окна (по заданию).
    """
    if pygame is None:
        typer.echo("pygame не установлен. Установите его: pip install pygame")
        raise typer.Exit(code=1)

    pygame.display.init()
    pygame.font.init()

    screen_width = 800
    screen_height = 600
    window_size = (screen_width, screen_height)

    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("AppSec greeting")

    bg_color = (255, 255, 255)

    font = pygame.font.SysFont(None, 75)
    text_surface = font.render(text, True, (0, 200, 0))
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        screen.fill(bg_color)
        screen.blit(text_surface, text_rect)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


@app.command()
def hello_printer(
    name: str = typer.Argument(..., help="Имя пользователя."),
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Формальное приветствие."),
    antiformal: bool = typer.Option(False, "--antiformal", "-af", help="Неформальное приветствие."),
    window: bool = typer.Option(
        False,
        "--window",
        "-w",
        help="Открыть графическое окно с надписью 'Hello appsec world*' (pygame).",
    ),
):
    """
    Здоровается с пользователем, используя повседневный, формальный или неформальный стиль.
    При необходимости открывает окно pygame.
    """
    if formal:
        greeting = f"Добрый день, {name} {lastname}!"
    elif antiformal:
        greeting = f"Здаров, {name}!"
    else:
        greeting = f"Привет, {name}!"

    rainbow_print(greeting)

    if window:
        show_pygame_window("Hello appsec world*")


if __name__ == "__main__":
    app()
