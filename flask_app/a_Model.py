import pickle
from sklearn.ensemble import RandomForestClassifier

def ModelIt(condition_ordinal, total_price, free_shipping, brand_included, description_length):
    features = [[condition_ordinal, total_price, free_shipping, brand_included, description_length]]
    loaded_model = pickle.load(open('flask_app/model.pkl', 'rb'))
    prediction = loaded_model.predict(features)
    return(prediction[0])
