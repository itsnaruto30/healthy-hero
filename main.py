@namespace
class SpriteKind:
    Cokeenemy = SpriteKind.create()
    Burgerenemy = SpriteKind.create()
    HealthPickup = SpriteKind.create()
    Veggies = SpriteKind.create()
    Button = SpriteKind.create()
    cursor = SpriteKind.create()
    milk = SpriteKind.create()
    Carrot = SpriteKind.create()
    Tomato = SpriteKind.create()
    Potato = SpriteKind.create()
    Exercise = SpriteKind.create()
    Donut = SpriteKind.create()
    Oilyfood = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    global Level
    if otherSprite == Play and controller.A.is_pressed():
        Level = 1
        Levelcontrol()
        sprites.destroy(Cursor)
        sprites.destroy(Play)
        effects.star_field.start_screen_effect()
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
sprites.on_overlap(SpriteKind.cursor, SpriteKind.Button, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    info.change_score_by(4)
    sprites.destroy(Tomato2)
    Player_Hero.start_effect(effects.hearts, 500)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Tomato, on_on_overlap2)

def on_on_overlap3(sprite3, otherSprite3):
    info.change_score_by(3)
    sprites.destroy(Veggies2)
    Player_Hero.start_effect(effects.hearts, 500)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Veggies, on_on_overlap3)

def on_on_overlap4(sprite4, otherSprite4):
    info.change_life_by(-1)
    sprites.destroy(Coke_Enemy, effects.spray, 500)
    Player_Hero.start_effect(effects.fire, 500)
    scene.camera_shake(8, 500)
    music.play(music.melody_playable(music.power_down),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Cokeenemy, on_on_overlap4)

def on_a_pressed():
    global Bullet
    music.play(music.melody_playable(music.pew_pew),
        music.PlaybackMode.UNTIL_DONE)
    Bullet = sprites.create_projectile_from_sprite(img("""
            ......................
                    ......................
                    ......................
                    ......................
                    ......................
                    ......................
                    ......................
                    ......................
                    ......................
                    ......................
                    ......................
                    ......................
                    ......55......55......
                    ......22......22......
                    ......82......28......
                    ......98......89......
                    ......99......99......
                    ......88......88......
                    ......99......99......
                    ......28......82......
                    ......22......22......
                    ......82......28......
        """),
        Player_Hero,
        0,
        -100)
    Bullet.set_kind(SpriteKind.projectile)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap5(sprite5, otherSprite5):
    info.change_score_by(7)
    sprites.destroy(Exercise_1)
    Player_Hero.start_effect(effects.hearts, 500)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Exercise, on_on_overlap5)

def on_on_overlap6(sprite6, otherSprite6):
    sprites.destroy(Donut2, effects.spray, 500)
    sprites.destroy(Bullet)
    info.change_score_by(2)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.Donut, SpriteKind.projectile, on_on_overlap6)

def on_on_overlap7(sprite7, otherSprite7):
    info.change_life_by(1)
    sprites.destroy(ExtraHealth)
    Player_Hero.start_effect(effects.hearts, 500)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.HealthPickup, on_on_overlap7)

def on_on_overlap8(sprite8, otherSprite8):
    info.change_score_by(5)
    sprites.destroy(milk2)
    Player_Hero.start_effect(effects.hearts, 500)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.milk, on_on_overlap8)

def on_on_overlap9(sprite9, otherSprite9):
    info.change_score_by(6)
    sprites.destroy(Potato2)
    Player_Hero.start_effect(effects.hearts, 500)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Potato, on_on_overlap9)

def on_on_overlap10(sprite10, otherSprite10):
    sprites.destroy(Coke_Enemy, effects.spray, 500)
    sprites.destroy(Bullet)
    info.change_score_by(2)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.Cokeenemy, SpriteKind.projectile, on_on_overlap10)

def on_on_overlap11(sprite11, otherSprite11):
    info.change_life_by(-1)
    sprites.destroy(Burger_enemy)
    Player_Hero.start_effect(effects.fire, 500)
    scene.camera_shake(8, 500)
    music.play(music.melody_playable(music.power_down),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Burgerenemy, on_on_overlap11)

def on_on_overlap12(sprite12, otherSprite12):
    info.change_score_by(2)
    sprites.destroy(Carrot2)
    Player_Hero.start_effect(effects.hearts, 500)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Carrot, on_on_overlap12)

def on_on_overlap13(sprite13, otherSprite13):
    info.change_life_by(-1)
    sprites.destroy(Donut2, effects.spray, 500)
    Player_Hero.start_effect(effects.fire, 500)
    scene.camera_shake(8, 500)
    music.play(music.melody_playable(music.power_down),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Donut, on_on_overlap13)

