import pygame


def music_pause(is_paused: bool) -> bool:
    """
    Toggle the background music between paused and playing.

    If the music is currently playing, it is paused. Otherwise, playback is
    resumed.

    Args:
        is_paused: Indicates whether the music is currently paused.

    Returns:
        The updated pause state of the music.
    """
    if not is_paused:
        pygame.mixer.music.pause()
        return True
    pygame.mixer.music.unpause()
    return False


def music_set_volume_down(volume: float) -> float:
    """
    Decrease the music volume.

    The function reduces the current volume by 0.2 and applies the new value
    through ``music_set_volume()``, ensuring the resulting volume remains
    within the valid range.

    Args:
        volume: The current music volume.

    Returns:
        The updated music volume.
    """
    return music_set_volume(volume - 0.2)


def music_set_volume_up(volume: float) -> float:
    """
    Increase the music volume.

    The function increases the current volume by 0.2 and applies the new value
    through ``music_set_volume()``, ensuring the resulting volume remains
    within the valid range.

    Args:
        volume: The current music volume.

    Returns:
        The updated music volume.
    """
    return music_set_volume(volume + 0.2)


def music_set_volume(volume: float) -> float:
    """
    Set the music volume.

    The function applies the specified volume while clamping its value to the
    valid range between 0.0 and 1.0.

    Args:
        volume: The desired music volume.

    Returns:
        The applied music volume after clamping.
    """
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
    """
    Get the current playback state of the background music.

    The function checks whether the music mixer is currently playing audio.

    Returns:
        ``True`` if music is currently playing, otherwise ``False``.
    """
    return pygame.mixer.music.get_busy()


def get_music_volume() -> float:
    """
    Get the current music volume.

    The function retrieves the current playback volume from the music mixer.

    Returns:
        The current music volume, ranging from 0.0 (muted) to 1.0 (maximum).
    """
    return pygame.mixer.music.get_volume()


def music_player() -> None:
    """
    Initialize and start the background music.

    The function initializes the pygame mixer, loads the music file, and
    starts playback in an infinite loop.

    Returns:
        None
    """
    pygame.mixer.init()
    pygame.mixer.music.load("assets/06. Unknown Planet.mp3")
    pygame.mixer.music.play(loops=-1)
