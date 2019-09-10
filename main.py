import random, time

def random_float():
    return random.randint(0, 20000000000) / 10000000000

def set_connections():
    connections = []
    for i in range(27):
        connections.append(random_float())
    return connections

def get_dataset(file_name="dataset.ds"):
    result = {}
    with open(file_name) as file:
        for i in file.readlines():
            a = i.split(":")
            result.update({int(a[0]):int(a[1])})
    return result

data_set = get_dataset()
connections = set_connections()

final = []
for test in data_set:
    bin_input = bin(test)[2:] # Pega em cada número do data set e transforma em binario sem o 0b
    ready_input = ['0']*(27 - len(bin_input)) + list(bin_input) # Pega em cada numero e transforma em lista com zeros à esquerda para
    # os numeros que têm menos que 27 caraqueteres
    result = [] # Inicializa a variavel result
    for bit in ready_input:
        biti = int(bit) + 1 # Para cada bit na lista do binário de cada numero no dataset transforma-o em inteiro e adiciona 1
        # por causa do 0 !?
        result.append((biti*connections[ready_input.index(bit)])-1) # Adiciona à lista result o valor de bit + 1 multiplicado pelo valor
        # das conexões selecionadas para cada index da lista
        byte = "" # Inicializa a variávlel byte

        for b in result:

            ## PEGAR NOS VALORES DE BYTE NO MAXIMO ENTRE 0 - 2 E TRANSFORMAR EM BINARIO POR ARREDONDAMENTO,
            ## JUNTAR TODOS E FORMAR O NUMERO FINAL
            if b < 0:
                b = 0
            elif b > 1:
                b = 1
            else:
                b = round(b)
            byte += str(b)

            #byte += b ### Estava a pegar no valor de b que era um numero e estava a adicionar como inteiro
        #print(byte)
    #final.append(int(byte, 2))
    final.append(byte)

#print(final)
for i in final:
    print(str(int(i, 2)))# + ":")# + str(data_set[ ## COMPARAR COM A ENTRADA DO DATASET CORRESPONDENTE

print(data_set)

