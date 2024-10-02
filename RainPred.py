import numpy as np

train_data = np.array([
    [30, 85, 1],
    [25, 65, 0],
    [35, 70, 1],
    [20, 50, 0],
    [40, 90, 1],
    [18, 55, 0]
])

test_data = np.array([
    [32, 80, 1],
    [27, 60, 0],
    [37, 75, 1],
    [62, 55, 0]
])

X_train = train_data[:, :-1]
y_train = train_data[:, -1]

X_test = test_data[:, :-1]
y_test = test_data[:, -1]

mean_rain = X_train[y_train == 1].mean(axis=0)
var_rain = X_train[y_train == 1].var(axis=0)

mean_no_rain = X_train[y_train == 0].mean(axis=0)
var_no_rain = X_train[y_train == 0].var(axis=0)

prob_rain = np.sum(y_train == 1) / len(y_train)
prob_no_rain = np.sum(y_train == 0) / len(y_train)

def gaussian_probability(x, mean, var):
    exponent = np.exp(-((x - mean) ** 2) / (2 * var))
    return (1 / np.sqrt(2 * np.pi * var)) * exponent

def predict(X_new):
    likelihood_rain = gaussian_probability(X_new[0], mean_rain[0], var_rain[0]) * \
                      gaussian_probability(X_new[1], mean_rain[1], var_rain[1])

    likelihood_no_rain = gaussian_probability(X_new[0], mean_no_rain[0], var_no_rain[0]) * \
                         gaussian_probability(X_new[1], mean_no_rain[1], var_no_rain[1])

    posterior_rain = likelihood_rain * prob_rain
    posterior_no_rain = likelihood_no_rain * prob_no_rain

    return 1 if posterior_rain > posterior_no_rain else 0

def accuracy(X_data, y_data):
    correct = 0
    for i in range(len(X_data)):
        prediction = predict(X_data[i])
        if prediction == y_data[i]:
            correct += 1
    return correct / len(X_data)

train_accuracy = accuracy(X_train, y_train)
print(f"Training Accuracy: {train_accuracy * 100:.2f}%")

test_accuracy = accuracy(X_test, y_test)
print(f"Test Accuracy: {test_accuracy * 100:.2f}%")

X_new = np.array([33, 80])
result = 'High chances of Rain' if predict(X_new) == 1 else 'No Rain'
print(f"Prediction for Temperature = {X_new[0]}, Humidity = {X_new[1]}: {result}")
