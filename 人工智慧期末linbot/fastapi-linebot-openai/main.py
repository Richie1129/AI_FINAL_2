from app.Line import app
# from fastapi import FastAPI, HTTPException, Depends
# from sqlalchemy.orm import Session
# from app.postgresql import database, MedicationRecord, MedicationRecordDetail

# app = FastAPI()

# # Dependency to get the database session
# def get_db():
#     db = database.connect()
#     try:
#         yield db
#     finally:
#         db.disconnect()

# # Example route to create a new MedicationRecord
# @app.post("/medication_records/")
# async def create_medication_record(
#     redate: str,
#     pres_hosp: str,
#     db: Session = Depends(get_db)
# ):
#     # Parse redate to DateTime if needed
#     new_record = MedicationRecord(redate=redate, pres_hosp=pres_hosp)
#     db.add(new_record)
#     db.commit()
#     db.refresh(new_record)
#     return new_record

from fastapi import FastAPI, Depends
from sqlalchemy.orm import sessionmaker, Session
from datetime import datetime
from app.postgresql import create_tables, MedicationRecord, engine

app = FastAPI()

# 初始化資料表
create_tables()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 依賴注入，獲取資料庫session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 創建藥單記錄的API
@app.post("/medication_records/")
async def create_medication_record(redate: str, pres_hosp: str, db: Session = Depends(get_db)):
    redate_date = datetime.strptime(redate, "%Y-%m-%d").date()
    new_record = MedicationRecord(redate=redate_date, pres_hosp=pres_hosp)
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record




# from fastapi import FastAPI, Depends, HTTPException
# from sqlalchemy.orm import Session
# from datetime import datetime
# from pydantic import BaseModel

# app = FastAPI()

# # Pydantic 模型用於輸入驗證
# class MedicationRecordCreate(BaseModel):
#     redate: str
#     pres_hosp: str

# # 用於獲取數據庫會話的依賴
# def get_db():
#     db = database.session()
#     try:
#         yield db
#     finally:
#         db.close()

# # 用於創建新 MedicationRecord 的示例路由
# @app.post("/medication_records/")
# async def create_medication_record(
#     record_data: MedicationRecordCreate,
#     db: Session = Depends(get_db)
# ):
#     try:
#         # 解析 redate 為 DateTime
#         redate_datetime = datetime.strptime(record_data.redate, "%Y-%m-%d %H:%M:%S")

#         new_record = MedicationRecord(redate=redate_datetime, pres_hosp=record_data.pres_hosp)
#         db.add(new_record)
#         db.commit()
#         db.refresh(new_record)
#         return new_record
#     except Exception as e:
#         # 在發生異常時回傳 500 錯誤
#         raise HTTPException(status_code=500, detail=str(e))