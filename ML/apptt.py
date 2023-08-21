import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

# Cargar el DataFrame
df = pd.read_csv("C:\Users\Leo\Desktop\API_ML\Csv_Proyecto_Terminado.csv")

# Seleccionar características (X) y etiquetas (y)
X = df[["stars_x", "nltk_stars", "Alcohol", "Ambience", "BikeParking",
        "BusinessAcceptsCreditCards", "BusinessParking", "Caters", "DogsAllowed",
        "DriveThru", "GoodForKids", "GoodForMeal", "HasTV", "NoiseLevel",
        "OutdoorSeating", "RestaurantsAttire", "RestaurantsDelivery",
        "RestaurantsGoodForGroups", "RestaurantsPriceRange2",
        "RestaurantsReservations", "RestaurantsTableService", "RestaurantsTakeOut",
        "WheelchairAccessible", "WiFi"]]  
y = df['promedio']  

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Crear y entrenar el modelo RandomForestRegressor
model_forest = RandomForestRegressor(n_estimators=305, max_depth=60, min_samples_split=20, max_features=37)
model_forest.fit(X_train, y_train)

# Función para predecir con el modelo
def predict_price(features):
    prediction = model_forest.predict([features])
    return prediction

def main():
    st.title("Predicción de Precio con RandomForestRegressor")
    
    # Obtener las características del usuario
    feature1 = st.sidebar.selectbox("stars_x", [0, 1])
    feature2 = st.sidebar.selectbox("nltk_stars", [0, 1])
    feature3 = st.sidebar.selectbox("Alcohol", [0, 1])
    feature4 = st.sidebar.selectbox("Ambience", [0, 1])
    feature5 = st.sidebar.selectbox("BikeParking", [0, 1])
    feature6 = st.sidebar.selectbox("BusinessAcceptsCreditCards", [0, 1])
    feature7 = st.sidebar.selectbox("BusinessParking", [0, 1])
    feature8 = st.sidebar.selectbox("Caters", [0, 1])
    feature9 = st.sidebar.selectbox("DogsAllowed", [0, 1])
    feature10 = st.sidebar.selectbox("DriveThru", [0, 1])
    feature11 = st.sidebar.selectbox("GoodForKids", [0, 1])
    feature12 = st.sidebar.selectbox("GoodForMeal", [0, 1])
    feature13 = st.sidebar.selectbox("HasTV", [0, 1])
    feature14 = st.sidebar.selectbox("NoiseLevel", [0, 1])
    feature15 = st.sidebar.selectbox("OutdoorSeating", [0, 1])
    feature16 = st.sidebar.selectbox("RestaurantsAttire", [0, 1])
    feature17 = st.sidebar.selectbox("RestaurantsDelivery", [0, 1])
    feature18 = st.sidebar.selectbox("RestaurantsGoodForGroups", [0, 1])
    feature19 = st.sidebar.selectbox("RestaurantsPriceRange2", [0, 1])
    feature20 = st.sidebar.selectbox("RestaurantsReservations", [0, 1])
    feature21 = st.sidebar.selectbox("RestaurantsTableService", [0, 1])
    feature22 = st.sidebar.selectbox("RestaurantsTakeOut", [0, 1])
    feature23 = st.sidebar.selectbox("WheelchairAccessible", [0, 1])
    feature24 = st.sidebar.selectbox("WiFi", [0, 1])
    
    # Botón para realizar la predicción
    if st.sidebar.button("Realizar Predicción"):
        user_features = [feature1, feature2, feature3, feature4, feature5,
                         feature6, feature7, feature8, feature9, feature10,
                         feature11, feature12, feature13, feature14, feature15,
                         feature16, feature17, feature18, feature19, feature20,
                         feature21, feature22, feature23, feature24]
        prediction = predict_price(user_features)
        st.write(f"La predicción de precio es: {prediction[0]}")

if __name__ == "__main__":
    main()
