import gc
import sys

class Garbage:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} deleted")

def main():
    # Garbage yaratish
    g1 = Garbage("Garbage 1")
    g2 = Garbage("Garbage 2")

    # Garbage ni o'zgartirish
    g1.name = "New Garbage 1"

    # Garbage ni o'chirish
    del g2

    # Garbage ni o'chirish uchun buyurtma berish
    gc.collect()

    # Garbage ni o'chirish uchun buyurtma berish
    sys.getrefcount(g1)

if __name__ == "__main__":
    main()
```

```python
import gc
import sys

class Garbage:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} deleted")

def main():
    # Garbage yaratish
    g1 = Garbage("Garbage 1")
    g2 = Garbage("Garbage 2")

    # Garbage ni o'zgartirish
    g1.name = "New Garbage 1"

    # Garbage ni o'chirish
    del g2

    # Garbage ni o'chirish uchun buyurtma berish
    gc.collect()

    # Garbage ni o'chirish uchun buyurtma berish
    sys.getrefcount(g1)

if __name__ == "__main__":
    main()
