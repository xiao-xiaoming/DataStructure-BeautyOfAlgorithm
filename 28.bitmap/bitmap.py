class Bitmap:
    def __init__(self, nbits: int):
        self.nbits = nbits
        self.bytes = bytearray((nbits >> 3) + 1)

    def setbit(self, k: int) -> None:
        if k > self.nbits or k < 1: return
        self.bytes[k >> 3] |= (1 << k % 8)

    def getbit(self, k: int) -> bool:
        if k > self.nbits or k < 1: return False
        return self.bytes[k >> 3] & (1 << k % 8) != 0


if __name__ == "__main__":
    bitmap = Bitmap(10)
    bitmap.setbit(1)
    bitmap.setbit(3)
    bitmap.setbit(6)
    bitmap.setbit(7)
    bitmap.setbit(8)

    for i in range(1, 11):
        print(i, bitmap.getbit(i))