def Levelcontrol():
    global Play, Cursor, Player_Hero
    if Level == 0:
        scene.set_background_image(img("""
            9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                        99999999999999999999999999999999999999999999999999999999999999999999999fffffffffffffffff9999fff99999999999999999999999999999999999999999999999999999999999999999
                        9999999999999999999fff999fffffffffff99999999999fff99999999fff9999999999fffffffffffffffff9999fff999999fff99999999999999999999999999999999999999999999999999999999
                        999999999fff9999999fff999fffffffffff9999999999ffff99999999fff9999999999fffffffffffffffff9999fff999999fff999999fff99999999999999fff999999999999999999999999999999
                        999999999fff9999999fff999fffffffffff9999999999ffff99999999fff99999999999999999fff99999999999fff999999fff999999fffff999999999999fff999999999999999999999999999999
                        999999999fff9999999fff999fff999999999999999999ffff99999999fff99999999999999999fff99999999999fff999999fff999999ffffff9999999999ffff999999999999999999999999999999
                        999999999fff9999999fff999fff99999999999999999ffffff9999999fff99999999999999999fff99999999999fff999999fff9999999fffffff99999999ffff999999999999999999999999999999
                        999999999fff9999999fff999fff99999999999999999ffffff9999999fff99999999999999999fff99999999999fff999999fff999999999ffffff999999ffff9999999999999999999999999999999
                        999999999fff9999999fff999fff99999999999999999ffffff9999999fff99999999999999999fff99999999999fff999999fff9999999999fffffff9999ffff9999999999999999999999999999999
                        999999999fff9999999fff999fff9999999999999999ffffffff999999fff99999999999999999fff99999999999fff999999fff999999999999ffffff99ffff99999999999999999999999999999999
                        999999999fff9999999fff999fff9999999999999999ffffffff999999fff99999999999999999fff99999999999fff999999fff9999999999999fffffffffff99999999999999999999999999999999
                        999999999fff9999999fff999fff9999999999999999fff99fff999999fff99999999999999999fff99999999999fff999999fff999999999999999ffffffff999999999999999999999999999999999
                        999999999fffffffffffff999fff999999999999999ffff99ffff99999fff99999999999999999fff99999999999ffffffffffff9999999999999999fffffff999999999999999999999999999999999
                        999999999fffffffffffff999fffffff99999999999ffff99ffff99999fff99999999999999999fff99999999999ffffffffffff999999999999999999ffff9999999999999999999999999999999999
                        999999999fffffffffffff999fffffff9999999999ffff9999fff99999fff99999999999999999fff99999999999ffffffffffff999999999999999999ffff9999999999999999999999999999999999
                        999999999fff9999999fff999fffffff9999999999ffff9999fff99999fff99999999999999999fff99999999999fff999999fff99999999999999999ffff99999999999999999999999999999999999
                        999999999fff9999999fff999fff99999999999999ffffffffffff9999fff99999999999999999fff99999999999fff999999fff9999999999999999fffff99999999999999999999999999999999999
                        999999999fff9999999fff999fff9999999999999fffffffffffff9999fff99999999999999999fff99999999999fff999999fff9999999999999999ffff999999999999999999999999999999999999
                        999999999fff9999999fff999fff9999999999999fffffffffffff9999fff99999999999999999fff99999999999fff999999fff999999999999999ffff9999999999999999999999999999999999999
                        999999999fff9999999fff999fff9999999999999fff9999999ffff999fff99999999999999999fff99999999999fff999999fff999999999999999ffff9999999999999999999999999999999999999
                        999999999fff9999999fff999fff999999999999ffff9999999ffff999fff99999999999999999fff99999999999fff999999fff99999999999999ffff99999999999999999999999999999999999999
                        999999999fff9999999fff999fff999999999999ffff99999999fff999fff99999999999999999fff99999999999fff999999fff99999999999999ffff99999999999999999999999999999999999999
                        999999999fff9999999fff999fff999999999999fff999999999ffff99fff99999999999999999fff99999dd9999fff999999fff9999999999999ffff999999999999999999999999999999999999999
                        999999999fff9999999fff999fffffffffff9999fff999999999ffff99ffffffffffff99999999fff9999dddd999fff999999fff9999999999999ffff999999999999999999999999999999999999999
                        999999999fff9999999fff999fffffffffff9999fff9999999999fff99ffffffffffff99999999fff9999dddd999fff999999fff999999999999ffff9999999999999999999999999999999999999999
                        999999999fff9999999fff999fffffffffff9999999999999999999999ffffffffffff99999999fff9999ddddd99fff999999fff999999999999ffff9999999999999999999999999999999999999999
                        999999999999999999999999999999999999999999999999999999999999999999999999999999fff999dddddd9999999999999999999999999ffff99999999999999999999999999999999999999999
                        999999999999999999999999999999999999999999999999999999999999999999999999999999fff999dddddd9999999999999999999999999ffff99999999999999999999999999999999999999999
                        999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddd9999999999999999999999999fff999999999999999999999999999999999999999999
                        999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddd999999999999999999999999999999999999999999999ffff999999999999999999999
                        999999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddd999999999999999999999999999999999999999999999f77f999999999999999999999
                        99999999999999999999999999999999999999999999999999999999999999999999999999999999999ddddddd999999999999999999999999999999999999999999999f77f999999999999999999999
                        99999999999999999999999999999999999999999999999999999999999999999999999999999999999ddddddd999999999999999999999999999999999999999999999f77f999999999dddddddddd99
                        dd999999999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd99999999999999999999999999999999999999999999f77f99999999ddddddddddddd
                        ddddd999999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd99999999999999999999999999999999999999999999f77f9999999dddddddddddddd
                        dddddd99999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd9999999999999999999999999999999999999999999ffffff999999dddddddddddddd
                        ddddddd9999999999999999999999999999999999999999999999999999999999999999999999999999dddddddd9999999999999999999fff9999999999999999999fffffffffff999dddddddddddddd
                        ddddddd99999999999999999999999999999999999999999999999999999999999999999fff9999fff9ddddfffffffffffffff99999999fffff9999999999999999ff7ff7f2ff22fdddddddddddddddd
                        ddddddd99999999999999999999999999999999999999999999999999999999999999999fff9999fff9ddddfffffffffffffff999999fffffffff999999999999ff2f7ff7f2ff222ffdddddddddddddd
                        ddddddd99999999999999999999999999999999999999999999999999999999999999999fff9999fff9ddddfffffffffffffff999999fffffffffff999999999f22ff7ff7f2f7f2222fddddddddddddd
                        ddddddd99999999999999999999999999999999999999999999999999999999999999999fff9999fff9ddddfffdd9999999999999999fff99ffffffff999999f222fffff7f2fff22222fdddddddddddd
                        ddddddd999999999999999999999999999999999ddd99999999999999999999999999999fff9999fff9ddddfffdd9999999999999999fff9999ffffffff9999f222fffffff22222fff2f7777dddddddd
                        ddddddd999999999999999999999999999999ddddddd9999999999999999999999999999fff9999fff9ddddfffddd999999999999999fff999999ffffff999f2222fff222222222fff22f7777ddddddd
                        ddddddd9999999999999999999999999999ddddddddd9999999999999999999999999999fff9999fff9ddddfffddd999999999999999fff999999ffffff99f22222fff222222222fff222f7777dddddd
                        ddddddd99999999999999999999999999dddddddddddd999999999999999999999999999fff9999fff9ddddfffdddd99999999999997fff77777ffffff777f22222222222222222222222f7777dddddd
                        ddddddd9999999999999999999999999ddddddddddddd999999999999999999999999999fff9999fffdddddfffffffffffff77777777fff777fffffff7777f22222222222222222222222f7777dddddd
                        ddddddd999999999999999999999999dddddddddddddd999999999999999999999999999ffffffffffdddddfffffffffffff77777777fff77ffffff777777f22222222222222222222222f7777dddddd
                        ddddddd999999999997999999999999dddddddddddddd999999999999999999999999999ffffffffffdddddfffffffffffff77777777fff7ffffff7777777f22222222222222222222222f7777dddddd
                        ddddddd999997777777799999999999dddddddddddddd999999999999999999999999dd9ffffffffffdddddfffdddd77777777777777ffffffff777777777f22222222222222222222222f7777dddddd
                        ddddddd997777777777799999999999ddddddddddddddd9999999999999999999999ddddfff9999fffdddddfffdddd77777777777777fffffff7777777777f22222222222222222222222f7777dddddd
                        ddddddd77777777777779999999999dddddddddddddddd999999999999999999999dddddfffdd99fffdddddfffdddd77777777777777ffffff77777777777f22222222222222222222222f7777dddddd
                        ddddddd77777777777779999999999dddddddddddddddd999999999999999999999dddddfffddddfffdddddfffdddd77777777777777ffffffff777777777f22222222222222fff222222f7777dddddd
                        ddddddd77777777777777999999999dddddddddddddddd999999999999999999999dddddfffddddfffdddddfffdddd77777777777777fffffffff77777777f222222fff22222fff222222f7777dddddd
                        ddddd7777777777777777999999999dddddddddddddddd99999999999999999999ddddddfffddddfffdddddfffddd777777777777777fff7ffffff7777777f222222ffff222ffff222222f7777dddddd
                        dddd77777777777777777999999ddddddddddddddddddd99999999999999999999ddddddfffddddfffdddddfffddd777777777777777fff777ffffff777777f22222ffff222ffff22222f77777dddddd
                        dddd77777777777777777ddddddddddddddddddddddddd99ddd999999999999999ddddddfffddddfffdddddfffddd777777777777777fff7777ffffff777777f22222ffffffffff2222f777777dddddd
                        ddd777777777777777777ddddddddddddddddddddddddd99dddd99999999999999ddddddfffddddfffdddddffffffffffffffff77777fff77777ffffff77777f22222fffffffff22222f777777dddddd
                        ddd777777777777777777dddddddddddddddddddddddddddddddd9999999999999ddddddfffddddfffdddddffffffffffffffff77777fff7777777ffffff7777f22222ffffffff2222f77777777ddddd
                        dd7777777777777777777ddddddddddddddddddddddddddddddddd999999999999dddddddddddddfffdddddffffffffffffffff77777fff77777777ffffff7777ff2222222222222ff777777777ddddd
                        dd7777777777777777777ddddddddddddddddddddddddddddddddd99999999999ddddddddddddddddddddddddddd7777777777777777fff777777777fffff777777f22222222222f77777777777ddddd
                        d77777777777777777777ddddddddddddddddddddddddddddddddd99999999999dddddddddddddddddddddddddd7777777777777777777777777777777fff7777777fffffffffff777777777777ddddd
                        d77777777777777777777ddddddddddddddddddddddddddddddddd99999999999ddddddddddddddddddddddddd777777777777777777777777777777777777777777777777777777777777777777dddd
                        d77777777777777777777dddddddddddd77777dddddddddddddddd99999999999dddddddddddddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777dddd
                        7777777777777777777777ddddddddddd7777777dddddddddddddd99999999999ddddddddddddddddddddddd777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777dddddddddd77777777dddddddddddddd9999999999dddddddddddddddd77777777777777777777777777777777777777777777777777777777777777777777777777777777
                        77777777777777777777777ddddddd77777777777dddddddddddddddddddddd9dddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777dddd777777777777dddddddddddddddddddddddddddddddddddd77777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        77777777777777777777777777777777777777777dddddddddddddddddddddddddddddddddddd77777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        77777777777777777777777777777777777777777ddddddddddddddddddddddddddddddddddd777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        77777777777777777777777777777777777777777ddddddddddddddddddddddddddddddddddd777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777ddddddddddddddddddddddddddddddddd777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        77777777777777777777777777777777777777777777777ddddddddddddddddddddddddddddd777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777dddddddddddddddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        777777777777777777777777777777777777777777777777777dddddddddddddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777ddddddddddddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777ddddddddddddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777ddddddddddddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777ddddddddddddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        77777777777777777777777777777777777777777777777777777dddddddddddddddddddddd7777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        77777777777777777777777777777777777777777777777777777777dddddddddddddddddd77777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777dddddd777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
                        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        """))
        Play = sprites.create(img("""
                ......................
                            ......................
                            ......................
                            ......................
                            ......................
                            .ffffffffffffffffffff.
                            .f111111111111111111f.
                            .f1ff11f1111f11f11f1f.
                            .f1f1f1f111f1f1f11f1f.
                            .f1ff11f111fff11ff11f.
                            .f1f111f111f1f111f11f.
                            .f1f1111ff1f1f11f111f.
                            .f111111111111111111f.
                            .ffffffffffffffffffff.
                            ......................
                            ......................
                            ......................
                            ......................
                            ......................
                            ......................
                            ......................
                            ......................
            """),
            SpriteKind.Button)
        Cursor = sprites.create(img("""
                . . . . . . . . f . . . . . . . 
                            . . . . . . . . f . . . . . . . 
                            . . . . . . . . f . . . . . . . 
                            . . . . . . . f f f . . . . . . 
                            . . . . . . . f 1 f . . . . . . 
                            . . . . . . . f 1 f . . . . . . 
                            . . . . . . f 1 1 1 f . . . . . 
                            . . . . . . f 9 1 1 f . . . . . 
                            . . . . . . f 9 1 1 f . . . . . 
                            . . . . . f 1 9 1 1 1 f . . . . 
                            . . . . . f 1 9 1 1 1 f . . . . 
                            . . . . . f 9 1 f 1 1 f . . . . 
                            . . . . f 1 1 f . f 1 1 f . . . 
                            . . . . f f f . . . f 1 f . . . 
                            . . . f f . . . . . . f f f . . 
                            . . . f . . . . . . . . . f . .
            """),
            SpriteKind.cursor)
        Play.set_position(80, 78)
        controller.move_sprite(Cursor)
        music.stop_all_sounds()
    if Level == 1:
        effects.star_field.start_screen_effect()
        Player_Hero = sprites.create(img("""
                ...........f..........
                            ...........f..........
                            ..........f8f.........
                            ..........f8f.........
                            .....aa..f688f.aa.....
                            .....f5..f888f.5f.....
                            .....ff.f88f88fff.....
                            .....5f.f88f88ff5.....
                            .....fff68f9f88ff.....
                            .....fff88f6f88ff.....
                            .....ff88f699f8ff.....
                            .....f888fffff88f.....
                            .....f68ff888ff8f.....
                            ....ff8868888868ff....
                            ....ff86688f8866ff....
                            ...f9f868ff.ff86f6f...
                            ...f6f66f.....f6f6f...
                            ..f66fff.......ff69f..
                            ..f6ff.a.......a.f6f..
                            .f9f....faaaaaf...f9f.
                            .ff................ff.
                            f....................f
            """),
            SpriteKind.player)
        Player_Hero.set_position(77, 97)
        controller.move_sprite(Player_Hero)
        music.play(music.create_song(hex("""
                0078000408020500001c00010a006400f4016400000400000000000000000000000000050000043a000400080001220c001000011b14001800011b18001c00012520002400012428002c00021e2530003400011d38003c000220293c004000031d242904001c00100500640000041e000004000000000000000000000000000a040004270000000400012904000800011e08000c0002192a10001400012738003c0001203c004000031d242706001c00010a006400f401640000040000000000000000000000000000000002480004000800012708000c00011e0c001000012514001800012218001c0002202a20002400012724002800021b292c003000012a30003400012534003800051b1d1e222938003c00011908001c000e050046006603320000040a002d000000640014000132000201000225001000140001251400180001292400280001242c003000021e2530003400012a38003c00012409010e02026400000403780000040a000301000000640001c80000040100000000640001640000040100000000fa0004af00000401c80000040a00019600000414000501006400140005010000002c0104dc00000401fa0000040a0001c8000004140005d0076400140005d0070000c800029001f40105c201f4010a0005900114001400039001000005c201f4010500058403050032000584030000fa00049001000005c201f4010500058403c80032000584030500640005840300009001049001000005c201f4010500058403c80064000584030500c8000584030000f40105ac0d000404a00f00000a0004ac0d2003010004a00f0000280004ac0d9001010004a00f0000280002d00700040408070f0064000408070000c80003c800c8000e7d00c80019000e64000f0032000e78000000fa00032c01c8000ee100c80019000ec8000f0032000edc000000fa0003f401c8000ea901c80019000e90010f0032000ea4010000fa0001c8000004014b000000c800012c01000401c8000000c8000190010004012c010000c80002c800000404c8000f0064000496000000c80002c2010004045e010f006400042c010000640002c409000404c4096400960004f6090000f40102b80b000404b80b64002c0104f40b0000f401022003000004200300040a000420030000ea01029001000004900100040a000490010000900102d007000410d0076400960010d0070000c8005900000001000600010305070b0800090001050c000d00020408100011000303040a140015000100180019000200031c001d000200072c002d00010b300031000108340035000300060a380039000201083c003d0005000105070a
            """)),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
        music.set_volume(27)
        info.set_life(3)
        game.set_game_over_scoring_type(game.ScoringType.HIGH_SCORE)
        Player_Hero.set_stay_in_screen(True)
        if info.life() == 0:
            music.stop_all_sounds()
    else:
        music.stop_all_sounds()

def on_on_overlap14(sprite14, otherSprite14):
    sprites.destroy(oilyFood, effects.spray, 500)
    sprites.destroy(Bullet)
    info.change_score_by(2)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.Oilyfood, SpriteKind.projectile, on_on_overlap14)

