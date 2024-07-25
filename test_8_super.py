class A:
    cmd = "whoami"

    def vuln(self, a: str):
        return eval(a)

    def __str__(self):
        return str(self.vuln(self.cmd))


class B(A):
    def __init__(self):
        self.cmd = input()

    def __str__(self):
        return super().__str__()


str(B())
