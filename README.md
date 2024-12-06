# Marketing Campaign Response Prediction

## Hackathon MD4 - Group 2

**Team Members:**
- [Abdessamad Touzani](https://github.com/AbdessamadTzn/)
- [Djamel Ouazar](https://github.com/legb78)
- [JC Emmanuel Mopeno-Bia](https://github.com/claude-morningstar47)
- [Amine Hamouma](https://github.com/HamoumaAmine)

This project is designed for predicting marketing campaign responses.

---

## To Use the App to Predict Your Models Step-by-Step:

### Prerequisites:
1. **Git** installed on your laptop.
2. **Virtualenv** installed on your laptop (You can install it from [here](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/).
3. Basic coding knowledge.
4. Your trained **model** (You should save it after training; in my case, it was a `.pkl` file, saved using `joblib`).
5. **Joblib** installed (You can install it using `pip install joblib`, or `!pip install joblib` in Jupyter Notebooks).

---

### How to Save Your Model:
After training your model, you can save it like this:

```python
import joblib
joblib.dump(model, 'modelname.pkl')  # Save the model for the repo
```

### Steps to Set Up the Application::
1. Fork the repository.
2. Clone the Repository to your local machine.
3. Create a Virtual Environment:
```
virtualenv envname
```
4. Activate the Virtual Environment:
```
For windows: envname\Scripts\activate
to deactivate: deactivate
```
5. Install Dependencies from the requirements.txt file:

```
pip install -r requirements.txt
```
6. Add the models folders & add your model to it
7. Make necessary changes to adapt it to your model's name and variables.
8. Run the Flask App:
```
python app.py
```
---

## For Dashboard:
You can visit the Power BI Dashboard at the following link:
[Marketing Dashboard](#)




