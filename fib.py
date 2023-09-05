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
