import pygame
import sys
from bullet import Bullet
from alien import Alien
from time import sleep
def check_events(ai_settings,screen,stats,scoreboard,play_button,ship,aliens,bullets):
    """Check for game events"""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=pygame.mouse.get_pos()
            check_play_button(ai_settings,screen,stats,scoreboard,play_button,ship,aliens,bullets,mouse_x,mouse_y)
        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event,ai_settings,screen,ship,bullets)
        elif event.type==pygame.KEYUP:
            check_keyup_events(event,ship)
def check_play_button(ai_settings,screen,stats,scoreboard,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active=True
        stats.reset_stats()
        aliens.empty()
        bullets.empty()
        scoreboard.prep_ships()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship
def ship_hit(ai_settings,stats,scoreboard,screen,ship,aliens,bullets):
    if stats.ships_left>0:
        stats.ships_left-=1
        scoreboard.prep_ships()
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)
        ship.center_ship
        ai_settings.initialize_dynamic_settings()
        sleep(0.5)
    else:
        stats.game_active=False
def update_aliens(ai_settings,stats,screen,scoreboard,aliens,ship,bullets):
    check_edges_fleet(ai_settings,aliens)
    aliens.update()
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings,stats,scoreboard,screen,ship,aliens,bullets)
    check_alliens_bottom(ai_settings,stats,screen,scoreboard,aliens,ship,bullets)
def check_alliens_bottom(ai_settings,stats,screen,scoreboard,aliens,ship,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom>=screen_rect.bottom:
            ship_hit(ai_settings,stats,scoreboard,screen,ship,aliens,bullets)
def check_edges_fleet(ai_settings,aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            break
def change_fleet_direction(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y+=ai_settings.fleet_drop_speed
    ai_settings.fleet_direction*=-1
def get_number_aliens(ai_settings,alien_width):
    available_space=ai_settings.screen_width - 2 * alien_width
    number_aliens=int(available_space/(2*alien_width))
    return number_aliens
def get_rows_number(ai_settings,alien_height,ship_height):
    available_space=(ai_settings.screen_height-(3*alien_height)-ship_height)
    number_rows=int(available_space/(2*alien_height))
    return number_rows
def create_alien(ai_settings,screen,aliens,alien_number,number_rows):
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x=alien_width+2*alien_width*alien_number
    alien.rect.x=alien.x
    alien.rect.y=alien.rect.height+2*alien.rect.height*number_rows
    aliens.add(alien)
def create_fleet(ai_settings,screen,ship,aliens):
    alien=Alien(ai_settings,screen)
    number_aliens=get_number_aliens(ai_settings,alien.rect.width)
    number_rows=get_rows_number(ai_settings,alien.rect.height,ship.rect.height)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)
def update_screen(ai_settings,screen,stats,scoreboard,ship,aliens,bullets,play_button):
    screen.fill(ai_settings.bg_color)
    ship.bltime()
    scoreboard.show_score()    
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    aliens.draw(screen)
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()
def check_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=False
    if event.key==pygame.K_LEFT:
        ship.moving_left=False
    elif event.key==pygame.K_q:
        sys.exit()
def check_keydown_events(event,ai_settings,screen,ship,bullets):
    if event.key==pygame.K_RIGHT:
        ship.moving_right=True
    if event.key==pygame.K_LEFT:
        ship.moving_left=True
    if event.key==pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
def update_bullets(ai_settings,screen,stats,scoreboard,ship,aliens,bullets):
    for bullet in bullets.copy():
        if bullet.rect.bottom<=0:
            bullets.remove(bullet)
    check_alliens_bullet_collisions(ai_settings,screen,stats,scoreboard,ship,aliens,bullets)
def check_alliens_bullet_collisions(ai_settings,screen,stats,scoreboard,ship,aliens,bullets):
    collisions=pygame.sprite.groupcollide(aliens,bullets,True,True)
    if collisions:
        stats.score+=ai_settings.alien_points
        scoreboard.prep_score()
    if len(aliens)==0:
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings,screen,ship,aliens)
def fire_bullets(ai_settings,screen,ship,bullets):
    if len(bullets)<ai_settings.bullets_allowed:
        new_bullet=Bullet(ai_settings,ship,screen)
        bullets.add(new_bullet)