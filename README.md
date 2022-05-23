# Python_FuzzyLogic
![Fuzzy_crisp-ru svg](https://user-images.githubusercontent.com/52812804/169823264-a1bc671d-7f54-4e2d-8408-c41b15b605ab.png)


# Opportunities:
- All available classes of fuzzy logic functions
- Also available to Gaussian func (3 parametrs)
- Quantifiers
- Comparison of sets
- Determination of properties and parameters of sets

# Instruction:
Enter sudo git clone in your terminal https://github.com/SniffSpoof/Python_FuzzyLogic or download the repository from the same link

In order to use the methods, first create an object of the fuzzy_set class:
your_fuzzy_set = fuzzy_logic.fuzzy_set(type = "Empty", U1 = None, U2 = None, a = None, b = None, c = None, epsilon = 1, U = None)
- Type - Class of the membership function, type String
- U1, U2 are the boundaries of the reasoning field (it is also a universal set) of type Int
- a,b,c - Parameters of the membership function, Float type
- epsilon - Precision, type Int. For example, epsilon = 3, Means precision 10^3
- U is a universal set, if a special one is required, of the list type

The methods are used as follows:
your_fuzzy_set.method(parameter1, parameter2, ...)
For a complete list of methods, see the documentation on https://github.com/SniffSpoof/Python_FuzzyLogic/documentation.txt

The graph is created as follows:
your_fuzzy_set.plot() or your_fuzzy_set.plot_scatter() if you need to output a set of points
Displaying a graph on the screen:
your_fuzzy_set.plot_show()

# TODO List:
- Determination of the remaining parameters and properties of the set
- Finish documentation
- Expand the list of methods
