import random
import time
import matplotlib.pyplot as plt
def bucket_sort(input_list):
    # Encuentra el valor maximo que se encuentra en la lista y usa la longitud de la lista a determinar cual valor en la lista pertenece al casillero
    max_value = max(input_list)
    size = max_value/len(input_list)

    # creacion n casilleros vacios donde n equivale a la longitud de la lista de entrada 
    buckets_list= []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    # pone una lista de elementos basandosen en la condición de tamaño de cada casillero
    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    # al ordenar los elementos, pueden haber algunos que no quedaran entre los casilleros, se apoyan en la función insertion sort
    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    # Concatenacion de los casilleros en el cual se convertira en una sola lista de los elementos ordenados.
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

#Función capaz de manejar elementos en los cuales no se encuentren en el tamaño de cada casillero, se trata de crear uno especialmente para ellos
def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def run():

    tt = []
    opcion = int(input("Digite la opcion de deseada: "))
    if opcion == 1:
        cant = int(input("Digite la cantidad de datos:"))
        for x in range(1,cant+1):
            ls = [random.randint(0,x+1) for _ in range(x+1)]
            ti = time.time_ns()
            ls = bucket_sort(ls)
            tf = time.time_ns()
            tt.append(tf-ti)
            
    else:
        pass

    fig = plt.figure(figsize=(10,6))
    ax = fig.add_subplot()
    ax.set_title("Tiempos")
    ax.plot(tt,label="Tiempos Finales")
    ax.set_xlabel("Datos")
    ax.set_ylabel("Tiempo")
    ax.legend()
    plt.ticklabel_format(useOffset=False, style='plain')

    fig.align_labels() 
    plt.show()



if __name__ == '__main__':
    run()