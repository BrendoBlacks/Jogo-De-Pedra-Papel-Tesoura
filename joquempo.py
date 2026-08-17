from random import randint
def jokenpoll(e):
    if e == 1:
        return "Pedra"
    elif e == 2:
        return "Papel"
    elif e == 3:
        return "Tesoura"

def resultado(u, m):
    if u == m:
        return "\033[1;33mEMPATOU\033[m"
    else:    
        if u == 'Pedra':
            if m == 'Papel':
                return '\033[1;31mPERDEU!!!\033[m'
            elif m == 'Tesoura':
                return '\033[1;32mVENCEU!!!\033[m'
            
        elif u == 'Tesoura':
            if m == 'Pedra':
                return '\033[1;31mPERDEU!!!\033[m'
            elif m == 'Papel':
                return '\033[1;32mVENCEU!!!\033[m'
        
        elif u == 'Papel':
            if m == 'Tesoura':
                return '\033[1;31mPERDEU!!!\033[m'
            elif m == 'Pedra':
                return '\033[1;32mVENCEU!!!\033[m'

def leiaInt(termo):
    if termo.isnumeric() is True:
        return int(termo)
    else:
        while termo.isnumeric() is False:
            print('\033[1;31mERRO! Digite uma opção válido.\033[m')
            termo = input('Escolha, [ 1 ] Pedra, [ 2 ] Papel, [ 3 ] Tesoura, [ 999 ] Sair: ')
        return int(termo)

vitorias = 0

while True:
    
    print('-='*30)
    print(f'{' JOGO DO PEDRA, PAPEL E TESOURA ':-^60}')
    escolha_maquina = randint(1,3)
    escolha_usuario = leiaInt(input('Escolha, [ 1 ] Pedra, [ 2 ] Papel, [ 3 ] Tesoura, [ 999 ] Sair: '))
    
    if escolha_usuario == 999:
        break
        
    while escolha_usuario not in (1, 2, 3, 999):
        print('\033[1;31mERRO! Digite uma opção válido.\033[m')
        escolha_usuario = leiaInt(input('Escolha [ 1 ] Pedra, [ 2 ] Papel, [ 3 ] Tesoura, [ 999 ] Sair: '))

    if escolha_usuario == 999:
            break
    
    maquina = jokenpoll(escolha_maquina)
    usuario = jokenpoll(escolha_usuario)
    
    r = resultado(usuario, maquina)
    
    print(f'Usuário: {usuario}')
    print(f'Máquina: {maquina}')
    print(f'Você {r}')
    
    if r == '\033[1;32mVENCEU!!!\033[m':
        vitorias += 1

print('-='*30)
print('JOGO FINALIZADO!!!')
print(f'Você venceu {vitorias} vezes')