#faila atvēršana, nolasīšana
with open("Python/fails.txt") as file:
    persons=file.readlines()
    print(persons)
    #['marcis miscenkovs\n', 'toms kurtiss']
    for i in range(len(persons)):
        persons[i]=persons[i].replace("\n","")
    print(persons)
    # ['marcis miscenkovs', 'toms kurtiss']
    persons.sort(reverse=True)
    print(persons)
    # ['toms kurtiss', 'marcis miscenkovs']
    words=[]
    for line in persons:
        words+=line.split()
    print(words)
    # ['toms', 'kurtiss', 'marcis', 'miscenkovs']

with open("Python/fails.txt", "w") as file:
    file.write("sis ir jauns fails")