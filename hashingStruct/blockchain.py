from hashlib import sha256


class Blockchain:
    def __init__(self,prev_Block_hash,transaction_list) -> None:
        self.prev_Block_hash=prev_Block_hash
        self.transaction_list=transaction_list

        self.block_data="-".join(transaction_list)+"-"+prev_Block_hash
        self.block_hash=sha256(self.block_data.encode()).hexdigest()

t1 = "tina sends 2 bitcoin to BOB"
t2 = "BOB sends 4.2 bit coins to mike "
t3 = "Mike sends 5.5 bitcoins to BOB"
t4 ="Ashely sned 0.3 bitcoin to tina"
t5= "mike sends 1 BITcoin to charlie"
t6 = "Mike sends 5.4 Bitcoin to Daniel"

intitial_block =Blockchain("Initial string",[t1,t2])
print(intitial_block.block_data)
print(intitial_block.block_hash)

second_block =Blockchain(intitial_block.block_hash,[t3,t4])
print(second_block.block_data)
print(second_block.block_hash)

third_block =Blockchain(second_block.block_hash,[t5,t6])
print(third_block.block_data)
print(third_block.block_hash)
