variable = "pastrami"
camelCase = "The best way to do anything"
python_nonsense = "You can also do it this way. How digusting."

dogBreeds = ["bulldog", "dalmatian", "shitzu", "labrador", "retriever", "boxer", "sheperd", "poodle"]
index = 0

while index < len(dogBreeds):
    print(dogBreeds[index])
    index += 1

def function(par1,par2):
  print(f"When you put in {par1}, you're probably not going to get {par2}")
function("salami","toast")

try: 
    5 / 0
except:
    print("You can't divide by 0, friend.")