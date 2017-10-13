# https://realpython.com/blog/python/inner-functions-what-are-they-good-for/

'''
def generate_power(number):
    """
    Examples of use:

    >>> raise_two = generate_power(2)
    >>> raise_three = generate_power(3)
    >>> print(raise_two(7))
    128
    >>> print(raise_three(5))
    243
    """

    # define the inner function ...
    def nth_power(power):
        return number ** power
    # ... which is returned by the factory function

    return nth_power
    '''