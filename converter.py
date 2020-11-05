import json
import pandas as pd
import fire
from tqdm import tqdm

def scrapy2dframe(json_file):    
    with open(json_file) as file:
        datas = json.load(file)
    
    alamat = {
        'name':[],
        'address': [],
        'region':[]
    }
    
    for data in tqdm(datas):
        name = str(data['name']).strip()
        address = str(data['address']).strip()
        
        alamat['name'].append(name)
        alamat['address'].append(address)
        alamat['region'].append(data['region'])

    df = pd.DataFrame(alamat)
    
    return df


def json2csv(src_path, dst_path):
    """[summary]

    Args:
        src_path ([type]): [description]
        dst_path ([type]): [description]
    """
    dframe:pd.DataFrame = scrapy2dframe(src_path)
    dframe.to_csv(dst_path, index=False, index_label=False)
    

if __name__ == "__main__":
    fire.Fire(json2csv)