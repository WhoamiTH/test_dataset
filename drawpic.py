import sys
sys.path.append('..')

from sklearn.externals import joblib
import sklearn.preprocessing as skpre
from sklearn.decomposition import PCA
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np


def loadTrainData(file_name):
    file_data = pd.read_csv(file_name)
    data = file_data.values
    label = data[:,-1]
    # data = np.delete(data, 0, axis=1)
    data = np.delete(data, -1, axis=1)
    # data = np.delete(data, 0, axis=1)
    data = data.astype(np.float64)
    data = pd.DataFrame(data)
    return data, label

def condense_data_pca(Data, num_of_components):
    pca = PCA(n_components=num_of_components)
    pca.fit(Data)
    return pca

def standardize_data(Data):
    scaler = skpre.StandardScaler()
    scaler.fit(Data)
    return scaler

def standarize_PCA_data(Data):
    scaler = standardize_data(Data)
    new_data = scaler.transform(Data)
    
    pca = PCA(n_components=2)
    pca.fit(Data)
    new_data = pca.transform(new_data)

    return new_data, scaler, pca


def transform_data_by_standarize_pca(Data, scaler, pca):
    new_data = scaler.transform(Data)
    # copy
    new_data = pca.transform(new_data)
    return new_data


def divide_data(Data, Label):


    positive_index = np.where(Label == 1)
    negative_index = np.where(Label == 0)

    positive = Data[positive_index[0]]
    negative = Data[negative_index[0]]


    return positive, negative

def divide_to_x_y(data):
    x = data[:, 0]
    y = data[:, 1]
    return x, y

def plotimage(ax1, ax2, train_data, train_label, test_data, test_label):
    # draw picture

    train_posi, train_nega = divide_data(train_data, train_label)
    test_posi, test_nega = divide_data(test_data, test_label)

    
    train_posi_x, train_posi_y = divide_to_x_y(train_posi)
    train_nega_x, train_nega_y = divide_to_x_y(train_nega)

    test_posi_x, test_posi_y = divide_to_x_y(test_posi)
    test_nega_x, test_nega_y = divide_to_x_y(test_nega)

    
    ax1.scatter(train_posi_x, train_posi_y, s=1, label='train_posi', color='b')
    ax1.scatter(train_nega_x, train_nega_y, s=1, label='train_nega', color='r')

    ax2.scatter(test_posi_x, test_posi_y, s=1, label='test_posi', color='b')
    ax2.scatter(test_nega_x, test_nega_y, s=1, label='test_nega', color='r')


    ax1.set_title('train data')
    ax2.set_title('train data')

    ax1.set_xlabel('x')
    ax1.set_ylabel('y')

    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')


def getNum(file_name):
    firstChar = file_name[-5]
    secondChar = file_name[-6]
    num = firstChar
    if secondChar.isdigit():
        num = secondChar + num
    current_file_number = int(num)
    return current_file_number


# def readandplot(ax1, ax2, file_name_pre, file_number):
#     train_file_name = './1_year_data/{0}_train_{1}.csv'.format(file_name_pre, file_number) 
#     test_file_name = './1_year_data/{0}_test_{1}.csv'.format(file_name_pre, file_number)

#     # data input
#     train_data, train_label = loadTrainData(train_file_name)

#     train_data = train_data.values
#     train_data = train_data.astype(np.float64)

#     train_label = train_label.astype(np.int)

#     train_data, standardize_scaler, pca_model = standarize_PCA_data(train_data)

#     test_data, test_label = loadTrainData(test_file_name)
#     test_data = test_data.values
#     test_data = test_data.astype(np.float64)
#     test_label = test_label.astype(np.int)

#     test_data = transform_data_by_standarize_pca(test_data, standardize_scaler, pca_model)
#     plotimage(ax1, ax2, train_data, train_label, test_data, test_label)


def readandplot(ax1, ax2, file_name_pre, file_number):
    train_file_name = '../1_year_data/{0}_train_{1}.csv'.format(file_name_pre, file_number) 
    test_file_name = '../1_year_data/{0}_test_{1}.csv'.format(file_name_pre, file_number)

    # data input
    train_data, train_label = loadTrainData(train_file_name)

    train_data = train_data.values
    train_data = train_data.astype(np.float64)

    train_label = train_label.astype(np.int)

    train_data, standardize_scaler, pca_model = standarize_PCA_data(train_data)

    test_data, test_label = loadTrainData(test_file_name)
    test_data = test_data.values
    test_data = test_data.astype(np.float64)
    test_label = test_label.astype(np.int)

    test_data = transform_data_by_standarize_pca(test_data, standardize_scaler, pca_model)
    plotimage(ax1, ax2, train_data, train_label, test_data, test_label)




# def set_para():
#     global train_file_name
#     global test_file_name
   

#     argv = sys.argv[1:]
#     for each in argv:
#         para = each.split('=')
#         if para[0] == 'train_file_name':
#             train_file_name = para[1]
#         if para[0] == 'test_file_name':
#             test_file_name = para[1]


# -------------------------------------global parameters-------------------------------
# test_number = 5

file_name_pre = 'yeast6'

fig, ax = plt.subplots(5,2)

# print(len(ax))
# print(len(ax[0]))



# set_para()

fig, ax = plt.subplots(5,2, figsize=(10,20))

# for row in range(len(ax)):
#     for col in range(len(ax[0])):
#         if (col%2 == 0):
#             file_name = './1_year_data/{0}_train_{1}.csv'.format(file_name_pre, row)
#         else:
#             file_name = './1_year_data/{0}_test_{1}.csv'.format(file_name_pre, row)
#         current_row = row+1
#         current_col = col+1

for row in range(len(ax)):
    readandplot(ax[row][0], ax[row][1], file_name_pre, row+1)

plt.savefig('distribution_{0}.pdf'.format(file_name_pre))