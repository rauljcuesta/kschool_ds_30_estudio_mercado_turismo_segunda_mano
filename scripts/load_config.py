
def load_config_const():
    import yaml
    with open(r'./../config/config.yml') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config



def cod_postal_zero_int_repair(cod_postal):
    import math
    if (not math.isnan( cod_postal )):
        cod_postal = int(cod_postal)
        if ( len(str(cod_postal)) == 5 ):
            return str(cod_postal)
        elif ( len(str(int(cod_postal))) == 4 ):
            return '0'+str(int(cod_postal))
        else:
            return int(cod_postal)
    else:
        return cod_postal
    return False
  

def return_id_province_by_zip(cod_postal):
    if (cod_postal):
        cod_postal = str(cod_postal)
        return cod_postal[0:2]
    else:
        return cod_postal
    return False
  


def is_weekend(day_week):
    if (day_week == 'Saturday' or day_week == 'Sunday'):
        return True
    else:
        return False
    return False


    
def return_province(id_province):
    list_ids_province = {
        '01': 'Álava',
        '08': 'Barcelona',
        '15': 'La Coruña',
        '23': 'Jaén',
        '30': 'Murcia',
        '38': 'Santa Cruz de Tenerife',
        '45': 'Toledo',
        '02': 'Albacete',
        '09': 'Burgos',
        '16': 'Cuenca',
        '24': 'León',
        '31': 'Navarra',
        '46': 'Valencia',
        '03': 'Alicante',
        '10': 'Cáceres',
        '17': 'Gerona',
        '25': 'Lérida',
        '32': 'Orense',
        '39': 'Cantabria',
        '47': 'Valladolid',
        '04': 'Almería',
        '11': 'Cádiz',
        '18': 'Granada',
        '26': 'La Rioja',
        '33': 'Asturias',
        '40': 'Segovia',
        '48': 'Vizcaya',
        '05': 'Ávila',
        '12': 'Castellón',
        '19': 'Guadalajara',
        '34': 'Palencia',
        '41': 'Sevilla',
        '49': 'Zamora',
        '06': 'Badajoz',
        '13': 'Ciudad Real',
        '20': 'Guipúzcoa',
        '27': 'Lugo',
        '35': 'Las Palmas',
        '42': 'Soria',
        '50': 'Zaragoza',
        '07': 'Islas Baleares',
        '21': 'Huelva',
        '28': 'Madrid',
        '36': 'Pontevedra',
        '43': 'Tarragona',
        '51': 'Ceuta',
        '14': 'Córdoba',
        '22': 'Huesca',
        '29': 'Málaga',
        '37': 'Salamanca',
        '44': 'Teruel',
        '52': 'Melilla'
    }
    
    return list_ids_province.get(id_province)

def return_make(make):
    list_makes = {
        'ABARTH': 'ABARTH',
        'ALFA': 'ALFA ROMEO',
        'ALFA ROMEO': '',
        'ASTON MARTIN': 'ASTON MARTIN',
        'AUDI': 'AUDI',
        'BENTLEY': 'BENTLEY',
        'BMW': 'BMW',
        'BMW I': 'BMW',
        'CADILLAC': 'CADILLAC',
        'CHEVROLET': 'CHEVROLET',
        'CHRYSLER': 'CHRYSLER',
        'CITROEN': 'CITROEN',
        'CUPRA': 'CUPRA',
        'DACIA': 'DACIA',
        'DAEWOO': 'DAEWOO',
        'DAIHATSU': 'DAIHATSU',
        'DAIMLER': 'DAIMLER',
        'DAIMLER AG': 'DAIMLER',
        'DAIMLER CHRYSLER': 'CHRYSLER',
        'DODGE': 'DODGE',
        'DS': 'DS',
        'FERRARI': 'FERRARI',
        'FIAT': 'FIAT',
        'FORD': 'FORD',
        'FORD CNG TECHNIK': 'FORD',
        'FORD-CNG-TECHNIK': 'FORD',
        'GMC': 'GMC',
        'HONDA': 'HONDA',
        'HUMMER': 'HUMMER',
        'HYUNDAI': 'HYUNDAI',
        'INFINITI': 'INFINITI',
        'ISUZU': 'ISUZU',
        'IVECO': 'IVECO',
        'JAGUAR': 'JAGUAR',
        'JAGUAR LAND ROVER LIMIT': 'LAND-ROVER',
        'JEEP': 'JEEP',
        'KIA': 'KIA',
        'LADA': 'LADA',
        'LAMBORGHINI': 'LAMBORGHINI',
        'LANCIA': 'LANCIA',
        'LAND ROVER': 'LAND-ROVER',
        'LEXUS': 'LEXUS',
        'LOTUS': 'LOTUS',
        'M.G': 'MG',
        'MAHINDRA': 'MAHINDRA',
        'MASERATI': 'MASERATI',
        'MAZDA': 'MAZDA',
        'MCC SMART': 'SMART',
        'MCLAREN': 'MCLAREN',
        'MERCEDES': 'MERCEDES-BENZ',
        'MERCEDES-AMG': 'MERCEDES-BENZ',
        'MERCEDES-BENZ': 'MERCEDES-BENZ',
        'MG': 'MG',
        'MICRO COMPACT CAR': 'SMART',
        'MINI': 'MINI',
        'MITSUBISHI': 'MITSUBISHI',
        'NISSAN': 'NISSAN',
        'OPEL': 'OPEL',
        'PEUGEOT': 'PEUGEOT',
        'PORSCHE': 'PORSCHE',
        'QUATTRO': 'AUDI',
        'RANGE ROVER': 'ROVER',
        'RENAULT': 'RENAULT',
        'ROVER': 'ROVER',
        'SAAB': 'SAAB',
        'SANTANA': 'SANTANA',
        'SEAT': 'SEAT',
        'SEAT FIAT': 'SEAT',
        'SKODA': 'SKODA',
        'SMART': 'SMART',
        'SSANGYONG': 'SSANGYONG',
        'SUBARU': 'SUBARU',
        'SUZUKI': 'SUZUKI',
        'SUZUKI SANTANA': 'SANTANA',
        'TATA': 'TATA',
        'TESLA': 'TESLA',
        'TESLA MOTORS': 'TESLA',
        'TOYOTA': 'TOYOTA',
        'VOLKSWAGEN': 'VOLKSWAGEN',
        'VOLKSWAGEN V W': 'VOLKSWAGEN',
        'VOLVO': 'VOLVO'
    }
    
    return list_makes.get(make)