def on_on_overlap15(sprite15, otherSprite15):
    info.change_life_by(-1)
    sprites.destroy(oilyFood, effects.spray, 500)
    Player_Hero.start_effect(effects.fire, 500)
    scene.camera_shake(8, 500)
    music.play(music.melody_playable(music.power_down),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.player, SpriteKind.Oilyfood, on_on_overlap15)

def on_on_overlap16(sprite16, otherSprite16):
    sprites.destroy(Burger_enemy, effects.spray, 500)
    sprites.destroy(Bullet)
    info.change_score_by(3)
    music.play(music.melody_playable(music.power_up),
        music.PlaybackMode.UNTIL_DONE)
sprites.on_overlap(SpriteKind.Burgerenemy,
    SpriteKind.projectile,
    on_on_overlap16)

oilyFood: Sprite = None
Carrot2: Sprite = None
Burger_enemy: Sprite = None
Potato2: Sprite = None
milk2: Sprite = None
ExtraHealth: Sprite = None
Donut2: Sprite = None
Exercise_1: Sprite = None
Bullet: Sprite = None
Coke_Enemy: Sprite = None
Veggies2: Sprite = None
Player_Hero: Sprite = None
Tomato2: Sprite = None
Cursor: Sprite = None
Play: Sprite = None
Level = 0
Level = 0
Levelcontrol()

