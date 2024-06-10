from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

## STUDENT INFORMATION USING FASTAPI

class students(BaseModel):
    name:str
    branch:str
    emailid:str=None
    id :int

@app.post("/info/")
async def students_info(info:students):
    return info