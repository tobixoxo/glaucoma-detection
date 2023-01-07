# GLAUCOMA DETECTION USING DEEP LEARNING
## Introduction
Glaucoma is a group of related eye disorders that cause damage to the optic nerve that carries information from the eye to the brain which can get worse over time and lead to blindness. It is very important that glaucoma is detected as early as possible for proper treatment. In this project, we have proposed a Convolutional Neural Network (CNN) system for early detection of Glaucoma. The eye images are pre- processed to remove noise using Gaussian Blur technique and make the image suitable for further processing. The system is trained using the pre-processed images and when new input images are given to the system it classifies them as normal eye or glaucoma eye based on the features extracted during training.
## Datsets
### RIM-ONE
485 images https://github.com/miag-ull/rim-one-dl
### ACRIMA
735 images http://www.cvblab.webs.upv.es/project/acrima_en/
### Models Tested
- VGG16
- InceptionV3
- Xception
### Results
#### RIM ONE DATASET RESULTS

|MODEL USED | PRECISION | RECALL | ACCURACY|
|--- | --- | --- | --- |
|First Prototype | 74 | 94 | 68|
|VGG-16 | 93.18 | 83.56 | 85.32|
|InceptionV3 | 90.80 | 84.04 | 84.24|
|Xception | 95.34 | 87.23 | 89.40|

#### ACRIMA DATASET RESULTS

|MODEL USED | PRECISION | RECALL | ACCURACY|
|--- | --- | --- | --- |
|First Prototype |- |- |-|
|VGG-16 |88.26 |85.33 |86.54|
|InceptionV3 |77.89| 82.11 |80.54|
|Xception |91.42| 96.96 |94.20|

#### COMBINED DATASET RESULTS
|MODEL USED | PRECISION | RECALL | ACCURACY|
|--- | --- | --- | --- |
|First Prototype |- |- |-|
|VGG-16| 81.89 |89.68 |82.41|
|InceptionV3 |81.37 |88.29 |79.45|
|Xception |84.07 |90.41 |86.67|