def on_update_interval():
    global Coke_Enemy
    Coke_Enemy = sprites.create_projectile_from_side(img("""
            . . . f f f f f f f f f f . . . 
                    . . . f 2 2 2 2 8 8 8 8 f . . . 
                    . . . f 2 2 8 8 8 2 2 8 f . . . 
                    . . . f 8 8 8 2 2 2 2 2 f . . . 
                    . . . f 2 f f 2 2 f f 2 f . . . 
                    . . . f f 2 2 2 f 2 2 f f . . . 
                    . . . f f 2 2 2 f 2 2 f f . . . 
                    . . . f 2 f f 2 2 f f 2 f . . . 
                    . . . f 2 2 2 2 2 2 2 2 f . . . 
                    . . . f 2 f 2 f 2 f f f f . . . 
                    . . . f 2 f f 2 2 f 2 2 f . . . 
                    . . . f 2 f f 2 2 f f 2 f . . . 
                    . . . f 2 f 2 f 2 f f f f . . . 
                    . . . f 2 2 8 8 8 8 8 8 f . . . 
                    . . . f 8 8 2 2 2 2 2 2 f . . . 
                    . . . f f f f f f f f f f . . .
        """),
        0,
        50)
    Coke_Enemy.x = randint(0, scene.screen_width())
    Coke_Enemy.set_kind(SpriteKind.Cokeenemy)
