from fastapi import FastAPI
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello This is Tanmay "}

@app.get("/test")
async def root():
    return {"message":"this is testing of code"}
    