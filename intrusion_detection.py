import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Placeholder dataset (replace later with real network traffic dataset)
data = {
    "packet_size": [50, 200, 400, 800, 1500],
    "is_suspicious": [0, 0, 1, 1, 1]
}
df = pd.DataFrame(data)

X = df[["packet_size"]]
y = df["is_suspicious"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
