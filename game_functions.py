import sys 
import pygame 
from bullet import Bullet
from alien import Alien
from time import sleep
#Get numbers of ...
def get_num_alinz(ai_sett, alinz_width):
    av_space_x = ai_sett.screen_width - 2 * alinz_width
    number_alinz_x = int(av_space_x / (2 * alinz_width))
    return number_alinz_x
def get_num_rows(ai_sett, rocket_height, alinz_height):
    av_space_y = (ai_sett.screen_height - (3 * alinz_height) - rocket_height)
    numbers_rows = int(av_space_y / (2 * alinz_height))
    return numbers_rows
#Checks
def check_record(stats, sb):
    if stats.score > stats.record:
        stats.record = stats.score
        sb.prep_record()
def check_keydown_events(event, ai_sett, screen, rocket, bullets):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_sett, screen, rocket, bullets)
    elif event.key == pygame.K_q:
        sys.exit()
def check_keyup_events(event, rocket):
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
def check_play_button( ai_sett, screen, stats, sb, play_button, rocket, alinzes, bullets, mouse_x, mouse_y):
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
        if button_clicked and not stats.game_active:
            ai_sett.initialize_dynamic_sett()
            pygame.mouse.set_visible(False)
            stats.reset_stats()
            stats.game_active = True
            sb.prep_score()
            sb.prep_record()
            sb.prep_level()
            sb.prep_rocket()
            alinzes.empty()
            bullets.empty()
            create_fleet(ai_sett, screen, rocket, alinzes)
            rocket.center_rocket()
def check_events(ai_sett, screen, stats, sb, play_button, rocket, alinzes, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_sett, screen, stats, sb, play_button, rocket, alinzes, bullets, mouse_x, mouse_y)            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_sett, screen, rocket, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rocket) 
           
def check_fleet_edges(ai_sett, alinzes):
    for alinz in alinzes.sprites():
        if alinz.check_edges():
            change_fleet_direction(ai_sett, alinzes)
            break
def check_bullet_alinz_collisions(ai_sett, screen, stats, sb, rocket, alinzes, bullets):
    collisions = pygame.sprite.groupcollide(alinzes, bullets, True, True)
    if collisions:
        for alinzes in collisions.values():
            stats.score += ai_sett.alinz_point * len(alinzes)
            sb.prep_score()
            check_record(stats, sb)
    if len(alinzes) == 0:
        bullets.empty()
        
        ai_sett.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_sett, screen, rocket, alinzes)
def check_alinzes_bottom(ai_sett, stats, sb, screen, rocket, alinzes, bullets):
    screen_rect = screen.get_rect()
    for alinz in alinzes.sprites():
        if alinz.rect.bottom >= screen_rect.bottom:
            rocket_hit(ai_sett, stats, sb, screen, rocket, alinzes, bullets)
            break
    
        
#Create something
def create_fleet(ai_sett, screen, rocket, alinzes):
    alinz = Alien(ai_sett, screen)
    number_alinz_x = get_num_alinz(ai_sett, alinz.rect.width)
    number_rows = get_num_rows(ai_sett, rocket.rect.height, alinz.rect.height)
    for row_number in range(number_rows):
        for alinz_num in range(number_alinz_x):
            create_alinz(ai_sett, screen, alinzes, alinz_num, row_number)
def create_alinz(ai_sett, screen, alinzes, alinz_num, row_number):
    alinz = Alien(ai_sett, screen)
    alinz_width = alinz.rect.width
    alinz.x = alinz_width + 2 * alinz_width * alinz_num
    alinz.rect.x = alinz.x
    alinz.rect.y = alinz.rect.height + 2 * alinz.rect.height * row_number
    alinzes.add(alinz)

#Change directions
def change_fleet_direction(ai_sett, alinzes):
    for alinz in alinzes.sprites():
        alinz.rect.y += ai_sett.fleet_drop_speed
    ai_sett.fleet_direction *= -1
#Fire
def fire_bullet(ai_sett, screen, rocket, bullets):
    if len(bullets) < ai_sett.bullets_allowed:
            new_bullet = Bullet(ai_sett, screen, rocket)
            bullets.add(new_bullet)
#Ship hits
def rocket_hit(ai_sett, stats, sb, screen, rocket, alinzes, bullets):
    if stats.rocket_crush > 0:
        stats.rocket_crush -= 1
        sb.prep_rocket()
        alinzes.empty()
        bullets.empty()
        create_fleet(ai_sett, screen, rocket, alinzes)
        rocket.center_rocket()
        sleep(1)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
#Anlizes (aliens)
def update_alinz(ai_sett, stats, sb, screen, rocket, alinzes, bullets):
    check_fleet_edges(ai_sett, alinzes)
    alinzes.update()
    if pygame.sprite.spritecollideany(rocket, alinzes):
        rocket_hit(ai_sett, stats, sb, screen, rocket, alinzes, bullets)
    check_alinzes_bottom(ai_sett, stats, sb, screen, rocket, alinzes, bullets)
#Bullets
def update_bullets(ai_sett, screen, stats, sb, rocket, alinzes, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alinz_collisions(ai_sett, screen, stats, sb, rocket, alinzes, bullets)
    if len(alinzes) == 0:
        bullets.empty()
        create_fleet(ai_sett, screen, rocket, alinzes)
#Screen
def update_s(ai_sett, screen, stats, sb, rocket, alinzes, bullets, play_button):
    screen.fill(ai_sett.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    rocket.blitme()
    alinzes.draw(screen)
    sb.show_score()
    pygame.display.flip()


    