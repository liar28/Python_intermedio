from DATA import DATA

def run():
    #comprehensions
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]
    all_Platzi_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]
 
    #High order functions
    adults = list(filter(lambda worker: worker["age"] > 18 ,DATA))
    adults = list(map(lambda worker: worker["name"], adults))
    old_peolpe = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))
 
    for worker in old_peolpe:
         print(worker)

    #filtrar trabajadores que usan Python
    devs = list(filter(lambda workers: workers["language"] == "python", DATA ))
    devs = list(map(lambda workers: workers["name"], devs))

    #filtrar trabajadores de Platzi
    Platzi = list(filter(lambda workers: workers["organization"] == "Platzi", DATA))
    Platzi = list(map(lambda workers: workers["name"], Platzi))
    
    #filtrar mayores de 18
    adult_devs = [workers["name"] for workers in DATA if workers["age"] > 18] 
    
    #agregar old : true/false a la lista
    old_people = [{**workers, **{'old': workers['age'] > 70}} for workers in DATA]   


    for workers in old_people:
        print(workers)

if __name__ == "__main__" : 
    run()