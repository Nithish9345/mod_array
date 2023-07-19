class ModArray:
    def mod(self, array, b):
        ans = 0
        power = 1
        for i in range(1, len(array)+1):

            ans = ans + ((array[-i] % b) * power) % b
            power = (power*10) % b

        return ans % b

array = list(map(int, input().split()))
b = int(input())
object = ModArray()
print(object.mod(array, b))




