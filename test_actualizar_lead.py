from freshsales import FreshsaleClient
import json


# test crear
print("Creando Perfil")
response = cliente.leads.create(
    first_name='Ricardo',
    last_name='Quiroga',
    email='l2radamanthys@gmail.com',
    mobile_number='+543875764272',
    custom_field={"no_me_borres": True}
)
print(json.loads(response.content))
print()

# test buscar
print("Buscado Perfil")
cliente = FreshsaleClient('spiderinvestments', api_key='yKcVd8HSb8HHSilpxUj9TA')
response = cliente.search('l2radamanthys@gmail.com', 'lead,contact')
print(json.loads(response.content))
print()

print("Actualizando datos")
response = cliente.leads.update(id='12012630583', mobile_number='1234567')
print(json.loads(response.content))
print()

# response = cliente.leads.get(id='12012630583')
# print(json.loads(response.content))
# print()