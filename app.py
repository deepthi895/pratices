from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class numbers(BaseModel):
    a:int
    b:int

@app.post("/add/")
def add_values(add:numbers):
    result=add.a+add.b
    return result

@app.post("/sub/")
def sub_values(sub:numbers):
    result=sub.a-sub.b
    return result

@app.post("/mul/")
def mul_values(mul:numbers):
    result=mul.a*mul.b
    return result

@app.post("/pow/")
def pow_values(pow:numbers):
    result=pow.a**pow.b
    return result

@app.post("/div/")
async def div_values(div:numbers):
    if div.b == 0 :
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    result=div.a / div.b
    return result

@app.post("/floor/")
def floor_values(floor:numbers):
    if floor.b == 0 :
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    result=floor.a // floor.b
    return result