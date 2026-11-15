# =========================================================
# ЭКСПЕДИЦИЯ: АРКТУР
# =========================================================

import random
import dungeon
import json
import os

try:
    from colorama import Fore, Style, init

    init()
    COLOR = True
except ImportError:
    COLOR = False
title = "ЭКСПЕДИЦИЯ: АРКТУР"
frame = "=" * (len(title) + 2)

print(frame)
print(" " + title + " ")
print(frame)

print()



def write_save():
    """Сохраняет состояние экспедиции в файл save.json."""
    save = {}
    save["hero"] = hero_name
    save["health"] = health
    save["max_health"] = max_health
    save["strength"] = strength
    save["ammo"] = ammo
    save["sanity"] = sanity
    save["gold"] = gold_total
    save["actions"] = steps
    save["bonus"] = ability_bonus
    save["enemies"] = enemies
    save["position"] = [hero_r, hero_c]
    save["visited"] = [list(p) for p in visited]
    save["loot"] = sorted(found_loot)
    save["log"] = log

    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=2)



loaded = None
if os.path.exists("save.json"):
    print("Обнаружен файл экспедиции. Продолжить миссию? (да/нет)")
    answer = input().strip().lower()
    if answer == "да" or answer == "yes":
        try:
            with open("save.json", encoding="utf-8") as f:
                loaded = json.load(f)
        except json.JSONDecodeError:
            print("Файл данных повреждён. Начинаем новую экспедицию.")
            loaded = None
if loaded is None:
    print("Назови имя исследователя:")
    hero_name = input()

    print(f"Научная станция приветствует тебя, {hero_name}!")
    print("Твой корабль совершил аварийную посадку на планете Арктур. Вокруг простирается ледяная пустыня, а сигнал спасательного маяка едва заметен на сканере.")
    print()

    print("Подготовка исследователя.")
    print("Введи показатели по очереди: здоровье, сила, ловкость и заряд сканера.")

    while True:
        try:
            health = int(input())
            if health <= 0:
                raise ValueError("Запас здоровья должен быть положительным!")
            break
        except ValueError as e:
            print(f"Некорректное значение: {e}. Повтори ввод:")

    max_health = health

    while True:
        try:
            strength = int(input())
            if strength < 0:
                raise ValueError("Сила не может быть меньше нуля!")
            break
        except ValueError as e:
            print(f"Некорректное значение: {e}. Повтори ввод:")

    while True:
        try:
            agility = int(input())
            if agility < 0:
                raise ValueError("Ловкость не может быть меньше нуля!")
            break
        except ValueError as e:
            print(f"Некорректное значение: {e}. Повтори ввод:")

    while True:
        try:
            sanity = int(input())
            if sanity < 0:
                raise ValueError("Заряд сканера не может быть меньше нуля!")
            break
        except ValueError as e:
            print(f"Некорректное значение: {e}. Повтори ввод:")

    base_attack = 10
    damage = base_attack + strength * 1.5
    crit_damage = damage * 2
    ammo = (health + sanity) // 10

    print("\nПараметры исследователя:")
    print(f"Прочность костюма: {health}")
    print(f"Физическая подготовка: {strength}")
    print(f"Манёвренность: {agility}")
    print(f"Заряд сканера: {sanity}")
    print(f"\nМощность атаки: {damage:.1f}")
    print(f"Усиленный импульс: {crit_damage:.1f}")
    print(f"Энергоячейки: {ammo}\n")

    enemies = ["ледяной мутант", "робот-охранник", "песчаный хищник", "древний страж"]
    inventory = {}
    log = []
    gold_total = 0
    ability_bonus = 0
    steps = 0

    MAP = [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", "#", "#"],
        ["#", ".", "#", ".", "#"],
        ["#", ".", ".", "#", "#"],
        ["#", "#", "#", "S", "."]
    ]
    hero_r, hero_c = 4, 3
    visited = {(4, 3)}
    LOOT = {(1, 1): "фрагмент метеорита", (2, 3): "аварийный медпакет", (3, 2): "деталь сигнального маяка"}
    found_loot = set()
    DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}

else:

    hero_name = loaded["hero"]
    health = loaded["health"]
    max_health = loaded["max_health"]
    strength = loaded["strength"]
    ammo = loaded["ammo"]
    sanity = loaded["sanity"]
    gold_total = loaded["gold"]
    steps = loaded["actions"]
    ability_bonus = loaded["bonus"]
    enemies = loaded["enemies"]
    hero_r, hero_c = loaded["position"]
    visited = {tuple(p) for p in loaded["visited"]}
    found_loot = set(loaded["loot"])
    log = loaded["log"]
    inventory = {}

    MAP = [
        ["#", "#", "#", "#", "#"],
        ["#", ".", ".", "#", "#"],
        ["#", ".", "#", ".", "#"],
        ["#", ".", ".", "#", "#"],
        ["#", "#", "#", "S", "."]
    ]
    LOOT = {(1, 1): "фрагмент метеорита", (2, 3): "аварийный медпакет", (3, 2): "деталь сигнального маяка"}
    DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}

    base_attack = 10
    damage = base_attack + strength * 1.5
    crit_damage = damage * 2

    print(f"Экспедиция продолжается: прочность {health}, кредиты {gold_total}, угроз осталось {len(enemies)}.")
