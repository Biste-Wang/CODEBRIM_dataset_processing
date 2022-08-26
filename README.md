# CODEBRIM_dataset_processing
### A method for processing the annotation of CODEBRIM Dataset

## Dataset
The dataset is available at: [https://doi.org/10.5281/zenodo.2620293](https://doi.org/10.5281/zenodo.2620293) 

Please note that the dataset is licensed for non-commercial and educational use only as specified by the license file attached with the dataset at above link. 

Please cite the paper if you make use of the content (e.g. the dataset):

> **Martin Mundt, Sagnik Majumder, Sreenivas Murali, Panagiotis Panetsos, Visvanathan Ramesh.
> *Meta-learning Convolutional Neural Architectures for Multi-target Concrete Defect Classification with the COncrete DEfect BRidge IMage Dataset.*
> IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2019**

## File list
* [**xml_show.py**](https://github.com/Biste-Wang/CODEBRIM_dataset_processing/blob/main/xml_show.py) : Display bounding boxes and annotations on the picture 

* [**xml_trans.py**](https://github.com/Biste-Wang/CODEBRIM_dataset_processing/blob/main/xml_trans.py) : Extract damage categories according to the value 0/1 in the **Element \<Defect>** and rewrite the **Element \<object>**  

* [**xml_seri.py**](https://github.com/Biste-Wang/CODEBRIM_dataset_processing/blob/main/xml_seri.py) : Beautify files by adjusting line breaks and indentations 

## Result
Through xml_trans.py and xml_seri.py above, we can transform 
