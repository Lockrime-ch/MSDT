import pytest
from unittest.mock import Mock
from hero import Hero


@pytest.fixture()
def default_hero():
    return Hero('Lithiel', 120)


def test_damage_and_heal_below_max(default_hero):
    default_hero.damage(50)
    assert default_hero.heal(40) == 110


def test_damage_and_heal_above_max(default_hero):
    default_hero.damage(50)
    assert default_hero.heal(60) == 120


def test_damage_negative_amount(default_hero):
    with pytest.raises(ValueError, match='Cannot damage a hero for a non-positive amount'):
        default_hero.damage(-30)


def test_heal_dead_hero(default_hero):
    with pytest.raises(RuntimeError, match='Cannot heal a dead hero'):
        default_hero.damage(200)
        default_hero.heal(100)


def test_heal_revived_hero(default_hero):
    default_hero.damage(200)
    default_hero.revive()
    assert default_hero.heal(100) == 101


@pytest.mark.parametrize('initial_health, damage_amount, heal_amount, expected_health', [
    (100, 30, 40, 100),
    (300, 200, 10, 110),
    (0, 50, 60, 10)
])
def test_parametrized(initial_health, damage_amount, heal_amount, expected_health):
    if initial_health <= 0:
        with pytest.raises(ValueError, match='A hero must have at least 1 max health point'):
            hero = Hero('Corin', initial_health)
    else:
        hero = Hero('Corin', initial_health)
        hero.damage(damage_amount)
        assert hero.heal(heal_amount) == expected_health


@pytest.mark.parametrize('initial_health, damage_amount', [
    (100, 200),
    (20, 30),
    (50, 20)
])
def test_revive_parametrized(initial_health, damage_amount):
    hero = Hero('Korgus', initial_health)
    hero.damage(damage_amount)
    if hero.dead:
        hero.revive()
        assert hero.get_health() == 1
    else:
        with pytest.raises(RuntimeError, match='Cannot revive a living hero'):
            hero.revive()
