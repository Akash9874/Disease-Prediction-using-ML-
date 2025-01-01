import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from tensorflow.keras.models import Sequential # type: ignore
from tensorflow.keras.layers import Dense, Dropout # type: ignore
from tensorflow.keras.callbacks import EarlyStopping # type: ignore

# Load the training dataset
train_data = pd.read_csv('C:\\Users\\Akash Deep\\OneDrive\\Desktop\\disease prediction model\\data for gene\\train_genetic_disorders.csv')

# Drop unnecessary columns
columns_to_drop = ['Patient Id', 'Patient First Name', 'Family Name', 'Father\'s name', 
                   'Mother\'s age', 'Father\'s age', 'Institute Name']
X = train_data.drop(columns=columns_to_drop + ['Genetic Disorder'], axis=1)  # Features
y = train_data['Genetic Disorder']  # Target

# Fill missing values for numeric columns
numeric_columns = X.select_dtypes(include=['number']).columns
X[numeric_columns] = X[numeric_columns].fillna(X[numeric_columns].mean())

# Encode categorical features
categorical_columns = X.select_dtypes(include=['object']).columns
for col in categorical_columns:
    X[col] = LabelEncoder().fit_transform(X[col])

# Encode the target column
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Save the label classes for decoding predictions
np.save('C:\\Users\\Akash Deep\\OneDrive\\Desktop\\disease prediction model\\models\\classes.npy', label_encoder.classes_)

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Save the preprocessed data (optional but helpful for debugging)
np.save('C:\\Users\\Akash Deep\\OneDrive\\Desktop\\disease prediction model\\models\\X_train.npy', X_scaled)
np.save('C:\\Users\\Akash Deep\\OneDrive\\Desktop\\disease prediction model\\models\\y_train.npy', y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Save test data for later evaluation
np.save('C:\\Users\\Akash Deep\\OneDrive\\Desktop\\disease prediction model\\models\\X_test.npy', X_test)
np.save('C:\\Users\\Akash Deep\\OneDrive\\Desktop\\disease prediction model\\models\\y_test.npy', y_test)

# Build the neural network model
model = Sequential([
    Dense(128, input_dim=X_train.shape[1], activation='relu'),
    Dropout(0.3),
    Dense(64, activation='relu'),
    Dropout(0.3),
    Dense(32, activation='relu'),
    Dense(len(label_encoder.classes_), activation='softmax')  # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model with early stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

model.fit(X_train, y_train, validation_split=0.2, epochs=50, batch_size=32, callbacks=[early_stopping])

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
model.save('C:\\Users\\Akash Deep\\OneDrive\\Desktop\\disease prediction model\\models\\trained_model.keras')
print("Model training complete and saved.")
