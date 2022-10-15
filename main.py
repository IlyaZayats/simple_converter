import os
import dicom2nifti
import dicom2nifti.settings as settings


settings.disable_validate_slice_increment()

dicom_path = input("Input path to dataset: ")
nifti_path = input("Input path where dataset will store: ")

dicom_paths = [
    os.path.join(os.getcwd(), dicom_path, x)
    for x in os.listdir(dicom_path)
]

if (not os.path.exists(nifti_path)):
    os.makedirs(nifti_path)

for path in dicom_paths:
    if path.rpartition('/')[2] != '.DS_Store':
        dicom2nifti.dicom_series_to_nifti(path, nifti_path + path.rpartition('/')[2], reorient_nifti=True)
        print("Study " + path.rpartition('/')[2] + " converted!")

