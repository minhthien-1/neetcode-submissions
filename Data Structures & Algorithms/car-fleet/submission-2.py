class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        box = []
        cars = list(zip(position,speed))
        sort_cars = sorted(cars,reverse=True)
        for p, s in sort_cars:
            time = (target-p)/s
            box.append(time)
            if len(box)>=2 and box[-1] <= box[-2]:
                box.pop()
        return len(box)