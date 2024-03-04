import pydicom
from pydicom.uid import RLELossless
import os

dcm_folder_path = 'dicom_files'

ds_list = []

for file in os.listdir(dcm_folder_path):
    dcm_file_path = os.path.join(dcm_folder_path,file)
    if os.path.isfile(dcm_file_path) and file.lower().endswith('.dcm'):
        ds = pydicom.dcmread(dcm_file_path)
        
        ds_list.append(ds)
        #tamanho
        size = os.path.getsize(dcm_file_path)
        print(f'tamanho do arquivo:{ds.PatientName}: {size} bytes')
        
        # comprimir 
        ds.compress(RLELossless)
        # muda o nome pra salvar em uma pasta de comprimidos
        ds.save_as(f'new_compressed_files/cp{file}')
        
        
cp_dcm_folder ='new_compressed_files'

# for file in os.listdir(cp_dcm_folder):
#     dcm_file_path = os.path.join(dcm_folder_path,file)
#     if os.path.isfile(dcm_file_path) and file.lower().endswith('.dcm'):
#         ds = pydicom.dcmread(dcm_file_path)
        
#         size = os.path.getsize(dcm_file_path)
#         print(f'tamanho do arquivo comprimido :{ds.PatientName}: {size} bytes')
        
    
    
    
    

