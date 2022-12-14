#!/usr/bin/python3

#  --------
# |Šaltinis|
#  --------

# Source: https://github.com/hymoe/Intrusion-Detection-on-NSL-KDD

#  -------------------------
# |Importuojamos bibliotekos|
#  -------------------------

import os
import csv
import time
import keras
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, GRU
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.utils import to_categorical, plot_model
from sklearn.preprocessing import Normalizer
import matplotlib.pyplot as plt

#  -----------------------
# |Veikimo laiko matavimas|
#  -----------------------
start = time.perf_counter()

#  -------------------
# |Duomenų apdorojimas|
#  -------------------

# Visi 39 atakų tipai suklasifikuojami į 4 klases
print("[+] NSL-KDD tinklo duomenų rinkinyje esančių atakų tipų klasifikacija į 4 klases")
print("--------------------------------------------------------------------------------")
dos_type = ['back','land','neptune','pod','smurf','teardrop','processtable','udpstorm','mailbomb','apache2']
probing_type = ['ipsweep','mscan','nmap','portsweep','saint','satan']
r2l_type = ['ftp_write','guess_passwd','imap','multihop','phf','warezmaster','warezclient','spy','sendmail','xlock','snmpguess','named','xsnoop','snmpgetattack','worm']
u2r_type = ['buffer_overflow','loadmodule','perl','rootkit','xterm','ps','httptunnel','sqlattack']
type2id = {'normal':0}

for i in dos_type:
    type2id[i] = 1
for i in r2l_type:
    type2id[i] = 2
for i in u2r_type:
    type2id[i] = 3
for i in probing_type:
    type2id[i] = 4
print(f"Klasifikuoti atakų tipai: {type2id}\n")

# Kiekvienam protokolo tipui priskiriamas eilės numeris
print("[+] NSL-KDD tinklo duomenų rinkinyje esantys protokolų tipai")
print("------------------------------------------------------------")
all_protocol = ['tcp', 'udp', 'icmp']
protocol_dict = {}
for id,name in enumerate(all_protocol):
    protocol_dict[name] = id
print(f"Protokolų tipai: {protocol_dict}\n")

# Kiekvienam paslaugos tipui priskiriamas eilės numeris
print("[+] NSL-KDD tinklo duomenų rinkinyje esantys paslaugų tipai")
print("-----------------------------------------------------------")
all_service = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u', 'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest', 'hostnames', 'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell', 'ldap', 'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i', 'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time', 'urh_i', 'urp_i', 'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50']
service_dict = {}
for id,name in enumerate(all_service):
    service_dict[name] = id
print(f"Paslaugų tipai: {service_dict}\n")

# Kiekvienai vėliavos (flag) vertei priskiriamas eliės numeris
print("[+] NSL-KDD tinklo duomenų rinkinyje esantčios vėliavos vertės")
print("--------------------------------------------------------------")
all_flag = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH']
flag_dict = {}
for id,name in enumerate(all_flag):
    flag_dict[name] = id
print(f"Vėliavos: {flag_dict}\n")

# Apmokymo duomenų nuskaitymas
all_train_data = []
trainX = []
trainY = []
with open(os.getcwd()+'/NSL-KDD/KDDTrain+.txt', newline='') as trainingData:
    trainingData = csv.reader(trainingData, delimiter=',')
    for row in trainingData:
        all_train_data.append(row) # Duomenys nuskaitomi eilutė po eilutės
print("[+] Apmokymo duomenys, paimti iš duomenų rinkinio")
print("-------------------------------------------------")
print(all_train_data[0],"\n")

# Tekstinės duomenų reikšmės pakeičiamos jų koduotomis vertėmis
for i in all_train_data:
    i[1] = protocol_dict[i[1]]
    i[2] = service_dict[i[2]]
    i[3] = flag_dict[i[3]]
    i[-2] = type2id[i[-2]]
    trainX.append(i[:41])
    trainY.append(i[-2])
print("[+] Užkoduoti apmokymo duomenys")
print("-------------------------------")
print(trainX[0],"\n")
print("[+] Užkoduotas kibernetinės atakos tipas (0-5)")
print("----------------------------------------------")
print(trainY[0],"\n")

# Testavimo duomenų nuskaitymas
all_test_data = []
testX = []
testY = []
with open(os.getcwd()+'/NSL-KDD/KDDTest+.txt', newline='') as testData:
    testData = csv.reader(testData, delimiter=',')
    for row in testData:
        all_test_data.append(row) # Duomenys nuskaitomi eilutė po eilutės