game.on_update_interval(randint(3000, 3500), on_update_interval)

def on_update_interval2():
    global Donut2
    Donut2 = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . f f f f f f f . . . . 
                    . . . . f e e e e e e e f . . . 
                    . . . f e 3 3 3 3 3 5 3 e f . . 
                    . . f e 3 2 5 5 5 3 3 3 3 e f . 
                    . . f e 3 3 f f f f f 3 5 e f . 
                    . . f e 2 3 f . . . f 3 3 e f . 
                    . . f e 5 3 f . . . f 3 2 e f . 
                    . . f e 3 3 f . . . f 5 3 e f . 
                    . . f e 3 5 f f f f f 5 3 e f . 
                    . . f e 3 3 3 3 2 5 5 5 3 e f . 
                    . . . f e 3 2 5 3 3 2 3 e f . . 
                    . . . . f e e e e e e e f . . . 
                    . . . . . f f f f f f f . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        0,
        50)
    Donut2.x = randint(0, scene.screen_width())
    Donut2.set_kind(SpriteKind.Donut)
game.on_update_interval(randint(3000, 3500), on_update_interval2)

def on_update_interval3():
    global oilyFood
    oilyFood = sprites.create_projectile_from_side(img("""
            . . 2 2 b b b b b . . . . . . . 
                    . 2 b 4 4 4 4 4 4 b . . . . . . 
                    2 2 4 4 4 4 d d 4 4 b . . . . . 
                    2 b 4 4 4 4 4 4 d 4 b . . . . . 
                    2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                    2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                    2 2 b 4 4 4 4 4 4 4 b e . . . . 
                    . 2 b b b 4 4 4 b b b e . . . . 
                    . . e b b b b b b b e e . . . . 
                    . . . e e b 4 4 b e e e b . . . 
                    . . . . . e e e e e e b d b b . 
                    . . . . . . . . . . . b 1 1 1 b 
                    . . . . . . . . . . . c 1 d d b 
                    . . . . . . . . . . . c 1 b c . 
                    . . . . . . . . . . . . c c . .
        """),
        0,
        50)
    oilyFood.x = randint(0, scene.screen_width())
    oilyFood.set_kind(SpriteKind.Oilyfood)
