[![CircleCI](https://circleci.com/gh/Anssikka/Reaktor-Junior-Pre-assignment.svg?style=svg)](https://circleci.com/gh/Anssikka/Reaktor-Junior-Pre-assignment)
[![Netlify Status](https://api.netlify.com/api/v1/badges/2ca78ed5-988e-4912-b0ab-2284019d67cc/deploy-status)](https://app.netlify.com/sites/eloquent-rosalind-cfa21a/deploys)
# [Reaktor Pre-assignment for junior developers](https://www.reaktor.com/junior-dev-assignment/)

## hosted on: 
<https://eloquent-rosalind-cfa21a.netlify.com/index.html>

## How to run:
1. Clone the repository
```
git clone git@github.com:Anssikka/Reaktor-Junior-Pre-assignment.git
```
3. Navigate to the folder
4. Replace status.real on the root folder with your own or on line 11 on parseri.py replace 'status.real' with the absolute path to your systems status.real.  
5. Run parseri.py with python
```
python3 parseri.py
```

## How to run tests:
1. Create a python virtual environment python
```
python3 -m venv venv
```
2. Activate the venv on windows with: 
```
venv\Scripts\activate.bat
``` 
or on linux/Mac 
```
source venv/bin/activate
```
3. Install dependencies with
```
pip install -r requirements.txt
```
4. Run pytest
```
pytest
```

## Made with:
Python that generates html and css.