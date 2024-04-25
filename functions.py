names = ["mark", "Aggrey", "Duku", "Benjamin"]
for name in names:
    print(name)
# Output: mark Aggrey Duku Benjamin
for name in range(len(names)):
    print(names[name])
# Output: mark 0 Aggrey 1 Duku 2 Benjamin 3</s

halls = {
    "duku":"lumumba",
    "Benjamin":"Livingstone",
    "mark":"Mitchell",
    "Aggrey":"Nsibiwa",
    "Caden" :"Africa",
    "Esther" :"Complex"
}
print(halls) # Output: Dictionary
print(halls["mark"]) # Output: Mitchell

if "Duku" in halls.keys():
    print(halls["duku"])# Output: lumumba
else:
    print(halls["Benjamin"])# Output: Livingstone
