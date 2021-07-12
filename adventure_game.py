import story
from time import sleep
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)                                   # auto reset color of text after printing a line


def game_over():                                                # restart game option
    print(f"{Style.BRIGHT}Would you like to restart? "
          f"{Fore.GREEN}Enter y to restart. "
          f"{Fore.BLUE}Enter n to end game.\n", end="")
    restart = input()
    while restart not in ["y", "n"]:
        print(f"{Style.BRIGHT}{Fore.RED}"
              f"Please input one of the commands shown.\n", end="")
        restart = input()
    else:
        if restart == "y":
            start_game()
        else:
            print("Thanks for playing!")
            sleep(2.0)
            exit()


def on_screen_help():                                            # on-screen help
    print(f"{Style.BRIGHT}{Fore.YELLOW}"
          f"This is an onscreen help for The Island Escape. To play the game you simply enter the correct keys "
          f"indicated to you as you will be given a choice for each event")
    print(f"{Style.BRIGHT}{Fore.YELLOW}"
          f"In this text-based game you must type the correct input to prevent losing the game\n"
          f"{Fore.GREEN}H{Fore.BLUE}a{Fore.MAGENTA}v{Fore.CYAN}e {Fore.GREEN}f{Fore.BLUE}u{Fore.MAGENTA}n!\n")
    sleep(3.0)


on_screen_help()


