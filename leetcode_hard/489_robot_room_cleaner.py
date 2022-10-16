
class Robot:
    def move(self) -> bool:
        ...

    def turnLeft(self) -> bool:
        ...

    def turnRight(self) -> bool:
        ...

    def clean(self) -> None:
        ...


# Runtime: 72 ms, faster than 92.54% of Python3 online submissions for Robot Room Cleaner.
# Memory Usage: 15.6 MB, less than 60.25% of Python3 online submissions for Robot Room Cleaner.
class Solution:
    def cleanRoom(self, robot: 'Robot'):
        """
        :type robot: Robot
        :rtype: None
        """

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(x: int, y: int, direction):
            visited.add((x, y))
            robot.clean()

            # 0 represents going up
            # 1 -> going right
            # 2 -> going down
            # 3 -> going left
            for i in range(4):
                new_direction = (direction + i) % 4

                new_x = x + directions[new_direction][0]
                new_y = y + directions[new_direction][1]

                if (new_x, new_y) not in visited and robot.move():
                    backtrack(new_x, new_y, new_direction)
                    go_back()
                robot.turnRight()
        backtrack(0, 0, 0)
        return
