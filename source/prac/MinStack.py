class MinStack:

    def __init__(self):
        """
        self._vals contains the values
        self._mins[i] contains the minimum value of self._vals[:i]
        """
        self._vals = []
        self._mins = []
        
    def push(self, val: int) -> None:
        """
        push the val onto self._vals
        push the smaller of the new val, or the old min onto self._mins
        """
        self._vals.append(val)
        m = val if not self._mins else min(val, self._mins[-1])
        self._mins.append(m)
        

    def pop(self) -> None:
        """
        Removes the element last pushed onto the stack
        LeetCode / Java convention to have pop not return anything
        Separation of concerns (top peeks, pop mutates)
        """
        if not self._vals:
            raise IndexError("pop from empty MinStack")
        self._vals.pop()
        self._mins.pop()


    def top(self) -> int:
        """
        Return the last value pushed onto the MinStack
        Do not mutate the MinStack
        """
        if not self._vals:
            raise IndexError("top from empty MinStack")
        return self._vals[-1]

    def getMin(self) -> int:
        """
        Return the smallest value currently present in the MinStack
        Does not mutate the MinStack
        """
        if not self._mins:
            raise IndexError("getMin from empty MinStack")
        return self._mins[-1]

Solution = MinStack