game.on_update_interval(randint(3000, 3500), on_update_interval3)

def on_update_interval4():
    global Carrot2
    Carrot2 = sprites.create_projectile_from_side(img("""
            . . . . . . f f . . . . . . . . 
                    . . . . . . f f . . f f f . . . 
                    . . . . . . f f f f f f . . . . 
                    . . . . f f f 7 f 7 f f . . . . 
                    . . . f 4 4 f f f 7 f . . . . . 
                    . . . f 2 4 4 4 f f f . . . . . 
                    . . . f 4 4 4 f 4 4 f . . . . . 
                    . . f 4 f f 4 4 f f . . . . . . 
                    . . f 4 2 f 4 4 f . . . . . . . 
                    . . f 4 4 4 4 f . . . . . . . . 
                    . . f 4 f 4 f . . . . . . . . . 
                    . f 4 4 4 f . . . . . . . . . . 
                    . f 4 4 f . . . . . . . . . . . 
                    . f 2 f . . . . . . . . . . . . 
                    . f f . . . . . . . . . . . . . 
                    . f . . . . . . . . . . . . . .
        """),
        0,
        50)
    Carrot2.x = randint(0, scene.screen_width())
    Carrot2.set_kind(SpriteKind.Carrot)
game.on_update_interval(randint(9000, 15000), on_update_interval4)

