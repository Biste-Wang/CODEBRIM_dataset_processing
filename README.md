# CODEBRIM_dataset_processing
### A method for processing the annotation of CODEBRIM Dataset

## Dataset
The dataset is available at: [https://doi.org/10.5281/zenodo.2620293](https://doi.org/10.5281/zenodo.2620293) 

Please note that the dataset is licensed for non-commercial and educational use only as specified by the license file attached with the dataset at above link. 

Please cite the paper if you make use of the content (e.g. the dataset):

> **Martin Mundt, Sagnik Majumder, Sreenivas Murali, Panagiotis Panetsos, Visvanathan Ramesh.
> *Meta-learning Convolutional Neural Architectures for Multi-target Concrete Defect Classification with the COncrete DEfect BRidge IMage Dataset.*
> IEEE Conference on Computer Vision and Pattern Recognition (CVPR), 2019**

## File
* [**xml_show.py**](https://github.com/Biste-Wang/CODEBRIM_dataset_processing/blob/main/xml_show.py) : Display bounding boxes and annotations on the picture 

* [**xml_trans.py**](https://github.com/Biste-Wang/CODEBRIM_dataset_processing/blob/main/xml_trans.py) : Extract damage categories according to the value 0/1 in the **Element \<Defect>** and rewrite the **Element \<object>**  

* [**xml_seri.py**](https://github.com/Biste-Wang/CODEBRIM_dataset_processing/blob/main/xml_seri.py) : Beautify files by adjusting line breaks and indentations 

## Result
Through xml_trans.py and xml_seri.py above, we can transform the original annotation format to a new style, where bridge damages are the first level annotations in xml files. And then we can convert .xml to .txt and try the open source YOLO algorithm to detect the damages of bridges.

**An example of original annotation**
```
<?xml version='1.0' encoding='utf-8'?>
<annotation>
	<folder>images</folder>
	<filename>image_0000028.jpg</filename>
	<size>
		<width>1752</width>
		<height>2632</height>
		<depth>3</depth>
	</size>
	<object>
		<name>defect</name>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1</xmin>
			<ymin>1</ymin>
			<xmax>907</xmax>
			<ymax>1043</ymax>
		</bndbox>
		<Defect>
			<Background>0</Background>
			<Crack>0</Crack>
			<Spallation>0</Spallation>
			<Efflorescence>1</Efflorescence>
			<ExposedBars>0</ExposedBars>
			<CorrosionStain>1</CorrosionStain>
		</Defect>
	</object>
	<object>
		<name>defect</name>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1173</xmin>
			<ymin>1</ymin>
			<xmax>1747</xmax>
			<ymax>1077</ymax>
		</bndbox>
		<Defect>
			<Background>0</Background>
			<Crack>0</Crack>
			<Spallation>0</Spallation>
			<Efflorescence>1</Efflorescence>
			<ExposedBars>0</ExposedBars>
			<CorrosionStain>0</CorrosionStain>
		</Defect>
	</object>
</annotation>
```

**An example of transformed annotation**
```
<annotation>
	<folder>images</folder>
	<filename>image_0000028.jpg</filename>
	<size>
		<width>1752</width>
		<height>2632</height>
		<depth>3</depth>
	</size>
	<object>
		<name>Efflorescence</name>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1</xmin>
			<ymin>1</ymin>
			<xmax>907</xmax>
			<ymax>1043</ymax>
		</bndbox>
	</object>
	<object>
		<name>CorrosionStain</name>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1</xmin>
			<ymin>1</ymin>
			<xmax>907</xmax>
			<ymax>1043</ymax>
		</bndbox>
	</object>
	<object>
		<name>Efflorescence</name>
		<difficult>0</difficult>
		<bndbox>
			<xmin>1173</xmin>
			<ymin>1</ymin>
			<xmax>1747</xmax>
			<ymax>1077</ymax>
		</bndbox>
	</object>
</annotation>
```

### Author: [**Biste-Wang**](https://github.com/Biste-Wang)
