from Session10 import FastTag, Vehicle
from Session10A import TollPlazaQueue

def main():
    
    """
    fasttag1 = FastTag(
            fasttag_id=4019, 
            bank='SBI', 
            balance=500)

    vehicle1 = Vehcile(
        registration_number='PB10AL2937', 
        type='4W', 
        fasttag=fasttag1
        )
    """

    vehicle1 = Vehicle(
        registration_number='PB10AL2937', 
        type='4W', 
        fasttag=FastTag(
            fasttag_id=4019, 
            bank='SBI', 
            balance=500)
        )
    
    vehicle2 = Vehicle(
        registration_number='KA12KC1212', 
        type='4W', 
        fasttag=FastTag(
            fasttag_id=7890, 
            bank='ICICI', 
            balance=600)
        )
    
    vehicle3 = Vehicle(
        registration_number='HR20AB1122', 
        type='4W', 
        fasttag=FastTag(
            fasttag_id=6609, 
            bank='ICICI', 
            balance=50)
        )
    
    vehicle4 = Vehicle(
        registration_number='PB10KC1220', 
        type='4W', 
        fasttag=FastTag(
            fasttag_id=5152, 
            bank='SBI', 
            balance=1000)
        )
    
    vehicle5 = Vehicle(
        registration_number='PB10BD3027', 
        type='2W', 
        fasttag=FastTag(
            fasttag_id=2234, 
            bank='SBI', 
            balance=200)
        )



    queue = TollPlazaQueue()
    queue.add(vehicle1)
    queue.add(vehicle2)
    queue.add(vehicle3)
    queue.add(vehicle4)
    queue.add(vehicle5)

    queue.show()

    # After adding Vehcile in Queue, deduc the toll
    queue.deduct_toll(vehicle1)
    queue.deduct_toll(vehicle2)
    queue.deduct_toll(vehicle3)
    queue.deduct_toll(vehicle4)
    queue.deduct_toll(vehicle5)

    print(f'Size of Queue is: {queue.size}')

    # Assignment: Write the Logic, if balance is low, highlight the vehcile 
    # and do not remove from queue


if __name__ == '__main__':
    main()