import pygame


def music_pause(is_paused: bool) -> bool:
    if not is_paused:
        pygame.mixer.music.pause()
        return True
    pygame.mixer.music.unpause()
    return False


def music_set_volume_down(volume: float) -> float:
    return music_set_volume(volume - 0.2)


def music_set_volume_up(volume: float) -> float:
    return music_set_volume(volume + 0.2)


def music_set_volume(volume: float) -> float:
    if volume < 0.0:
        pygame.mixer.music.set_volume(0.0)
        return 0.0
    elif volume > 1.0:
        pygame.mixer.music.set_volume(1.0)
        return 1.0
    else:
        pygame.mixer.music.set_volume(volume)
        return volume


def get_music_state() -> bool:
    return pygame.mixer.music.get_busy()


def get_music_volume() -> float:
    return pygame.mixer.music.get_volume()


def music_player() -> None:
    pygame.mixer.init()
    pygame.mixer.music.load("assets/06. Unknown Planet.mp3")
    pygame.mixer.music.play(loops=-1)