def print_leaderboard(log):
    if not log:
        print("Столкновений пока не было. Журнал пуст.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Три самых мощных попадания:")
    for i in range(len(top)):
        print(f"{i + 1}. Этап {top[i][0]}: {top[i][1]:.1f} урона")
    worst = max(log, key=lambda r: r[2])
    print(f"Самая мощная атака противника: {worst[2]} (этап {worst[0]}).")


def print_run_summary(log):
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Нанесено {total:.1f} урона за {rounds} этапов; среднее значение — {total / rounds:.1f}.")
    else:
        print("За время экспедиции столкновений не произошло.")


def scout(r, c, seen):
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total

running = True

commands = ["look", "go <направление>", "rest", "listen", "torch", "train", "descend",
            "leaders", "shop", "backpack", "drink potion",
            "buy <item> [count]", "map", "scout", "newgame", "exit"]

MENU = ["Выбери действие (номер или команду; help — подсказка):",
        "1 - осмотреть местность (look)",
        "2 - переместиться (go north / go west / ...)",
        "3 - восстановить силы (rest)",
        "4 - просканировать сигнал (listen)",
        "5 - проверить обломки корабля (torch)",
        "6 - тренировка на робот-охраннике (train)",
        "7 - исследовать сектор (descend)",
        "8 - статистика столкновений (leaders)",
        "9 - торговый терминал (shop)",
        "10 - снаряжение (backpack)",
        "11 - использовать предмет (drink)",
        "12 - карта сектора (map)",
        "13 - просканировать территорию (scout)",
        "newgame - новая экспедиция",
        "0 - завершить миссию (exit)"]

num_to_verb = {"1": "look", "2": "go", "3": "rest", "4": "listen",
               "5": "torch", "6": "train", "7": "descend", "8": "leaders",
               "9": "shop", "10": "backpack", "11": "drink", "12": "map", "13": "scout", "0": "exit"}

