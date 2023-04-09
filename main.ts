namespace SpriteKind {
    export const Cokeenemy = SpriteKind.create()
    export const Burgerenemy = SpriteKind.create()
    export const HealthPickup = SpriteKind.create()
    export const Veggies = SpriteKind.create()
    export const Button = SpriteKind.create()
    export const cursor = SpriteKind.create()
    export const milk = SpriteKind.create()
    export const Carrot = SpriteKind.create()
    export const Tomato = SpriteKind.create()
    export const Potato = SpriteKind.create()
    export const Exercise = SpriteKind.create()
    export const Donut = SpriteKind.create()
    export const Oilyfood = SpriteKind.create()
    export const tutorial = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.HealthPickup, function (sprite7, otherSprite7) {
    info.changeLifeBy(1)
    sprites.destroy(ExtraHealth)
    Player_Hero.startEffect(effects.hearts, 500)
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Oilyfood, function (sprite15, otherSprite15) {
    info.changeLifeBy(-1)
    sprites.destroy(oilyFood, effects.spray, 500)
    Player_Hero.startEffect(effects.fire, 500)
    scene.cameraShake(8, 500)
    music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Carrot, function (sprite12, otherSprite12) {
    info.changeScoreBy(2)
    sprites.destroy(Carrot2)
    Player_Hero.startEffect(effects.hearts, 500)
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.cursor, SpriteKind.Button, function (sprite, otherSprite) {
    if (otherSprite == Play && controller.A.isPressed()) {
        Level = 1
        Levelcontrol()
        sprites.destroy(Cursor)
        sprites.destroy(Play)
        effects.starField.startScreenEffect()
        scene.setBackgroundImage(img`
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
            `)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Burgerenemy, function (sprite11, otherSprite11) {
    info.changeLifeBy(-1)
    sprites.destroy(Burger_enemy)
    Player_Hero.startEffect(effects.fire, 500)
    scene.cameraShake(8, 500)
    music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.UntilDone)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (Level == 1) {
        music.play(music.melodyPlayable(music.pewPew), music.PlaybackMode.UntilDone)
        Bullet = sprites.createProjectileFromSprite(img`
            ......................
            ......................
            ......................
            ......................
            ......................
            ......................
            ......................
            ......................
            ........55...55.......
            ........75...57.......
            ........77...77.......
            ........22...22.......
            ........22...22.......
            ........66...66.......
            ......................
            ......................
            ......................
            ......................
            ......................
            ......................
            ......................
            ......................
            `, Player_Hero, 0, -100)
        Bullet.setKind(SpriteKind.Projectile)
    }
})
sprites.onOverlap(SpriteKind.Cokeenemy, SpriteKind.Projectile, function (sprite10, otherSprite10) {
    sprites.destroy(Coke_Enemy, effects.spray, 500)
    sprites.destroy(Bullet)
    info.changeScoreBy(2)
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.milk, function (sprite8, otherSprite8) {
    info.changeScoreBy(5)
    sprites.destroy(milk2)
    Player_Hero.startEffect(effects.hearts, 500)
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Cokeenemy, function (sprite4, otherSprite4) {
    info.changeLifeBy(-1)
    sprites.destroy(Coke_Enemy, effects.spray, 500)
    Player_Hero.startEffect(effects.fire, 500)
    scene.cameraShake(8, 500)
    music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Donut, SpriteKind.Projectile, function (sprite6, otherSprite6) {
    sprites.destroy(Donut2, effects.spray, 500)
    sprites.destroy(Bullet)
    info.changeScoreBy(2)
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Veggies, function (sprite3, otherSprite3) {
    info.changeScoreBy(3)
    sprites.destroy(Veggies2)
    Player_Hero.startEffect(effects.hearts, 500)
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
function Levelcontrol () {
    if (Level == 0) {
        music.play(music.createSong(assets.song`Theme Song`), music.PlaybackMode.LoopingInBackground)
        scene.setBackgroundImage(img`
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
            `)
        game.showLongText("USE ARROW TO MOVE CURSOR AND A FOR OK", DialogLayout.Bottom)
        Play = sprites.create(img`
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            ........................................
            .fffffffffffffffffffffffffffffffff......
            .f1111111111111111111111111111111fd.....
            .f11ffffff111f1111111f11fd11111f1fd.....
            .f11f1111df11fd11111f1f11d1111f11fd.....
            .f11f1111df11fd11111f1f11fd111f11fd.....
            .f11f1111df11fd1111fd11fd1fd1f111fd.....
            .f11fdddddf11fd1111fd11fd11ffd111fd.....
            .f11ffffffd11fd1111fd11fd111fd111fd.....
            .f11fd1111111fd1111fffffd111fd111fd.....
            .f11fd1111111fd1111fd11fd111fd111fd.....
            .f11fd1111111fd1111fd11fd111fd111fd.....
            .f11fd1111111fffff1fd11fd111fd111fd.....
            .f11d111111111dddd111111111111111fd.....
            .fffffffffffffffffffffffffffffffffd.....
            ...dddddddddddddddddddddddddddddddd.....
            ........................................
            ........................................
            ........................................
            `, SpriteKind.Button)
        Cursor = sprites.create(img`
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
            `, SpriteKind.cursor)
        Play.setPosition(75, 78)
        controller.moveSprite(Cursor)
    }
    if (Level == 1) {
        game.showLongText("USE ARROW TO MOVE AND A TO SHOOT...... Collect healthy food to stay healthy and avoid unhealthy food or else the game will over.....", DialogLayout.Full)
        effects.starField.startScreenEffect()
        Player_Hero = sprites.create(img`
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
            `, SpriteKind.Player)
        Player_Hero.setPosition(75, 93)
        controller.moveSprite(Player_Hero)
        music.setVolume(255)
        info.setLife(3)
        game.setGameOverScoringType(game.ScoringType.HighScore)
        Player_Hero.setStayInScreen(true)
    }
}
sprites.onOverlap(SpriteKind.Oilyfood, SpriteKind.Projectile, function (sprite14, otherSprite14) {
    sprites.destroy(oilyFood, effects.spray, 500)
    sprites.destroy(Bullet)
    info.changeScoreBy(2)
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Donut, function (sprite13, otherSprite13) {
    info.changeLifeBy(-1)
    sprites.destroy(Donut2, effects.spray, 500)
    Player_Hero.startEffect(effects.fire, 500)
    scene.cameraShake(8, 500)
    music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Potato, function (sprite9, otherSprite9) {
    info.changeScoreBy(6)
    sprites.destroy(Potato2)
    Player_Hero.startEffect(effects.hearts, 500)
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Tomato, function (sprite2, otherSprite2) {
    info.changeScoreBy(4)
    sprites.destroy(Tomato2)
    Player_Hero.startEffect(effects.hearts, 500)
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Exercise, function (sprite5, otherSprite5) {
    info.changeScoreBy(7)
    sprites.destroy(Exercise_1)
    Player_Hero.startEffect(effects.hearts, 500)
    music.play(music.melodyPlayable(music.powerUp), music.PlaybackMode.UntilDone)
})
sprites.onOverlap(SpriteKind.Burgerenemy, SpriteKind.Projectile, function (sprite16, otherSprite16) {
    sprites.destroy(Burger_enemy, effects.spray, 500)
    sprites.destroy(Bullet)
    info.changeScoreBy(3)
    music.play(music.melodyPlayable(music.zapped), music.PlaybackMode.UntilDone)
})
let Exercise_1: Sprite = null
let Tomato2: Sprite = null
let Potato2: Sprite = null
let Veggies2: Sprite = null
let Donut2: Sprite = null
let milk2: Sprite = null
let Coke_Enemy: Sprite = null
let Bullet: Sprite = null
let Burger_enemy: Sprite = null
let Cursor: Sprite = null
let Play: Sprite = null
let Carrot2: Sprite = null
let oilyFood: Sprite = null
let Player_Hero: Sprite = null
let ExtraHealth: Sprite = null
let Level = 0
Level = 0
Levelcontrol()
game.onUpdateInterval(randint(3000, 3500), function () {
    if (Level == 1) {
        Coke_Enemy = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        Coke_Enemy.x = randint(0, scene.screenWidth())
        Coke_Enemy.setKind(SpriteKind.Cokeenemy)
    }
})
game.onUpdateInterval(randint(3000, 3500), function () {
    if (Level == 1) {
        Donut2 = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        Donut2.x = randint(0, scene.screenWidth())
        Donut2.setKind(SpriteKind.Donut)
    }
})
game.onUpdateInterval(randint(3000, 3500), function () {
    if (Level == 1) {
        oilyFood = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        oilyFood.x = randint(0, scene.screenWidth())
        oilyFood.setKind(SpriteKind.Oilyfood)
    }
})
game.onUpdateInterval(randint(9000, 15000), function () {
    if (Level == 1) {
        Carrot2 = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        Carrot2.x = randint(0, scene.screenWidth())
        Carrot2.setKind(SpriteKind.Carrot)
    }
})
game.onUpdateInterval(randint(10000, 15000), function () {
    if (Level == 1) {
        Veggies2 = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        Veggies2.x = randint(0, scene.screenWidth())
        Veggies2.setKind(SpriteKind.Veggies)
    }
})
game.onUpdateInterval(randint(10000, 15000), function () {
    if (Level == 1) {
        Potato2 = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        Potato2.x = randint(0, scene.screenWidth())
        Potato2.setKind(SpriteKind.Potato)
    }
})
game.onUpdateInterval(randint(10000, 15000), function () {
    if (Level == 1) {
        ExtraHealth = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        ExtraHealth.x = randint(0, scene.screenWidth())
        ExtraHealth.setKind(SpriteKind.HealthPickup)
    }
})
game.onUpdateInterval(randint(10000, 15000), function () {
    if (Level == 1) {
        Exercise_1 = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        Exercise_1.x = randint(0, scene.screenWidth())
        Exercise_1.setKind(SpriteKind.Exercise)
    }
})
game.onUpdateInterval(randint(2000, 6000), function () {
    if (Level == 1) {
        Burger_enemy = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        Burger_enemy.x = randint(0, scene.screenWidth())
        Burger_enemy.setKind(SpriteKind.Burgerenemy)
    }
})
game.onUpdateInterval(randint(15000, 17000), function () {
    if (Level == 1) {
        Tomato2 = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        Tomato2.x = randint(0, scene.screenWidth())
        Tomato2.setKind(SpriteKind.Tomato)
    }
})
game.onUpdateInterval(randint(15000, 20000), function () {
    if (Level == 1) {
        milk2 = sprites.createProjectileFromSide(img`
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
            `, 0, 50)
        milk2.x = randint(0, scene.screenWidth())
        milk2.setKind(SpriteKind.milk)
    }
})
