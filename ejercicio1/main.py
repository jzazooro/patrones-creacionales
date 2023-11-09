from abstract import *
from read import *
from clientela import *

def main():
    print("Factoria 1")
    cliente(Factoria1())
    print("Factoria 2")
    cliente(Factoria2())

if __name__ == "__main__":
    main()