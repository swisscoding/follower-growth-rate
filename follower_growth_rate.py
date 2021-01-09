#!/usr/local/bin/python3
# Made by @swisscoding on Instagram

from colored import stylize, fg

# decoration
print(stylize("\n---- | Calculate follower growth rate | ----\n", fg("red")))

# class
class GrowthRate:
    def __init__(self, amount, new_amount):
        self.amount = amount
        self.new_amount = new_amount

    # output magic method
    def __repr__(self):
        rate = stylize(self.calculate_rate(self.amount, self.new_amount), fg("red"))
        period = input("Growth period in weeks: ")
        return f"\nGrowth rate of {period} week/s is {rate}%.\n"

    # methods
    def calculate_rate(self, amount, new_amount):
        difference = new_amount - amount

        return round(100 / amount * difference, 2)

# main execution
if __name__ == "__main__":
    # user interaction
    follower_count = int(input("Previous follower count: "))
    new_follower_count = int(input("New follower count: "))

    print(GrowthRate(follower_count, new_follower_count))
