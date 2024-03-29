import tensorflow as tf
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd

file="../pimaindiansdiabetescsv.zip"

diabetes = pd.read_csv(file)
diabetes.replace(0, diabetes.replace([0], [None]))# This is causing problems
diabetes.head(5)
print(diabetes.columns)
normalize = ['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI', 'DiabetesPedigreeFunction']
diabetes[normalize] = diabetes[normalize].apply(lambda x:(x-x.min())/(x.max())-x.min())
nump = tf.feature_column.numeric_column('Pregnancies')
glucval = tf.feature_column.numeric_column('Glucose')
bp = tf.feature_column.numeric_column('BloodPressure')
intsk = tf.feature_column.numeric_column('SkinThickness')
insulinval = tf.feature_column.numeric_column('Insulin')
bmival = tf.feature_column.numeric_column('BMI')
dbf = tf.feature_column.numeric_column('DiabetesPedigreeFunction')
ageval  = tf.feature_column.numeric_column('Age')
assignedg = tf.feature_column.categorical_column_with_vocabulary_list('Group',['A','B','C','D'])


diabetes['Age'].hist(bins=20)
x_data = diabetes.drop('Outcome',axis=1)
labels = diabetes['Outcome']

test_size = 0.037
seed = 89
X = x_data
Y = labels
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y,test_size=test_size, random_state=seed)
input_func=tf.estimator.inputs.pandas_input_fn(x=X_train,y=y_train
                                           ,batch_size=5
                                            ,num_epochs= 1250
                                           ,shuffle=True)

age_buckets = tf.feature_column.bucketized_column(ageval, boundaries=[20,30,40,50,60,70,80])
feat_cols = ([nump,glucval,bp,intsk,insulinval,bmival,dbf,age_buckets])
model = tf.estimator.LinearClassifier(feature_columns=feat_cols, n_classes=2)
model.train(input_fn=input_func, steps=1250)