def start_game():                                                 # game restarts from this point

    def indicate_exp():                                           # displays experience points earned
        print("You have", exp, "Experience points")
        sleep(2.0)

    exp = 0                                                       # experience points starting from 0
    print(f"{Fore.GREEN}Type in your adventurers name\n", end="")
    name = input()                                                # converts print to input function for colorama
    print("Welcome", name, "to The Island Escape")
    sleep(3.0)
    print("You currently possess:\n"
          f"{Fore.CYAN}A knife")
    sleep(3.0)

    story.chapter1()
    # event 1
    print(f"{Fore.GREEN}Enter s to sneak by. "
          f"{Fore.BLUE}Enter S to kill it. "
          f"{Fore.YELLOW}Enter h for hint:")
    event1 = input()
    while event1 not in ["s", "S"]:
        if event1 == "h":
            print(f"{Fore.YELLOW}Entering lowercase s is safer. Entering uppercase S grants more risk:\n", end="")
            event1 = input()
        else:
            print(f"{Fore.RED}Please input one of the commands shown.\n", end="")
            event1 = input()
    else:
        if event1 == "s":
            print("Carefully you edge past")
            exp = exp + 2
            sleep(2.0)
            print("You make it past the wolf")
        else:
            print("You confront the wolf and kill it")
            exp = exp + 1
            sleep(2.0)

    indicate_exp()

    story.chapter2()
    # event 2
    print(f"{Fore.GREEN}Enter p to take the gold:\n", end="")
    event2 = input()
    while event2 != "p":
        print(f"{Fore.RED}Please input the command shown.\n", end="")
        event2 = input()
    else:
        print("You take the gold and store it in your backpack but now the roof of the ice cave is crumbling.")
        sleep(3.0)

    story.chapter3()
    # event 3
    print(f"{Fore.GREEN}Enter 1 for the first route. "
          f"{Fore.BLUE}Enter 2 for the second route. "
          f"{Fore.YELLOW}Enter h for hint:\n", end="")
    event3 = input()
    while event3 not in ["1", "2"]:
        if event3 == "h":
            print(f"{Fore.YELLOW}Entering 1 could cause injury. Entering 2 could bring a worse fate:\n", end="")
            event3 = input()
        else:
            print(f"{Fore.RED}Please input one of the commands shown.\n", end="")
            event3 = input()
    else:
        if event3 == "1":
            print("You dash down route 1\n"
                  "You have injured you left leg and dropped your knife which will slow you down but you can still "
                  "manage to make your way out.")
            exp = exp + 2
            sleep(2.0)
        else:
            print("Route 2 was a dead end and you were killed by the ceiling collapsing on top of you.")
            sleep(2.0)
            print("GAME OVER YOU LOSE!")
            game_over()

    indicate_exp()

    story.chapter4()
    # event 4
    print(f"{Fore.GREEN}Enter t to wait for them to rush past. "
          f"{Fore.BLUE}Enter T try take them both on. "
          f"{Fore.YELLOW}Enter h for hint:\n", end="")
    event4 = input()
    while event4 not in ["t", "T"]:
        if event4 == "h":
            print(f"{Fore.YELLOW}Entering lowercase t makes you more vulnerable. Entering uppercase T gives you a "
                  f"chance at survival:\n", end="")
            event4 = input()
        else:
            print(f"{Fore.RED}Please input one of the commands shown.\n", end="")
            event4 = input()
    else:
        if event4 == "T":
            print("You manage to quickly rush two of the armed men and knock them down. You take one of their weapons "
                  "and made your way out of the cave as the roof collapses on top of them")
            exp = exp + 5
            sleep(2.0)
        else:
            print("You did not make it as the roof above collapsed")
            sleep(2.0)
            print("GAME OVER YOU LOSE!")
            game_over()

    indicate_exp()

    print("You now currently possess:\n"
          f"{Fore.CYAN}An assault rifle")
    sleep(3.0)

    story.chapter5()
    # event 5
    print(f"{Fore.GREEN}Enter k to shoot him down. "
          f"{Fore.BLUE}Enter K to try and choke hold the guard. "
          f"{Fore.YELLOW}Enter h for hint:\n", end="")
    event5 = input()
    while event5 not in ["k", "K"]:
        if event5 == "h":
            print(f"{Fore.YELLOW}Entering lowercase k could alert other guards. Entering uppercase K could result in "
                  f"a failed choke hold:\n", end="")
            event5 = input()
        else:
            print(f"{Fore.RED}Please input one of the commands shown.\n", end="")
            event5 = input()
    else:
        if event5 == "K":
            print("You manage to quietly choke hold the guard, however he breaks out and try to attack. Luckily your "
                  "assault rifle came in handy and you knock him out.")
            exp = exp + 5
            sleep(2.0)
        else:
            print("You shoot the guard down, alerting the other guards. You were unable to kill them all as you were "
                  "outnumbered")
            sleep(2.0)
            print("GAME OVER YOU LOSE!")
            game_over()

    indicate_exp()

    story.chapter6()
    # event 6
    print(f"{Fore.GREEN}Enter m to throw the knife at the guard. "
          f"{Fore.BLUE}Enter M to rush towards the boat. "
          f"{Fore.YELLOW}Enter h for hint:\n", end="")
    event6 = input()
    while event6 not in ["m", "M"]:
        if event6 == "h":
            print(f"{Fore.YELLOW}Entering lowercase m could grant you better equipment. Entering uppercase M leaves "
                  f"you vulnerable as you rush towards the boat:\n", end="")
            event6 = input()
        else:
            print(f"{Fore.RED}Please input one of the commands shown.\n", end="")
            event6 = input()
    else:
        if event6 == "m":
            print("The knife you threw manages to hit the guard, killing him. You get the knife back and find a "
                  "suppressed pistol equipped on him which should come in handy for your escape.")
            exp = exp + 5
            sleep(2.0)
        else:
            print("As you quickly head towards the boat, a guard awaits at a watchtower equipped with a suppressed "
                  "sniper rifle and manages to shoot you down.")
            sleep(2.0)
            print("GAME OVER YOU LOSE!")
            game_over()

    indicate_exp()

    print("You now currently possess:\n"
          f"{Fore.CYAN}"
          f"A suppressed pistol\n"
          "A knife")
    sleep(3.0)

    story.chapter7()
    # event 7
    print(f"{Fore.GREEN}Enter p to kill the guard with a knife. "
          f"{Fore.BLUE}Enter P to shoot the guard with the suppressed pistol. "
          f"{Fore.YELLOW}Hint unavailable:\n", end="")
    event7 = input()
    while event7 not in ["p", "P"]:
        print(f"{Fore.RED}Please input one of the commands shown.\n", end="")
        event7 = input()
    else:
        if event7 == "P":
            print("You managed to silently shoot the guard down with your suppressed pistol. You climb back down the "
                  "watchtower and manage to get to the boat")
            exp = exp + 10
            sleep(2.0)
            print("Congratulations, you have completed The Island Escape!\n"
                  "Total EXP earned:", exp)
            sleep(2.0)
            game_over()
        else:
            print("You take out the guard from behind with a knife. You then manage to climb down from the watchtower "
                  "and get to the boat to escape")
            exp = exp + 5
            sleep(2.0)
            print("Congratulations, you have completed The Island Escape!\n"
                  "Total EXP earned:", exp)
            sleep(2.0)
            game_over()


start_game()
