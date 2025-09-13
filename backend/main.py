from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello!"}


def main():
    print("Hello from backend!")
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == "__main__":
    main()
