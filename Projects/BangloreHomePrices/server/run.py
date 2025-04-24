import uvicorn

if __name__ == "__main__":
    print("Starting Python Flask server with uvicorn for home price prediction...")
    uvicorn.run("server:app", host="0.0.0.0", port=5000, reload=True) 