def return_avaliable_makes():
    return [
        'ABARTH',
        'ALFA',
        'ALFA ROMEO',
        'ASTON MARTIN',
        'AUDI',
        'BENTLEY',
        'BMW',
        'BMW I',
        'CADILLAC',
        'CHEVROLET',
        'CHRYSLER',
        'CITROEN',
        'CUPRA',
        'DACIA',
        'DAEWOO',
        'DAIHATSU',
        'DAIMLER',
        'DAIMLER AG',
        'DAIMLER CHRYSLER',
        'DODGE',
        'DS',
        'FERRARI',
        'FIAT',
        'FORD',
        'FORD CNG TECHNIK',
        'FORD-CNG-TECHNIK',
        'GMC',
        'HONDA',
        'HUMMER',
        'HYUNDAI',
        'INFINITI',
        'ISUZU',
        'IVECO',
        'JAGUAR',
        'JAGUAR LAND ROVER LIMIT',
        'JEEP',
        'KIA',
        'LADA',
        'LAMBORGHINI',
        'LANCIA',
        'LAND ROVER',
        'LEXUS',
        'LOTUS',
        'M.G',
        'MAHINDRA',
        'MASERATI',
        'MAZDA',
        'MCC SMART',
        'MCLAREN',
        'MERCEDES',
        'MERCEDES-AMG',
        'MERCEDES-BENZ',
        'MG',
        'MICRO COMPACT CAR',
        'MINI',
        'MITSUBISHI',
        'NISSAN',
        'OPEL',
        'PEUGEOT',
        'PORSCHE',
        'QUATTRO',
        'RANGE ROVER',
        'RENAULT',
        'ROVER',
        'SAAB',
        'SANTANA',
        'SEAT',
        'SEAT FIAT',
        'SKODA',
        'SMART',
        'SSANGYONG',
        'SUBARU',
        'SUZUKI',
        'SUZUKI SANTANA',
        'TATA',
        'TESLA',
        'TESLA MOTORS',
        'TOYOTA',
        'VOLKSWAGEN',
        'VOLKSWAGEN V W',
        'VOLVO'
    ]


    
