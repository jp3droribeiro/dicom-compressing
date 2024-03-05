# # VERSAO 2.0

# # corrigida


# import pydicom
# from pydicom.uid import RLELossless
# import os

# dcm_folder_path = 'dicom_files'
# cp_dcm_folder = 'new_compressed_files'

# ds_list = []

# # Comprimir e salvar os arquivos DICOM
# for file in os.listdir(dcm_folder_path):
#     dcm_file_path = os.path.join(dcm_folder_path, file)
#     if os.path.isfile(dcm_file_path) and file.lower().endswith('.dcm'):
#         ds = pydicom.dcmread(dcm_file_path)
#         size = os.path.getsize(dcm_file_path)
#         print(f'Tamanho do arquivo antes da compressão - {ds.PatientName}: {size} bytes')
#         ds.compress(RLELossless)
#         new_file_path = os.path.join(cp_dcm_folder, f'cp_{file}')
#         ds.save_as(new_file_path)
#         ds_list.append(new_file_path)


# # Mostrar o tamanho dos arquivos comprimidos
# for file_path in ds_list:
#     size2 = os.path.getsize(file_path)
#     file_name = os.path.basename(file_path)
#     print(f' \n Tamanho do arquivo comprimido - {file_name}: {size2} bytes')
    
    
