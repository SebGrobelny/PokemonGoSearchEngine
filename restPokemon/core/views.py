from django.shortcuts import render
from django.conf import settings

import json, requests

from .forms import SubmitEmbed

def get_pokemon(request):
    

    input1 = ' '


    context = { 'name': ' ', 'height': ' ', 'weight': ' ', 'image': ' ', 'all_abilities' : ' ', 'status_code': ' '}
    image_url = ' '
    
    if request.method == "POST":
    #
        if request.POST['input'] :
            name = request.POST['input']
            r =  requests.post('http://pokeapi.co/api/v2/pokemon/'+name)
           
            if r.status_code == 200 :
                
                text = r.json()

                if 'name' in text : 
                    image_url = 'http://www.pokestadium.com/sprites/xy/'+str(text['name'])+'.gif'

                    abilities = {}

                    abilities = text['abilities']

                    ability_names = ' '

                    for i in range(0,len(abilities)):
                         ability = abilities[i]['ability']

                         ability_names+=str(ability['name'])

                         if(i < len(abilities)-1):
                            ability_names += ', '
                         # ability_names+='\n'

                    types = text['types']

                    type_names = ' '

                    for i in range(0,len(types)):
                        poke_type = types[i]['type']

                        type_names+=str(poke_type['name'])
                        if(i < len(types)-1):
                            type_names+=', ' 
                    
                    context =   { 'name': str(text['name']), 'height': str(text['height']), 'weight': str(text['weight']), 'image' : image_url, 'abilities' : ability_names, 'types' : type_names }
               
                else:
                    context = {'error_message': 'Please Enter a Valid Pokemon'}
            else :
                context = {'error_message': 'Please Enter a Valid Pokemon'}

    #context = {'name': text}
    return render(request, 'index.html', context)


