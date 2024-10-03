# FastAPIの読み込み
from fastapi import FastAPI
from pydantic import BaseModel

from model.db.HistoryDate import HistoryDate

import math

class TaxIn(BaseModel):
    price: int
    item: str = None
    tax_rate: float

# FastAPIのインスタンスを作成
app = FastAPI()

# getメソッドで、/にアクセスした時の処理を記述
@app.get("/")
# asyncで*非同期処理を行う
# *あるタスクを実行している最中に、実行中のタスクを止めることなく、別のタスクを実行できる
async def hello():
    return {"text": "Hello World!"}

# getメソッドで、/TaxEx/{price}にアクセスした時の処理を記述
@app.get("/TaxEx/{price}")
async def TaxEx(price: int, item: str = None):
    if item:
        return {"text": f"{item}は{price}円"}
    return {"text": f"何かが{price}円"}

# postメソッドで、/にアクセスした時の処理を記述
@app.post("/TaxIn")
async def TaxIn(data: TaxIn):
    in_tax_cost = math.ceil(data.price * (1 + data.tax_rate))
    return {"text": f"{data.item}は{in_tax_cost}円(税込み)"}