from fastapi import FastAPI

app = FastAPI()


@app.post('/calculator/{a}/{b}/{sign}')
def calculate(a: float, b: float, sign: str = ''):
    if sign == '+':
        return (a + b)
    elif sign == '-':
        return (a - b)
    elif sign == '*':
        return (a * b)
    elif sign == '%' and b != 0:
        return (a / b)
