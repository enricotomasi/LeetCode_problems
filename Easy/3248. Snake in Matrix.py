class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x = 0
        y = 0

        for it in commands:
            if it == 'UP':
                x -= 1
            elif it == 'DOWN':
                x += 1
            elif it == 'RIGHT':
                y += 1
            else:
                y -= 1

        return (n * x) + y
