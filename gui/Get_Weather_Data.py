'''
Created on 2017年5月26日

@author: Todd
'''

weather_data_tags_dict = {
     'observation_time': ''
    ,'weather': ''
    ,'temp_f':''
    ,'temp_c':''
    ,'dewpoint_f':''
    ,'dewpoint_c':''
    ,'relative_humidity':''
    ,'wind_string':''
    ,'visibility_mi':''
    ,'pressure_string':''
    ,'pressure_in':''
    ,'location':''
    }
# import urllib.request
from urllib import request

def get_weather_data(station_id='KLAX'):
    url_general = 'http://www.weather.gov/xml/current_obs/{}.xml'
    url = url_general.format(station_id)
    print(url)
    with request.urlopen(url) as f:
    
        content = f.read().decode()
    #     print(content)
        import xml.etree.ElementTree as ET
        xml_root = ET.fromstring(content)
    #     print('xml_root: {}\n'.format(xml_root.tag))
    
        for data_point in weather_data_tags_dict.keys():
            weather_data_tags_dict[data_point] = xml_root.find(data_point).text
            
            
        icon_url_base = xml_root.find('icon_url_base').text
        icon_url_name = xml_root.find('icon_url_name').text
        icon_url = icon_url_base + icon_url_name
        
        return weather_data_tags_dict, icon_url
    
    
if __name__ == '__main__':
    weather_dict, icon = get_weather_data()
    from pprint import pprint
    pprint(weather_dict)
#     print()
#     print(weather_dict)
    print(icon)
            