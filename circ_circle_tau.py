# Created by Dylan Melo
# Created on November 2021
# This program asks the user for the radius of
# a circle in mm. It then calculates and displays
# the circumference using tau.
import constants


def main():
    # input
    radius = float(input("Enter the radius of the circle (cm) "))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference = {} cm".format(circumference))


if __name__ == "__main__":
    main()
