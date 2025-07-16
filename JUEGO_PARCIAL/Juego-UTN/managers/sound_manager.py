import pygame

_music_playing = False
_music_paused = False
_music_volume = 0.25

def play_music(music_path, loops=-1, volume=_music_volume):
    """Carga y reproduce música de fondo."""
    global _music_playing, _music_paused
    if _music_playing:
        return  # Si ya está sonando, no hacer nada
    pygame.mixer.music.load(music_path)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loops)
    _music_playing = True
    _music_paused = False

def stop_music():
    """Detiene la música y resetea el estado."""
    global _music_playing, _music_paused
    pygame.mixer.music.stop()
    _music_playing = False
    _music_paused = False

def pause_music():
    """Pausa la música."""
    global _music_paused
    if not _music_paused:
        pygame.mixer.music.pause()
        _music_paused = True

def unpause_music():
    """Reanuda la música si estaba pausada."""
    global _music_paused
    if _music_paused:
        pygame.mixer.music.unpause()
        _music_paused = False

def is_music_playing():
    """Devuelve True si la música está sonando y no pausada."""
    return _music_playing and not _music_paused
