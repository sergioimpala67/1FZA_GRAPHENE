
import numpy
import sys
import os


################################################################################################################
#Archivos output proteina superficie interactuando
################################################################################################################

Output_int_1 = '1fza_result_interaction'
 
file_aux= open('auxiliar.txt','w')

file_1 = open(Output_int_1,'r')

E_solv_interaccion = []
h = []
a_tilt = []
a_rot = []


for line_1 in file_1:
    linea_1=line_1.split()
    if len(linea_1)==11:
        if linea_1[0]== '2.00' or linea_1[0]== '3.00' or linea_1[0]== '4.00' or linea_1[0]== '5.00':
            aa='{0} {1} {2} {3} \n'.format(linea_1[0],linea_1[2],linea_1[4],linea_1[6])
            file_aux.write(aa)
            
            
file_aux.close()

file_aux= open('auxiliar.txt','r')
X=numpy.loadtxt(file_aux)
Xc=numpy.copy(X)
E_solv_interaccion[:]=Xc[:,3]
h[:]=Xc[:,0]
a_tilt[:]=Xc[:,1]
a_rot[:]=Xc[:,2]
file_aux.close()

##############################################################################################################
##############################################################################################################
#Proteina aislada
##############################################################################################################

Output_aislada_1 = '1fza_result_isolated'

file_aux_2= open('auxiliar_2.txt','w')

file_6 = open(Output_aislada_1,'r')

for line_1 in file_6:
    linea_1=line_1.split()
    if len(linea_1)==11:
        if linea_1[0]== '2.00' or linea_1[0]== '3.00' or linea_1[0]== '4.00' or linea_1[0]== '5.00':
            aa='{0} {1} {2} {3} \n'.format(linea_1[0],linea_1[2],linea_1[4],linea_1[6])
            file_aux_2.write(aa)
                        
file_aux_2.close()

file_aux_2= open('auxiliar_2.txt','r')
Y=numpy.loadtxt(file_aux_2)
Yc=numpy.copy(Y)
E_solv_prot_aislada=Yc[3]
file_aux_2.close()
######################################################################################################################
######################################################################################################################
#Superficie sensor
#INSERTAR 
E_solv_sensor_aislada=0

#####################################################################################################################
#####################################################################################################################
#Calculo energia de interaccion y encontrar estado mas probable
E_interaccion = numpy.zeros(len(h))

for i in range(len(h)):
    E_interaccion[i]= E_solv_interaccion[i] - (E_solv_prot_aislada + E_solv_sensor_aislada)
    
E_mas_prob=min(E_interaccion)
argumento_mas_prob=numpy.argmin(E_interaccion)
h_mas_prob = h[argumento_mas_prob]
a_tilt_mas_prob=a_tilt[argumento_mas_prob]
a_rot_mas_prob=a_rot[argumento_mas_prob]

print('Distancia proteina sensor =',h_mas_prob)
print('Alpha_tilt =', a_tilt_mas_prob)
print('Alpha_rot =', a_rot_mas_prob)
print('Energia de Interaccion =', E_mas_prob)

#Archivo_input_probability_plot_python
conformacion_file = open('conformacion','w')
for i in range(len(h)):
	angulos_energia_interaccion='{0} {1} {2} \n'.format(a_tilt[i], a_rot[i], E_interaccion[i])
	conformacion_file.write(angulos_energia_interaccion)
conformacion_file.close()

os.system('rm -r auxiliar.txt')
os.system('rm -r auxiliar_2.txt')	