def obtain_dgt_dataset(config, fraction):
    import pandas as pd
    import math
    import numpy as np
    
    columns = config['fields_dgt_process']

    df = '';

    for dgt_file in config['files_dgt']:

        route_file = config['base_route'] + config['data_route'] +  config['data_dgt_route'] + '/' + dgt_file

        print(f'Processing {dgt_file}')

        df_aux = pd.read_csv(route_file, compression='gzip', sep=config['csv_dgt_separator'], low_memory=False)
        df_aux.columns = columns

        '''
        df_aux.astype({
            "Q_query":"int",
            "year_Q":"int",
            "CODIGO_POSTAL":"int",
            "CLAVE_TRAMITE":"int",
            "NUM_TRANSMISIONES":"int",
            "NUM_PLAZAS":"int",
            "NUM_TITULARES":"int",
            "CILINDRADA_ITV":"int",
            "COD_MUNICIPIO_INE_VEH":"int",
            "KW_ITV":"int",
            "NUM_PLAZAS_MAX":"int",
            "CO2_ITV":"int"
        })
        '''

        df_aux = df_aux.sample(frac=fraction)

        df_aux['FEC_MATRICULA'] = pd.to_datetime(df_aux['FEC_MATRICULA'])
        df_aux['FEC_TRAMITACION'] = pd.to_datetime(df_aux['FEC_TRAMITACION'])
        df_aux['FEC_TRAMITE'] = pd.to_datetime(df_aux['FEC_TRAMITE'])
        df_aux['FEC_PRIM_MATRICULACION'] = pd.to_datetime(df_aux['FEC_PRIM_MATRICULACION'])
        
        df_aux = df_aux[df_aux['MARCA_ITV'].isin( return_avaliable_makes() )]
        df_aux['MARCA_ITV'] = df_aux['MARCA_ITV'].apply(lambda x: return_make(x) )
        df_aux = df_aux[df_aux['MARCA_ITV'] != '']

        df_aux['Q_query'] = df_aux['Q_query'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['year_Q'] = df_aux['year_Q'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['CODIGO_POSTAL'] = df_aux['CODIGO_POSTAL'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['CLAVE_TRAMITE'] = df_aux['CLAVE_TRAMITE'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['NUM_TRANSMISIONES'] = df_aux['NUM_TRANSMISIONES'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['NUM_PLAZAS'] = df_aux['NUM_PLAZAS'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['NUM_TITULARES'] = df_aux['NUM_TITULARES'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['CILINDRADA_ITV'] = df_aux['CILINDRADA_ITV'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['COD_MUNICIPIO_INE_VEH'] = df_aux['COD_MUNICIPIO_INE_VEH'].apply(lambda x: int(x) if not math.isnan(x) else x )
        # df_aux['KW_ITV'] = df_aux['KW_ITV'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['NUM_PLAZAS_MAX'] = df_aux['NUM_PLAZAS_MAX'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['CO2_ITV'] = df_aux['CO2_ITV'].apply(lambda x: int(x) if not math.isnan(x) else x )

        df_aux['CODIGO_POSTAL'] = df_aux['CODIGO_POSTAL'].apply(lambda x: cod_postal_zero_int_repair(x) )
        df_aux['COD_MUNICIPIO_INE_VEH'] = df_aux['COD_MUNICIPIO_INE_VEH'].apply(lambda x: cod_postal_zero_int_repair(x) )
        df_aux['ID_MUNICIPIO'] = df_aux['COD_MUNICIPIO_INE_VEH'].apply(lambda x: return_id_province_by_zip(x) )

        df_aux = df_aux[df_aux['FEC_TRAMITACION'] >= '2015-01-01 00:00:00']
        df_aux = df_aux[df_aux['FEC_TRAMITACION'] <= '2021-12-31 23:59:59']

        df_aux = df_aux[df_aux['FEC_TRAMITE'] >= '2015-01-01 00:00:00']
        df_aux = df_aux[df_aux['FEC_TRAMITE'] <= '2021-12-31 23:59:59']

        df_aux['ID_MUNICIPIO'].fillna(value=np.nan, inplace=True)

        df_aux = df_aux[df_aux['ID_MUNICIPIO'].notna()]
        df_aux = df_aux[df_aux['year_Q'].notna()]

        df_aux = df_aux[df_aux['ID_MUNICIPIO'] != 0]

        df_aux['year_Q'] = df_aux['year_Q'].apply(lambda x: int(x) if not math.isnan(x) else x )
        df_aux['Q_query'] = df_aux['Q_query'].apply(lambda x: int(x) if not math.isnan(x) else x )

        df_aux['month_year_Q'] = df_aux['FEC_TRAMITE'].dt.month
        df_aux['day_of_week'] = df_aux['FEC_TRAMITE'].dt.day_name()
        
        df_aux['is_weekend'] = df_aux['day_of_week'].apply(lambda x: is_weekend(x))

        index = df_aux.index
        number_of_rows = len(index)
        print(f'### Lines -> {number_of_rows}')

        if (type(df) == pd.core.frame.DataFrame):
            print('### Merge with main datagrame')
            df = pd.concat([df,df_aux]);
        else:
            print('### Create main datagrame')

            df = df_aux.copy()
            
        del df_aux

        index = df.index
        number_of_rows = len(index)
        print(f'### Total lines -> {number_of_rows}')
        
    return df
