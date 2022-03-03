from monty_hall import MontyHallSimulator, Statistics


def printer(title: str, stat: Statistics) -> None:
    print(title)
    print(f'Overall: {stat.overall}')
    print(f'Wins: {stat.wins} Loses: {stat.loses}')
    print(f'Win ratio: {stat.win_ratio} Lose ratio: {stat.lose_ratio}\n')


def main():
    monty_hall = MontyHallSimulator()
    monty_hall.startup()
    stat_without_changes = monty_hall.get_statistics()
    printer(title='STATISTICS WITHOUT CHANGING DECISION', stat=stat_without_changes)

    monty_hall.reset_attributes()
    monty_hall.switch_mode()

    monty_hall.startup()
    stat_with_changes = monty_hall.get_statistics()
    printer(title='STATISTICS WITH CHANGING DECISION', stat=stat_with_changes)


if __name__ == '__main__':
    main()
