﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    scene bg sergei room
    play music sad1
    "За окном тихий зимний вечер."
    m "Всё идёт, как обычно: я сижу за своим столом и пялюсь в монитор своего компьютера, зависая в соц. сетях."
    "Сам-то я не работаю нигде, но на жизнь мне хватает, родители время от времени помогают мне материальной поддержкой, а на улицу я почти не выхожу."
    "Мне нечего там делать, моя жизнь в основном проходит в интернете, где куда больше  интересного, а главное есть люди которые разделяют мои увлечения."
    "Всегда находится та или иная группа людей, с кем можно обсудить общую интересующую нас тему."
    "Хотя, учитывая что мне нравится, в чатах мы только и обсуждаем, что аниме или игры."
    "Меня устраивает такая жизнь, но иногда бывает ужасно скучно и даже хочется начать что-то менять. "
    m "Все вокруг слишком привычное, всегда незаправленная кровать, над которой находятся все те же аниме плакаты и фигурки, гирлянда который висит с прошлого года, один и тот же вид из окна и конечно же экран монитора который я вижу первым с утра и последним перед сном. Но лень быстро берет свое, вряд ли я смогу жить по другому."  
    "Да и друзья в интернете не сказать что настоящие, просто люди которым так же нечего делать как и мне. Есть, конечно, пара беседок, которые меня «поглотили» своей ламповой атмосферой, но и это мелкий эффект, который в скором времени рассеется, словно пыль в воздухе..."
    stop music fadeout 2.0

    return
