from freshsales import FreshsaleClient
import json

cliente = FreshsaleClient('app', api_key='yKcwqrwetdewqeSilp32j9TA')

crear = 0
if crear:
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
lead_id = None
response = cliente.search('l2radamanthys@gmail.com', 'lead,contact')
resultado = json.loads(response.content)
if len(resultado) > 0:
    lead = resultado[0]
    print(lead)
    lead_id = lead.get('id')
else:
    print("No Encontrado")
print()


print("Actualizando datos")
response = cliente.leads.update(id=lead_id, mobile_number='1234567')
print(json.loads(response.content))
print()

# response = cliente.leads.get(id='12012630583')
# print(json.loads(response.content))
# print()
