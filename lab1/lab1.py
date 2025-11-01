import math


def GetCoefficient(printCoeff):
    coef = 0
    print(printCoeff)
    try:
        coef = float(input())
    except ValueError:
        print("Введено не число")
    return coef



def GetRoots(a, b, c):

    result = []
    D = b*b - 4*a*c
    if D == 0.0:
        root = -b / (2.0*a)
        result.append(root)
    elif D > 0.0:
        sqD = math.sqrt(D)
        root1 = (-b + sqD) / (2.0*a)
        root2 = (-b - sqD) / (2.0*a)
        result.append(root1)
        result.append(root2)
    return result


def main():

    a = GetCoefficient('Введите коэффициент А:')
    b = GetCoefficient('Введите коэффициент B:')
    c = GetCoefficient('Введите коэффициент C:')
    roots = GetRoots(a,b,c)
    lenRoots = len(roots)
    if lenRoots == 0:
        print('Нет корней')
    elif lenRoots == 1:
        print('Один корень: ', roots[0])
    elif lenRoots == 2:
        print('Два корня: ', roots[0], roots[1])



if __name__ == "__main__":
    main()