def on_update_interval5():
    global Veggies2
    Veggies2 = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . f f f f f . . . . . 
                    . . f f f f f 7 7 7 f f f . . . 
                    f f f 7 7 7 7 7 7 7 7 7 f f f . 
                    . f f 7 7 7 7 7 7 7 7 7 7 7 f f 
                    f f f f f f f 7 7 7 7 7 7 7 7 f 
                    f 7 7 7 7 7 f f f 7 7 7 7 7 7 f 
                    f f 7 1 1 7 7 7 f f f 7 7 7 7 f 
                    . f f 7 1 7 7 7 7 7 7 7 7 7 f f 
                    . . f 7 1 1 7 7 1 1 1 7 7 f f . 
                    . . f f 7 1 1 1 7 7 f f f f . . 
                    . . . f 7 7 7 7 7 f f . . . . . 
                    . . . f f f f f f . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        0,
        50)
    Veggies2.x = randint(0, scene.screen_width())
    Veggies2.set_kind(SpriteKind.Veggies)
game.on_update_interval(randint(10000, 15000), on_update_interval5)

def on_update_interval6():
    global Potato2
    Potato2 = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . f f f f . . . . f f f f . 
                    . f f f e f d f f f f f d f f f 
                    f f e e e f d e e e e e d f f f 
                    f e e e e f d f d e e e e e f f 
                    f e e e e f d f e e e e e e f f 
                    f f e e e f d e e e e e e e e f 
                    . f e e e e e e e f e d f e e f 
                    . f f e e e e e e f e d f e e f 
                    . . f f e e e e e f e d f e e f 
                    . . . f f f f e e f f e e e e f 
                    . . . . . . . f f f f f f f f . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        0,
        50)
    Potato2.x = randint(0, scene.screen_width())
    Potato2.set_kind(SpriteKind.Potato)
game.on_update_interval(randint(10000, 15000), on_update_interval6)

def on_update_interval7():
    global ExtraHealth
    ExtraHealth = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . f f f . . . . . f f f . . 
                    . . f 3 3 3 f . . . f 3 3 3 f . 
                    . f 3 3 1 3 3 f . f 3 3 3 3 3 f 
                    f f 3 1 3 3 3 3 f 3 3 3 3 3 3 f 
                    f 3 3 1 3 3 3 3 3 3 3 3 3 3 3 f 
                    f 3 3 1 3 3 3 3 3 3 3 3 3 3 3 f 
                    f 3 3 1 3 3 3 3 3 3 3 3 3 3 3 f 
                    . f 3 3 1 3 3 3 3 3 3 3 3 3 f . 
                    . . f 3 3 1 3 3 3 3 3 3 3 f . . 
                    . . . f 3 3 1 3 3 3 3 3 f . . . 
                    . . . . f 3 3 1 3 3 3 3 f . . . 
                    . . . . . f 3 3 1 3 3 f . . . . 
                    . . . . . . f 3 3 3 f . . . . . 
                    . . . . . . . f 3 f . . . . . . 
                    . . . . . . . . f . . . . . . .
        """),
        0,
        50)
    ExtraHealth.x = randint(0, scene.screen_width())
    ExtraHealth.set_kind(SpriteKind.HealthPickup)
game.on_update_interval(randint(10000, 15000), on_update_interval7)

def on_update_interval8():
    global Exercise_1
    Exercise_1 = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . 1 1 1 1 1 . . . . . 
                    . . . . . . 1 5 5 5 1 . . . . . 
                    . . . . . . 1 5 5 5 1 . . . . . 
                    . . . . . . 1 5 5 5 1 . . . . . 
                    . . . . . . 1 5 5 5 1 . . . . . 
                    . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                    . . . . . . . . 1 . . . . . . . 
                    . . . . . . . . 1 . . . . . . . 
                    . . . . . . . . 1 . . . . . . . 
                    . . . . . . . . 1 . . . . . . . 
                    . . . . . . . . 1 . . . . . . . 
                    . . . . . . . 1 . 1 . . . . . . 
                    . . . . . . . 1 . 1 . . . . . . 
                    . . . . . . 1 . . . 1 . . . . . 
                    . . . . . 1 . . . . . 1 . . . .
        """),
        0,
        50)
    Exercise_1.x = randint(0, scene.screen_width())
    Exercise_1.set_kind(SpriteKind.Exercise)
