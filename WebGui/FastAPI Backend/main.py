from fastapi import FastAPI
from routers import connection, signal
import uvicorn
app = FastAPI(
  title="SEL Fault Signal Generator API",
  description="Backend to link custom Fault Signal Generator React GUI to custom hardware stack",
  version='0.1.0',
  docs_url='/'
)

app.include_router(connection.router)
app.include_router(signal.router)

if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=5000)