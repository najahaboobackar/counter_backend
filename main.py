from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import  Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Count(BaseModel):
    count:int
    
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.get("/count/")
async def last_count(db: Annotated[Session, Depends(get_db)]):
    db_count = db.query(models.Count).order_by(models.Count.id.desc()).first()
    if db_count is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_count   
@app.post("/count/")   
async def create_count(count:Count,db: Annotated[Session, Depends(get_db)]):
    db_count=models.Count(count=count.count)
    db.add(db_count)
    db.commit()
    db.refresh(db_count)
    return    