game.on_update_interval(randint(10000, 15000), on_update_interval8)

def on_update_interval9():
    global Burger_enemy
    Burger_enemy = sprites.create_projectile_from_side(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . b b b b b b b . . . . . 
                    . . c b 4 4 4 4 4 5 4 b b . . . 
                    . c 4 4 4 4 4 4 4 4 4 4 4 b . . 
                    . b 4 4 4 4 4 4 4 4 4 4 4 b . . 
                    b 4 4 4 4 5 4 4 5 4 4 4 4 4 b . 
                    e 4 4 4 4 4 4 4 4 4 5 4 4 4 b . 
                    . e 4 4 4 4 5 4 4 4 4 4 4 e . . 
                    . e 4 4 4 4 4 4 4 4 4 4 4 e . . 
                    7 7 e e 4 4 4 4 4 4 4 e e 7 7 . 
                    7 7 7 7 e e e e e e e 7 7 7 7 . 
                    5 5 7 7 7 7 7 7 7 7 7 7 7 5 5 . 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 e . 
                    e e 4 4 4 4 4 4 4 4 4 4 4 e e . 
                    . e e e 4 4 4 4 4 4 4 4 e e . . 
                    . . . e e e e e e e e e e . . .
        """),
        0,
        50)
    Burger_enemy.x = randint(0, scene.screen_width())
    Burger_enemy.set_kind(SpriteKind.Burgerenemy)
game.on_update_interval(randint(2000, 6000), on_update_interval9)

def on_update_interval10():
    global Tomato2
    Tomato2 = sprites.create_projectile_from_side(img("""
            . . . . . . . f f f . . . . . . 
                    . . . . . . . f 7 f . . . . . . 
                    . . . . . . . f 7 f . . . . . . 
                    . . . . . f f f f f f f . . . . 
                    . . . . f f f 7 f 7 7 f f . . . 
                    . . . f 2 f 7 f f f 7 f 2 f . . 
                    . . f 2 f f f f 2 f f f 2 2 f . 
                    . . f 2 2 2 f 2 2 2 f f 2 2 f . 
                    . . f 2 4 2 2 2 2 2 2 2 2 2 f . 
                    . . f 2 4 2 2 2 2 2 2 2 2 2 f . 
                    . . f 2 4 4 2 2 2 2 2 2 2 2 f . 
                    . . f 2 2 4 2 2 2 2 2 2 2 2 f . 
                    . . f 2 2 4 2 2 2 2 2 2 2 2 f . 
                    . . . f 2 4 4 2 2 2 2 2 2 f . . 
                    . . . . f 2 2 2 2 2 2 2 f . . . 
                    . . . . . f f f f f f f . . . .
        """),
        0,
        50)
    Tomato2.x = randint(0, scene.screen_width())
    Tomato2.set_kind(SpriteKind.Tomato)
game.on_update_interval(randint(15000, 17000), on_update_interval10)

def on_update_interval11():
    global milk2
    milk2 = sprites.create_projectile_from_side(img("""
            . . . f f f f f f f f f f f . . 
                    . . . f f 1 1 1 1 1 1 1 1 f . . 
                    . . f 1 1 1 1 1 1 1 1 1 1 1 f . 
                    . . f f f f f f f f f f f f f . 
                    . . f 8 8 8 8 8 8 8 8 8 8 8 f . 
                    . . f 8 f f 8 f f 8 f f f 8 f . 
                    . . f 9 f 8 f 8 f 8 8 f 8 8 f . 
                    . . f 9 f 8 8 8 f 8 8 f 8 8 f . 
                    . . f 9 f 8 8 8 f 8 f f f 8 f . 
                    . . f 9 8 8 8 8 8 8 8 8 8 8 f . 
                    . . f 9 8 f 8 8 8 f 8 f 8 8 f . 
                    . . f 9 8 f 8 8 8 f f 8 8 8 f . 
                    . . f 9 8 f 8 8 8 f f 8 8 8 f . 
                    . . f 9 8 f f f 8 f 8 f 8 8 f . 
                    . . f 9 8 8 8 8 8 8 8 8 8 8 f . 
                    . . f f f f f f f f f f f f f .
        """),
        0,
        50)
    milk2.x = randint(0, scene.screen_width())
    milk2.set_kind(SpriteKind.milk)
game.on_update_interval(randint(15000, 20000), on_update_interval11)
