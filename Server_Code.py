from fastapi import FastAPI, Path

app = FastAPI()

inventory = {
    1: {
        'Name': 'Milk',
        'Price': 60,
        'Quantity': 1,
        'Brand': 'Mother Dairy'
    }
}

@app.get('/get_item/{item_id}')
def get_item(item_id: int = Path(description="Item Number should be Integer"), gt=0):
    if item_id <= gt:
        return {"error": "Item ID must be greater than 0"}
    else:
        return inventory[item_id]


@app.get('/get_item_by_name')
def get_item(name:str):
   for item_id in inventory:
       if inventory[item_id]["Name"] == name:
           return inventory[item_id]

   return {"Data": "Not found"}
