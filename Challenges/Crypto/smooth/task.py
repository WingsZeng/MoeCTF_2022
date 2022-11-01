from Crypto.Util.number import sieve_base,isPrime,getPrime
import random
from secret import flag

def get_vulnerable_prime():
    p=2
    while True:
        for i in range(136):
            smallp=random.choice(sieve_base)
            p*=smallp
        if isPrime(p+1):
            return p+1

P=get_vulnerable_prime()
Q=getPrime(2048)
N=P*Q
e=0x10001

for i in range(1,P-1729):
    flag=flag*i%P

c=pow(flag,e,N)
print("c=",hex(c))
print("N=",hex(N))

'''
c= 0x3cc51d09c48948e2485820f6758fb10c7693c236acc527ad563ba8369c50a0bc3f650f39a871ee7ef127950ed916c5f4dc69894e11caf9d178cd7e8f9bf9af77e1c69384cc5444da64022b45636eeb5b7a221792880dd242be2bb99be3ed02c430c2b77d4912bec1619d664e066680910317c2bb0c87fafdf25f0a2400103278f557b8eca51d3b67d61098f1ab68da072bb2810596180afbc81a840cd24efef4d4113235160e725a5af4824dc716d758b3bc792f2458e979398e001b27e44d21682e2ef80ae94e21cd09a12e522ca2e569df72f012fa40341645445c6e68c6233a8a39e5b91eb14b1ccfa61c9bad25e8e3285a22da27cd506ddd63f207517a4e8ede00b104d8806ff4c0e3162c3de69169d7e584952655272b96d39d242bb83019c7eab1ceb0b4b287591e1e0a5b6378e70340a82d3430c5925d215f31fda6d9d0bccea240591b22a3d0f6b5bf4ddf1243d71aca0fd53045c352c8c5497ebcdbd7ac11083d63aba7c053604fda2430c317a4e04702b5ad539e110f101165b21dcd9fdb5ba7324acdba6a506244ce7c911197dfe067441fe7488d164c050f45ef6476aaf399cedde1793cceb8c21d88ec8ecf5e17df27586713d7dd9566ec5023cfef75422b73e2d5a932c661b3cfdf9c4bda12b64380d2be1aa957c3e1416e068937bafe79b8cf303296792388e9c197702e11e7ded6088ae992d352b23a4a27
N= 0xdc77f076092cbe81c44789ccfc1b2ca55eabae65f44cf34382799e8bbb42d4d6c032bd897c21df1da401929d82deb56264823a757f6cacf63e0037146026cbab32ab9e4abc783dcabaac2b7ccc439937be3ab0fbf149524ff29ef0fe6f27e45215d74b40597c70e8207159dc7f542c2a6828500016480053dfc2d8dbf8fcdf6700640184c8f3318f7aab2e17e116edf680592f5eae951159bb8c20cfbd0cbab8b4b95925b5068038d0377a55a4d346ebbf53a1c2943b7c17e1b9d4a1b77916da2e15140b05b96655906942a07d04b7e25fa7521b3b7ae26eda68375a8b8ef2d5b4704a28168b236de97f24a663f0d0a3aeab47767dfe75a21662f5f25ef7f7d4b25c90fd7bcdd7137c23f03b6ea4209f8fb9b4628355e6ad62e6467d26666d3d1b0e6f078c5f3866413a6fcd3c1dc2ff3a5ab286e339d5c72f4d2f0473a4faddcba6b031bb6ec226fd4b319834b5029f09ea0ffeb5b6ed182d5a13675571b6708c38299118043390343e2f79edebd2ae0e0a765a3aebf776f54ca983cdae8547547cfc8430f7222aefa77301d7cc7c03b1451b6603028b21fea869d35138a9c83919985a91b3fdfa934f25a442cc10349b0ed6f2ee3955d40249e8b3fb9f1955534ee06cee41a3ad2d6ff7dbdb0f01e47b9e4d04f65232f5579135ae035e8ba2d1fe6465a730dcc8b9ba3a558ab38f040ea510757d25e92f886c50c24ad967f1
'''