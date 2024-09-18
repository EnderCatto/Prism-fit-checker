if __name__ == '__main__':
    # Ask the user for the dimensions of the rectangular prism
    print('Enter the first dimension of the prism:')
    prismHeight = input()
    print('Enter the second dimension of the prism:')
    prismWidth = input()
    print('Enter the third dimension of the prism:')
    prismDepth = input()  # prismDepth = beam length

    # Ask the user for the dimensions of the rectangular hole
    print('Enter the first dimension of the rectangular hole:')
    holeHeight = input()
    print('Enter the second dimension of the rectangular hole:')
    holeWidth = input()

    textFits = 'The prism fits through the hole'
    textDoesNotFit = 'The prism does not fit through the hole'

    # Sort the dimensions from smallest to largest
    prism_sides_list = sorted([prismHeight, prismWidth, prismDepth])

    min_prism_side = prism_sides_list[0]
    mid_prism_side = prism_sides_list[1]

    # Find the smallest and largest sides of the hole
    min_hole_side = min(holeWidth, holeHeight)
    max_hole_side = max(holeWidth, holeHeight)

    # Check if the two smallest dimensions of the prism fit through the hole
    if (min_prism_side <= min_hole_side) and (mid_prism_side <= max_hole_side):
        print(textFits)
    else:
        print(textDoesNotFit)
