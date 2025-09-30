import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer

def preprocess_student_data(df):
    # Handle missing values
    imputer = SimpleImputer(strategy='mean')
    df['GPA'] = imputer.fit_transform(df[['GPA']])
    
    # Encode categorical features
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    major_encoded = encoder.fit_transform(df[['Major']])
    df_encoded = pd.concat([df.drop('Major', axis=1),
                            pd.DataFrame(major_encoded, columns=encoder.get_feature_names_out())],
                           axis=1)
    
    # Scale numeric features
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_encoded)
    
    return pd.DataFrame(df_scaled, columns=df_encoded.columns)
