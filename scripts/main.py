from get_data import get_data
from read_json import open_data, save_csv_file
from frecuencies import craete_frequency

URL = 'https://dog.ceo/api/breeds/list/all'

def main() -> None:

    get_data(URL,  'perros' )
    json_data = open_data('perros')
    save_csv_file(json_data, 'sub-razas-perros')
    craete_frequency('sub-razas-perros', 'frecuencias')



if __name__=='__main__':
    main()