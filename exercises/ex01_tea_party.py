"""Make a function to calculate the cost of a tea party"""

__author__: str = "730760430"


def main_planner(guests: int) -> None:
    """Creates the output of the function"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    # came into error about wrong data type, swtiched all outputs to string
    # another error about the printing cost function, i dont know how to introduce the tea/treat functions
    # I replaced the costs parameters with the two functions due to my previous reasoning back at the cost function, but it woudnt work for sometime, but now it does for some reason :)
    # fixed the spacing issues and added the dollar sign


def tea_bags(people: int) -> int:
    """Calculates number of teabags needed"""
    return people * 2


def treats(people: int) -> int:
    """Calculates number of treats needed"""
    # put type of function in front of call to create specfic return
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of both teabags and treats"""
    # im currently having trouble figuring this out, looking at practice
    # I kept trying to introduce the other function as the cost parameters because I thought the cost function was going to be the last function, but looking ahead I realize this is wrong
    return (tea_count * 0.5) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
