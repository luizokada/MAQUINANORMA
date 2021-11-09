class reg():
    sinal: int
    magnitude: int

    def __init__(self, a) -> None:
        if a >= 0:
            self.sinal = 0
            self.magnitude = a
        else:
            self.sinal = 1
            self.magnitude = a * (-1)
        pass

    def igual(self, b):
        C = reg(0)
        self.magnitude = 0
        self.sinal = 0
        while(b.magnitude != 0):
            C.magnitude += 1
            self.magnitude += 1
            b.magnitude -= 1
        if b.sinal == 0:
            pass
        else:
            self.sinal += 1
        while(C.magnitude != 0):
            C.magnitude -= 1
            b.magnitude += 1


class numREAL():
    a: reg
    b: reg

    def __init__(self, a: reg, b: reg) -> None:
        self.a = a
        self.b = b
        pass

# SOMA A:=A+B


def soma(A: reg, B: reg):
    C = reg(0)

    while(B.magnitude != 0):
        C.magnitude += 1
        B.magnitude -= 1

    while(C.magnitude != 0):
        if B.sinal == 0:
            if A.sinal == 0:
                A.magnitude += 1
            else:
                A.magnitude -= 1
                if A.magnitude == 0:
                    A.sinal -= 1
                else:
                    pass
        else:
            if A.sinal == 0:
                if A.magnitude == 0:
                    A.sinal += 1
                    A.magnitude += 1
                else:
                    A.magnitude -= 1
            else:
                A.magnitude += 1
        C.magnitude -= 1
        B.magnitude += 1


# A:=A-B -3-3
def sub(A: reg, B: reg):
    C = reg(0)
    while(B.magnitude != 0):
        C.magnitude += 1
        B.magnitude -= 1

    while(C.magnitude != 0):
        if B.sinal == 0:
            if A.sinal == 0:
                if A.magnitude == 0:
                    A.sinal += 1
                    A.magnitude += 1
                else:
                    A.magnitude -= 1
            else:
                A.magnitude += 1

        else:  # -3-(-3)
            if A.sinal == 0:
                A.magnitude += 1
            else:
                A.magnitude -= 1
                if A.magnitude == 0:
                    A.sinal -= 1
                else:
                    pass

        C.magnitude -= 1
        B.magnitude += 1

# A:= A * B


def mut(A: reg, B: reg):
    E = reg(0)
    C = reg(0)
    D = reg(0)
    D.igual(A)
    A.magnitude = 0
    A.sinal = 0

    while(B.magnitude != 0):
        C.magnitude += 1
        B.magnitude -= 1
    while C.magnitude != 0:
        soma(E, D)
        C.magnitude -= 1
        B.magnitude += 1
    A.igual(E)
    if B.sinal == 0:
        pass
    else:
        if A.sinal == 0:
            A.sinal += 1
        else:
            A.sinal -= 1
    return A

# A = A / B


def div(A: reg, B: reg):
    C = reg(0)
    D = reg(0)
    E = reg(0)
    F = reg(0)
    if B.magnitude == 0:
        return
    else:
        while(A.magnitude != 0):
            C.magnitude += 1
            A.magnitude -= 1
        while(B.magnitude != 0):
            D.magnitude += 1
            B.magnitude -= 1
        F.magnitude += 1
        while(F.magnitude != 0):
            sub(C, D)  # C = C - D
            if C.sinal == 0:
                E.magnitude += 1
            else:
                F.magnitude -= 1

        if B.sinal == 0:
            if A.sinal == 0:
                pass
            else:
                E.sinal += 1
        else:
            if A.sinal == 0:
                E.sinal += 1
            else:
                pass
        A.igual(E)
        while(D.magnitude != 0):
            D.magnitude -= 1
            B.magnitude += 1
    return


def soma1(fracao: numREAL):
    C = reg(0)
    C.magnitude += 1
    X = reg(0)
    Y = reg(0)
    X.igual(fracao.a)
    Y.igual(fracao.b)
    XY = numREAL(X, Y)
    mut(C, fracao.b)
    soma(XY.a, C)
    return XY


def sub1(fracao: numREAL):
    C = reg(0)
    C.magnitude += 1
    X = reg(0)
    Y = reg(0)
    X.igual(fracao.a)
    Y.igual(fracao.b)
    XY = numREAL(X, Y)
    mut(C, fracao.b)
    sub(XY.a, C)
    return XY


def mutfrac(AB: numREAL, CD: numREAL):
    X = reg(0)
    Y = reg(0)
    Y.igual(AB.b)
    mut(C, CD.b)
    div(AB.a, C)
    div(CD.a, C)
    sum(AB.a, CD.a)


a = reg(1)
b = reg(2)
fracao = numREAL(a, b)
C = reg(4)
XY = sub1(fracao)
print("a")
