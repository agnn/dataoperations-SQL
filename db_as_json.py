import pandas as pd

f = pd.read_excel("F:\ineuron FSDS\pandas practice\data fsds\Attribute DataSet.xlsx")
f.to_json("attribute.json")
g = pd.read_json(r"C:\Users\agnik\attribute.json")