print("[+] Testavimo duomenys, paimti iš duomenų rinkinio")
print("--------------------------------------------------")
print(all_test_data[0],"\n")

# Tekstinės duomenų reikšmės pakeičiamos jų koduotomis vertėmis
for i in all_test_data:
    i[1] = protocol_dict[i[1]]
    i[2] = service_dict[i[2]]
    i[3] = flag_dict[i[3]]
    i[-2] = type2id[i[-2]]
    testX.append(i[:41])
    testY.append(i[-2])

print("[+] Užkoduoti testavimo duomenys")
print("--------------------------------")
print(testX[0],"\n")
print("[+] Užkoduotas kibernetinės atakos tipas (0-5)")
print("----------------------------------------------")
print(testY[0],"\n")

# Duomenų parengimas (preprocessing)
trainX = Normalizer().fit(trainX).transform(trainX)
print("\n[+] Transformuoti apmokymo duomenys")
print("-----------------------------------")
print(trainX,"\n")
testX = Normalizer().fit(trainX).transform(testX)
print("[+] Transformuoti testavimo duomenys")
print("------------------------------------")
print(testX,"\n")

# Duomenų transformavimas į 3D masyvą
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
print("[+] Apmokymo duomenys transformuoti į 3D masyvą")
print("-----------------------------------------------")
print(trainX,"\n")
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))
print("[+] Testavimo duomenys transformuoti į 3D masyvą")
print("------------------------------------------------")
print(testX,"\n")

# Kompiuterinio tinklo klasių kodavimas one-hot metodu
trainY = tf.keras.utils.to_categorical(trainY, num_classes=5)
print("[+] Apmokymo duomenų rinkinyje esančių atakų klasių kodavimas one-hot metodu")
print("----------------------------------------------------------------------------")
print(trainY,"\n")
testY = tf.keras.utils.to_categorical(testY, num_classes=5)
print("[+] Testavimo duomenų rinkinyje esančių atakų klasių kodavimas one-hot metodu")
print("-----------------------------------------------------------------------------")
print(testY,"\n")

print("[+] Duomenys parengti\n")

#  -----------------
# |Duomenys parengti|
#  -----------------

#  -------
# |Modelis|
#  -------

# Modelio sukūrimas
model = Sequential()
model.add(GRU(256, input_shape=(1,41)))     # Gated Recurrent Unit, skirtas saugoti aktualią tinklui informaciją
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))     # Paslėptas sluoksnis #1
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))     # Paslėptas sluoksnis #2
model.add(Dropout(0.2))
model.add(Dense(5, activation='softmax'))   # Išeigos sluoksnis

sgd = SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])

print("\n[+] Modelio apmokymas bei validavimas")
print("---------------------------------------")
history = model.fit(trainX, trainY,
          epochs=20,
          batch_size=16, validation_split=0.1, verbose=1)

print("\n[+] Modelio testavimas")
print("------------------------")
_, score = model.evaluate(testX, testY, batch_size=16)
print("\n[+] Modelio tikslumas")
print("-----------------------")
print('Tikslumas: %.2f' % (score*100)+"%")

#  --------
# |Grafikai|
#  --------

print("\n[+] Sukurto neuroninio tinklo modelio grafikai")
print("------------------------------------------------")
print("[+] Kuriama neuroninio tinklo modelio blokinė schema")
plot_model(model, to_file='Models/model.png')
print("[+] Schema išsaugota adresu:"+os.getcwd()+"/Models/model.png")

# Grafike pavaizduojamos apmokymo bei validavimo tikslumo reikšmės
print("[+] Kuriamas neuroninio tinklo modelio tikslumo grafikas")
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig(os.getcwd()+'/Models/acc.png')
print("[+] Grafikas išsaugotas adresu:"+os.getcwd()+"/Models/acc.png")

# Apmokymo bei validavimo praradimo (loss) reikšmės
print("[+] Kuriamas praradimo (loss) vertės grafikas")
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.savefig(os.getcwd()+'/Models/loss.png')
print("[+] Grafikas išsaugotas adresu:"+os.getcwd()+"/Models/loss.png")

#  -----------------------
# |Veikimo laiko matavimas|
#  -----------------------
print("\n[+] Programos veikimo laikas")
print("------------------------------")
end = time.perf_counter()
laikas = end-start
if (laikas < 60):
    print("Programos veikimo laikas: %.2f" % laikas+" s")
if (laikas > 60):
    minutes = laikas / 60
    sekundes = laikas - int(minutes) * 60
    print("Programos veikimo laikas: %.0f" % minutes+" min. ir %.2f" % sekundes+" s")
