from numpy.linalg import det
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load

app = FastAPI()
model = load("house-pricing-model.pkl")

class HouseDetails(BaseModel):
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    mainroad: int
    guestroom: int
    basement: int
    hotwaterheating: int
    airconditioning: int
    parking: int
    prefarea: int
    furnishingstatus: int

features = ["area",     
"bedrooms",      
"bathrooms",     
"stories",       
"mainroad",      
"guestroom",     
"basement",      
"hotwaterheating",
"airconditioning",
"parking",       
"prefarea",      
"furnishingstatus"]

@app.get("/")
def root():
    return {"message": "House price prediction API - see /docs for usage"}

@app.post("/predict")
def predict(details: HouseDetails):
    detailsList = details.model_dump()
    houseDetailValues = [detailsList[key] for key in features]
    pred_price = model.predict([houseDetailValues])
    return {"predicted_price": float(pred_price[0])}

@app.get("/health")
def health():
    test_details = {
        "area": 7152, "bedrooms": 3, "bathrooms": 1, "stories": 2,
        "mainroad": 1, "guestroom": 0, "basement": 0, "hotwaterheating": 0,
        "airconditioning": 1, "parking": 0, "prefarea": 0, "furnishingstatus": 2
    }
    test_details_val_list = [test_details[key] for key in features]
    pred_price = model.predict([test_details_val_list])
    pred_price = float(pred_price[0])
    
    is_healthy = 100000 < pred_price < 20000000  # rough sane bounds for this dataset
    status = "ok" if is_healthy else "not ok"
    return {"status": status, "test_prediction": pred_price}
