
# Eletator Sim

 Implementation of an elevator software that handles multiple calls, using a producer-consumer approach. 

## Running

Just run the script in the terminal.
  
## How It Works

There are two threads that run in an infinite loop: a producer, that always waits for floor requests, and a consumer, that reads the requested floors and moves the elevator accordingly.  

To store the requested floors, two ordered arrays are used. When a new floor is requested, the floor number is inserted in the respective array, depending if the elevator is going up or down. The "requests up" array stores the floors that are above the current floor and always keep an ascending order. The "requests down" array stores the floors that are below the current floor and always keep an descending order.

The elevator will always keep moving while there are requested floors in any of the arrays. Otherwise, it will halt and wait for new requests. The current floor and the direction is stored so we know where to move the elevator. It always start at floor 0 and its direction facing up. As every request will be ordered, the elevator will respect the following logic:  

* If there are no more floors to visit, the elevator will halt on its current floor;
* For every new floor request:
    * If the requested floor F is equal to the current floor C, nothing will happen;
	* If the elevator is going up:
	    * If the requested floor F is above the floor C, it will be stored in the "requests up" array, and the elevator will go up until the requested floor is reached;
	    * If the requested floor F is below the current floor C, it will the stored in the "requests down" array, and will remain in the array until the elevator starts consuming that array;
      * If the elevator reached the last value of the array, and no more upper floors were requested, the elevator's direction is reversed and will start to consume the "requests down" array;
	 * If the elevator is going down:
		* If the requested floor F is below the current floor C, it will be stored in the "requests down" array, and the elevator will go down until the requested floor is reached;
	    * If the requested floor F is above the current floor C, it will be stored in the "requests up" array andwill remain in the array until the elevator starts consuming that array;
	   * If the elevator reached the last of the array, and no more lower floors were requested, the elevator's direction is reversed and will start to consume the "requests up" array;
  * If a new floor is requested while the elevator is moving, it will be added to the array respecting the logic above.