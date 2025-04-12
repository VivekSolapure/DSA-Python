class Math:
    def add(self, a, b=0):  # Default argument
        return a + b
    def add(self, a, b,c):  # Default argument
        return a + b+c
math=Math()
print(math.add(1,2))