from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/dexcom-data")
async def receive_data(request: Request):
    data = await request.json()
    print("Received data:", data)
    return {"status": "success"}
