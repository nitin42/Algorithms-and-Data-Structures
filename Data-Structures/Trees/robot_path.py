def Robot_Maze( Maze , position , N ):

    '''
    >>> Maze = [[ 1 , 0 , 1, 0 , 0], [ 1 , 1 , 0, 1 , 0],[ 0 , 1 , 0, 1 , 0],[ 0 , 1 , 0, 0 , 0],[ 1 , 1 , 1, 1 , 1]]
    >>> print Robot_Maze(Maze, (0,0), 5)
    [(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (4, 4)]

    '''

    # returns a list of the paths taken
    if position == ( N - 1 , N - 1 ): # If already present at the destination
        return [ ( N - 1 , N - 1 ) ]
    x , y = position
    if x + 1 < N and Maze[x+1][y] == 1: # If the path is having no obstacles and robot is moving forward
        a = Robot_Maze( Maze , ( x + 1 , y ) , N ) # recursively move forward and backtrack if there are any obstacles
        if a != None:
            return [ (x , y ) ] + a # Destination position 

    if y + 1 < N and Maze[x][y+1] == 1: # Path with no obstacles and robot is moving downward
        b = Robot_Maze( Maze , (x , y + 1) , N )
        if  b != None:
            return [ ( x , y ) ] + b


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)