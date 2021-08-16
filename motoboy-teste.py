motoboys = [{
    "name": "motoboy_1",
    "price": "2",
    "exclusive": "todas"
},{
    "name": "motoboy_2",
    "price": "2",
    "exclusive": "todas"
},{
    "name": "motoboy_3",
    "price": "2",
    "exclusive": "todas"
},{
    "name": "motoboy_4",
    "price": "2",
    "exclusive": "loja_1"
},{
    "name": "motoboy_5",
    "price": "3",
    "exclusive": "todas"
}]

lojas = [{
    "name": "loja_1",
    "pedidos": ["50", "50", "50"],
    "percentile": "5"        
},{
    "name": "loja_2",
    "pedidos": ["50", "50", "50", "50"],
    "percentile": "5"
},{
    "name": "loja_3",
    "pedidos": ["50", "50", "100"],
    "percentile": "15"
}]

while True:
    input_motoboy = str(input("Escolha um motoboy ou tecle enter: \n1. motoboy_1 \n2. motoboy_2 \n3. motoboy_3 \n4. motoboy_4 \n5. motoboy_5 \n\nEscolha: " ))
    motoboy = []
    if len(input_motoboy) == 0:
        motoboy = motoboys
        break
    elif len(input_motoboy) > 1:
        continue
    elif input_motoboy == '1':
        motoboy.append(motoboys[0])
        break
    elif input_motoboy == '2':
        motoboy.append(motoboys[1])
        break
    elif input_motoboy == '3':
        motoboy.append(motoboys[2])
        break
    elif input_motoboy == '4':
        motoboy.append(motoboys[3])
        break
    elif input_motoboy == '5':
        motoboy.append(motoboys[4])
        break


def percentile(n1, n2): 
    percent = (n1*n2)/100 
    return percent     


def motoboys_delivery(motoboy):
    results = []
    i = 0
    for m in motoboy:
        results.append({'name': m['name'], "amount_delivered": 0, "amount_received": 0, "loja": ''})
        delivered = 0
        amount = 0
        for loja in lojas:
            if m['exclusive'] != loja['name'] and m['exclusive'] == 'todas':
                for pedido in loja['pedidos']:
                    amount += int(m['price'])
                    amount += percentile(int(loja['percentile']), int(pedido))
                    delivered += 1
                results[i]['amount_received'] = amount
                results[i]['amount_delivered'] = delivered
            elif m['exclusive'] == loja['name']:
                for pedido in loja['pedidos']:
                    amount += int(m['price'])
                    amount += percentile(int(loja['percentile']), int(pedido))
                    delivered += 1
                results[i]['amount_received'] = amount
                results[i]['amount_delivered'] = delivered
        results[i]['loja'] = m['exclusive']        
        i += 1
    for result in results:
        print(10*'*'+result['name']+10*'*' )
        print("Quem é o motoboy:\nR: {}".format(result['name']))
        print("Quantos pedidos terá?\nR: {}".format(result['amount_delivered']))
        print("De qual loja é?\nR: {}".format(result['loja']))
        print("Quanto vai ganhar?\nR: R${:.2f}".format(result['amount_received']))
        print('')
                
    
if __name__ == '__main__':
    motoboys_delivery(motoboy)    