try:
    while running:
        steps += 1
        print(f"--- Цикл миссии {steps} ---")
        print("\n".join(MENU))
        print()

        line = input()
        cmd = line.strip().lower()

        while cmd == "":
            print("Команда не введена. Укажи номер или название действия.")
            line = input()
            cmd = line.strip().lower()

        words = cmd.split()
        verb = words[0]

        if cmd in num_to_verb:
            verb = num_to_verb[cmd]

        print()

        if verb == "look":
            print("Сканер показывает ледяные скалы, разбитые контейнеры и следы неизвестных существ.")

        elif verb == "go":
            if len(words) > 1 and words[1] in DIRECTIONS:
                dr, dc = DIRECTIONS[words[1]]
                nr, nc = hero_r + dr, hero_c + dc

                if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                    hero_r, hero_c = nr, nc
                    visited.add((hero_r, hero_c))
                    print(f"Ты перемещаешься в направлении {words[1]}. Координаты сектора: ({hero_r}, {hero_c}).")

                    if (hero_r, hero_c) in LOOT:
                        item = LOOT[(hero_r, hero_c)]
                        if item not in found_loot:
                            found_loot.add(item)
                            print(f"Обнаружен объект: {item}. Найдено уникальных образцов: {len(found_loot)}.")
                else:
                    print(f"Маршрут {words[1]} недоступен: путь перекрыт или сектор заканчивается.")
            else:
                ammo = ammo - 2
                print("Ты пробираешься по поверхности планеты и расходуешь две энергоячейки на защитный импульс.")

        elif verb == "rest":
            sanity = sanity + 10
            print("Ты включаешь режим отдыха в скафандре. Заряд сканера постепенно восстанавливается.")

        elif verb == "listen":
            sanity = sanity - 15
            print("Ты запускаешь дальний сканер. В помехах появляется слабый сигнал: «Маяк находится за северным хребтом».")

        elif verb == "torch":
            ammo = ammo + 3
            print("В обломках посадочного модуля ты находишь запасные энергоячейки.")

        elif verb == "train":
            strikes = 6
            print("Ты подходишь к старому ржавому робот-охраннику на посту охраны.")
            print(f"Выполняется {strikes} тестовых импульсов.")
            total_damage = 0
            crit_count = 0
            for i in range(1, strikes + 1):
                hit_damage, crit = dungeon.hero_hit(i, damage, crit_damage)
                if crit:
                    crit_count += 1
                    print(f"Импульс {i}: {hit_damage:.1f} — усиленный!")
                else:
                    print(f"Импульс {i}: {hit_damage:.1f}")
                total_damage += hit_damage
            print(f"Проверка завершена: импульсов — {strikes}, усиленных — {crit_count}.")
            print(f"Суммарная мощность: {total_damage:.1f}")
            print(f"Средняя мощность импульса: {total_damage / strikes:.1f}")
            ammo = ammo - 1

        elif verb == "descend":
            if not enemies:
                print("В этом секторе больше не осталось обнаруженных угроз. Можно продолжить путь к маяку.")
            else:
                enemy = random.choice(enemies)
                rounds, won, health, loot = dungeon.fight(enemy, health, ability_bonus, damage, crit_damage)
                for r in rounds:
                    log.append(r)
                if won:
                    gold_total += loot
                    enemies.remove(enemy)

                    win_msg = f"Угроза «{enemy}» нейтрализована. Опасностей осталось: {len(enemies)}."
                    if COLOR:
                        print(Fore.YELLOW + win_msg + Style.RESET_ALL)
                    else:
                        print(win_msg)

                    print(f"Столкновение завершено за этапов: {len(rounds)}. Получено кредитов: {loot}.")

        elif verb == "leaders":
            print_leaderboard(log)

        elif verb == "shop":
            print("Торговый терминал:")
            for name, price in dungeon.prices.items():
                print(f"{name}: {price} кредитов")
            print("(Для покупки введи: buy <название> [количество])")

        elif verb == "backpack":
            if not inventory:
                print("Сумка исследователя пуста.")
            else:
                print("Снаряжение:")
                for name, qty in inventory.items():
                    print(f"{name}: {qty} ед.")

        elif verb == "buy":
            if len(words) > 1 and words[-1].isdigit():
                qty = int(words[-1])
                item = " ".join(words[1:-1])
            else:
                qty = 1
                item = " ".join(words[1:])

            if item == "":
                print("Что приобрести? Используй: buy <предмет>.")
                continue

            if item not in dungeon.prices:
                print("Терминал не распознаёт такой товар.")
                continue

            gold_total, ok = dungeon.buy(dungeon.prices[item], gold_total, quantity=qty)
            if ok:
                inventory[item] = inventory.get(item, 0) + qty
                print(f"Получено: {qty} ед. предмета «{item}». Списано кредитов: {dungeon.prices[item] * qty}. Баланс: {gold_total}.")
            else:
                print(f"Недостаточно кредитов: требуется {dungeon.prices[item] * qty}, доступно {gold_total}.")

        elif verb == "drink":
            item = " ".join(words[1:]) or "медпакет"
            if inventory.get(item, 0) == 0:
                print(f"В снаряжении отсутствует предмет: {item}.")
            else:
                if item == "медпакет":
                    health = min(health + 10, max_health)
                    print(f"Ты выпиваешь аптечку. Прочность костюма: {health}.")
                elif item == "усилитель":
                    ability_bonus += 2
                    print("Ты выпиваешь усилитель. Урон увеличен на 2!")
                else:
                    print(f"Использован объект: {item}.")
                inventory[item] -= 1
                if inventory[item] == 0:
                    del inventory[item]

        elif verb == "map":
            print("Карта исследованного сектора:")
            for i in range(len(MAP)):
                cells = []
                for j in range(len(MAP[i])):
                    cell = "@" if (i, j) == (hero_r, hero_c) else MAP[i][j]
                    cells.append(cell)
                print(" ".join(cells))

        elif verb == "scout":
            seen = set()
            count = scout(hero_r, hero_c, seen)
            print(f"Сканирование завершено. Доступных участков: {count}.")

        elif verb == "newgame":
            if os.path.exists("save.json"):
                os.remove("save.json")
            print("Данные прошлой миссии удалены. Подготовка новой экспедиции.")
            continue

        elif verb == "help":
            print("Команды управления: " + ", ".join(commands) + ".")
            print("Можно также вводить номера от 0 до 13.")

        elif verb == "exit":
            print("Ты завершаешь исследование и отправляешь отчёт на орбитальную станцию...")
            write_save()
            print("Данные экспедиции сохранены.")
            running = False

        else:
            print(f"Неизвестная команда: '{line.strip()}'. Введи 'help', чтобы увидеть список действий.")
            continue

        if verb not in ["exit", "rest", "shop", "backpack", "map", "scout", "newgame"]:
            health -= 2
            print("Экстремальный холод истощает скафандр... (-2 к прочности)")

        if health <= 0:
            print(f"\n{hero_name} больше не может продолжать миссию. Связь с исследователем потеряна...")
            if os.path.exists("save.json"):
                os.remove("save.json")
            running = False

        print()
        state = f"Прочность: {health:<3} Энергоячейки: {ammo:<3} Сканер: {sanity:<3} Угрозы: {len(enemies)} Кредиты: {gold_total}"
        if COLOR:
            print(Fore.GREEN + state + Style.RESET_ALL)
        else:
            print(state)
        print()

except KeyboardInterrupt:
    print("\n[Передача прервана]")
    write_save()
    print("Данные экспедиции сохранены.")

finally:
    print()
    print("=" * 23)
    print(f"Миссия завершена, {hero_name}. Циклов выполнено: {steps}")

    if inventory:
        print("Осталось снаряжения:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} ед.")
    else:
        print("Осталось снаряжения: ничего.")

    print_run_summary(log)
    print("=" * 23)
