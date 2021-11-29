import pickle

def cat(category):
    if category == 'collar':
        return [1,0,0]
    elif category == 'harness':
        return [0,1,0]
    elif category == 'lead':
        return [0,0,1]
    else:
        return [0,0,0]
    
def siz(size):
    if size == 'L':
        return [1,0,0,0,0,0,0,0,0]
    elif size == 'M':
        return [0,1,0,0,0,0,0,0,0]
    elif size == 'M+L+XL':
        return [0,0,1,0,0,0,0,0,0]
    elif size == 'Normal':
        return [0,0,0,1,0,0,0,0,0]
    elif size == 'S':
        return [0,0,0,0,1,0,0,0,0]
    elif size == 'Slim':
        return [0,0,0,0,0,1,0,0,0]
    elif size == 'XL':
        return [0,0,0,0,0,0,1,0,0]
    elif size == 'XS':
        return [0,0,0,0,0,0,0,1,0]
    elif size == 'XS+S':
        return [0,0,0,0,0,0,0,0,1]
    else:
        return [0,0,0,0,0,0,0,0,0]


def prod(product):
    if product == 'Durango Collar':
        return [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Durango Harness':
        return [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Durango Harness':
        return [0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Guadalajara Collar':
        return [0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Guadalajara Harness':
        return [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Guadalajara Lead':
        return [0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Huatulco Collar':
        return [0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Huatulco Harness':
        return [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Huatulco Lead':
        return [0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Limited Edition Collar':
        return [0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Nayarit Collar':
        return [0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Nayarit Harness':
        return [0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Nayarit Lead':
        return [0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Oaxaca Collar':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Oaxaca Harness':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
    elif product == 'Oaxaca Lead':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]
    elif product == 'Sonora Collar':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
    elif product == 'Sonora Harness':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    elif product == 'Sonora Lead':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]
    elif product == 'Tulum Collar':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]
    elif product == 'Tulum Harness':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]
    elif product == 'Tulum Lead':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]
    elif product == 'Veracruz Collar':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    elif product == 'Veracruz Harness':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]
    elif product == 'Veracruz Lead':
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
    else:
        return [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
def sea(season):
    if  season == 'Fall':
        return [1,0,0,0]
    elif season == 'Spring':
        return [0,1,0,0]
    elif season == 'Summer':
        return [0,0,1,0]
    elif season == 'Winter':
        return [0,0,0,1]
    else:
        return [0,0,0,0]
    


def run_model(mylist):
    
    X_new = [mylist]
    
    with open('sales_model.pkl', 'rb') as file:
        sales_model = pickle.load(file)
        
    prediction = sales_model.predict(X_new)
    
    return prediction



print(prod('M'))

conc = cat('collar') + siz('M') + prod('Durango Collar') + sea('Fall')

print(run_model(conc))