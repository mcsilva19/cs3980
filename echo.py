# echo.py
def echo(text: str, repetitions: int = 3) -> str:
    """Imitate Real-World Echo"""
    for i in range(repetitions, 0, -1):
        print(text[-i:])
    print(".")

if __name__ == '__main__':
    text = input('Yell Something At A Mountain: ')
    echo(text)
