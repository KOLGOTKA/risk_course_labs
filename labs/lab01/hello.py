
"""
Модуль для приветствия пользователя
"""
import typer
import random


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


def hello_printer(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Формальное приветствие."),
    antiformal: bool = typer.Option(False, "--antiformal", "-af", help="Неформальное приветствие."),
):
    """
    Здоровается с пользоваетелем, используя повседневный, формальный или неформальный стиль.
    """
    # Формальный стиль
    if formal:
        rainbow_print(f"Добрый день, {name} {lastname}!")
    # Максимально неформальный стиль
    elif antiformal:
        rainbow_print(f"Здаров, {name}!")
    # Повседневный стиль
    else:
        rainbow_print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(hello_printer)
