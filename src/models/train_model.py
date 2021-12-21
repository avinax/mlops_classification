from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle
from src.data import read_data

def model_train():
    # get data
    df = read_data()
    print(df.columns)

    # choose features
    features = ["bedrooms","bathrooms","sqft_living","sqft_above","grade",
                "floors","view",'sqft_lot','floors','waterfront','zipcode'] 

    # getting those features from the dataframe
    x = df[features]
    y = df["price"]

    # splits data into 80% train 20% test
    x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.7, 
                                                        random_state=3)

    # choose model with settings
    model = RandomForestRegressor(n_estimators=100) 
    model.fit(x_train, y_train)
    with open('C:/Users/Avinash/classification/models/model_pkl', 'wb') as files:
        pickle.dump(model, files)

