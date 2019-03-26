import csv
list1 = [
    ["トップガン","リスキービジネス","マイノリティレポート"],
    ["タイタニック","ザ･レベネント","インセプション"],
    ["トレーニングデイ","マンオンファイア","フライト"]
]

with open("st.csv","w",newline="") as f:
    w = csv.writer(f,delimiter=",")
    for i in list1:
        w.writerow(i)
        
