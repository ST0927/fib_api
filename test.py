import unittest

def fibonacci(n):
    if n <= 0:
        raise ValueError("nは正の整数を入力してください")
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
try:
    n = int(input("nを入力してください: "))
    result = fibonacci(n)
    print(f"{n}番目のフィボナッチ数は {result} です")
except ValueError as ve:
    print(f"nは正の整数を入力してください: {ve}")
except RecursionError:
    print("計算が深すぎます。nの値を小さくしてください。")
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")

class TestFibonacci(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            fibonacci(0)
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(0.5)
        with self.assertRaises(ValueError):
            fibonacci(あ)
