# tasks/task1.py



def solve():
# Ниже пишите решение задачии(Обязательно поставьте четыре пробела после функции Solve())
    ves=float(input("Введите ваш вес в КГ: "))
    rost=float(input("Введите ваш рост в Метрах: "))
    BMI=ves/(rost**2)
    print("Ваш BMI: ", BMI)
   

# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()