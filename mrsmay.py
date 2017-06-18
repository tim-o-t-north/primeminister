def mrs_may():
    """
    A subroutine simulation of the UK Prime-Minister
    Teresa May.
    For further help see
    https://en.wikipedia.org/wiki/Satire
    """
    print "Hello, I am your Prime-Minister"
    counter = 0
    while counter < 3:
        answer = raw_input("Did you want to ask me somthing?  ")
        print "Strong and Stable"
        counter += 1
    print "Brexit Means Brexit!"
    raise TypeError("Tautology error: 'Brexit Means Brexit is undefined")


if __name__ == "__main__":
    mrs_may()
