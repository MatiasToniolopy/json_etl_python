import  json
import requests
import matplotlib.pyplot as plt


def fetch():
    url = 'https://api.mercadolibre.com/sites/MLA/search?category=MLA1459&q=Departamentos%20Alquilers%20Mendoza%20&limit=50'
    response = requests.get(url)
    data = response.json()
    js = data['results']
    
    dep_ars = [{"price":x["price"],"condition":x["condition"]} for x in js if x.get("currency_id")== 'ARS']
    
    return dep_ars

def transform(data1, min, max):
    precio_min = [{"price":x["price"]} for x in data1 if x.get('price')<=min]
    precio_med = [{"price":x["price"]} for x in data1 if min>x.get('price')<max]
    precio_max = [{"price":x["price"]} for x in data1 if x.get('price')>=max]
    
    total = [len(precio_min),len(precio_med),len(precio_max)]
    
    return total
   
def report(data2):
    grade = ('precio min', 'precio med', 'precio max')
    color = ['yellow', 'hotpynk', 'green']
    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle('PROMEDIO DE ALQUILERES', color = 'red')
    ax.pie(data2, labels = grade, radius = 1.3, autopct = '%0.f%%', explode = [0.1,0,0.1], shadow = True)
    plt.legend(title = 'Alquileres', loc= 4)
    plt.show()   
    



    
if __name__ == "__main__":
    
    min = 2000
    max = 9000
    data1 = fetch()
    data2 = transform(data1,min,max)
    graf = report(data2)
    print(graf)
    
    
