from hashlib import sha256
import time
NONCE = 1000000000


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'* prefix_zeros
    for nonce in range(NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Bitcoins minerados com sucesso com valor nonce:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {NONCE} times")

if __name__=='__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty= 19 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
 
    start = time.time()
    print("inicio da mineração")
    new_hash = mine(5,transactions,'00000000000000000007428108c07f5bb223b8f95f65ab14f8c11b49a203c770', difficulty)
    total_time = str((time.time() - start))
    print(f"fim da mineração. A mineração levou: {total_time} segundos")
    print(new_hash)