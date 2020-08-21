class Hash:
    def __init__(self):







    def __str__(self):
        pass




def _hash(self, key):
        p = 0
        for c in key:
            p = 31*p + ord(c)
        return p % self._size

def main():
    sfile = input()
    n = int(input())
    assert n > 0

    table,file_list = build_table(sfile, n)
    text_size = int(input())
    assert text_size > 0




main()