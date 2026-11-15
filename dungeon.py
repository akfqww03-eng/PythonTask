import random
prices = {"медпакет": 10, "энергоячейки": 15, "усилитель": 40}

enemy_stats = {
    "ледяной мутант": {"hp": 45, "damage": 6, "loot": 25},
    "робот-охранник": {"hp": 30, "damage": 4, "loot": 15},
    "песчаный хищник": {"hp": 20, "damage": 3, "loot": 10},
    "древний страж": {"hp": 12, "damage": 2, "loot": 5}
}


def hero_hit(strike_n, damage, crit_damage):
    if strike_n % 3 == 0:
        return crit_damage, True
    return damage, False


def fight(enemy, hero_health, bonus, damage, crit_damage):
    stats = enemy_stats[enemy]
    enemy_hp = float(stats["hp"])
    rounds = []
    round_n = 0

    print(f"Сканер фиксирует движение. На пути появляется {enemy}!")

    while enemy_hp > 0 and hero_health > 0:
        round_n += 1
        hit, crit = hero_hit(round_n, damage, crit_damage)
        hit += bonus
        enemy_hp -= hit

        line = f"Этап {round_n}: бластер наносит {hit:.1f} урона"
        if crit:
            line += " — усиленный импульс!"

        if enemy_hp <= 0:
            line += f" Противник {enemy} больше не представляет угрозы."
            rounds.append([round_n, hit, 0])
        else:
            blow = stats["damage"]
            hero_health -= blow
            line += f" Остаток прочности противника {enemy}: {enemy_hp:.1f}. Ответная атака наносит {blow} урона."
            rounds.append([round_n, hit, blow])

        print(line)
        print()

    won = enemy_hp <= 0
    loot = stats["loot"] if won else 0
    return rounds, won, hero_health, loot


def buy(price, gold, quantity=1):
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


if __name__ == "__main__":
    test_rounds, test_won, test_hp, test_loot = fight("робот-охранник", 100, 0, 20.5, 41.0)
    print(f"self-test: {len(test_rounds)} rounds, won={test_won}, loot={test_loot}")
