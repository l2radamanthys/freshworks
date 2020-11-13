from freshsales import FreshsaleClient
import json

cliente = FreshsaleClient('spiderinvestments', api_key='yKcVd8HSb8HHSilpxUj9TA')
response = cliente.search('l2radamanthys@gmail.com', 'lead,contact')
print(response.content)

response = cliente.leads.create(
    first_name='Ricardo',
    last_name='Quiroga',
    email='l2radamanthys@gmail.com',
    mobile_number='+543875764272'
)
print(response.content)
