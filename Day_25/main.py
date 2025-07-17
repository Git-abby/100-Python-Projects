import pandas

data = pandas.read_csv("./2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data)

gray_Squirrels = len(data[data["Primary Fur Color"] == "Gray"])
black_Squirrels = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_Squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(F"Gray = {gray_Squirrels}\nBlack = {black_Squirrels}\nCinnamon = {cinnamon_Squirrels}")


data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_Squirrels, black_Squirrels, cinnamon_Squirrels]
}

# Convert data into DataFrame (CSV)
# print(data_dict)

df = pandas.DataFrame(data=data_dict)
df.to_csv("squirrels_counts.csv")