/*
Some clarifying questions.

1) Are we going to have some kind of payment system?
  - if so then we will need to implement some kind of variable within either
    the Admin class or the ParkingLot class that will check how long a car
    has been parked.
2) Is the parking lot only for Cars? i.e. can we have other types of vehicle?
  - if so then we will need to create a vehicle class. And all other types of
    vehicles like car, trucks, motorcylce, etc. will extend this class.
3) Can we add additional parking spots?
  - if so, then in the parking lot class, we will need to treat the grid as an
    2D arraylist. 
*/


// this is the actual parking lot.
// we will use a 2D array of RegularSpot to represent the parking lot
public class ParkingLot {
	private Admin admin;
	private RegularSpot[][] grid;
	private boolean turnOnLights;

	public ParkingLot(int d) {
		this.grid = new RegularSpot[d][d];
		this.admin = new Admin(d * d);
		this.turnOnLights = true;
	}
	// whatever car is in the parking lot, charge them
	// as long as they are parked.
	public void charge() {
	}
	// simply turn off the lights
	public void turnLightsOff() {
	}
	// simply turn on the lights
	public void turnLightsOn() {
	}
}


public class Car {
	// car has two variables license and type.
	// license will be used to see if the car is allowed to park in the parking lot
	// type will be used to determine where the car can park.

	private int license;
	private String type;

	// default constructor
	public Car() {
		this.license = 0;
		this.type = "INVALID";
	}

	// constructor with license and type as parameter.
	// Parking admin can use this to register new cars in the system
	public Car(int license, String type) {
		this.license = license;
		this.type = type;
	}

	// this function will be used to park a car.
	// license will be used to make sure car is registered within the system
	// type will be used to park in appropriate parking spot
	public void park() {
	}

	// will be used to exit a parking spot and eventually out of the parking lot
	public void unPark() {
	}
}


import java.util.ArrayList;

public class Admin {

	// admin has two variables
	// an arraylist of registeredCars that will store all the cars that
	// are registered within the system.
	// capacity, which will determine the max number of cars
	// that can be registered.
	private ArrayList<Car> registeredCar;
	private int capacity;

	// constructor
	public Admin(int capacity) {
		this.capacity = capacity;
		this.registeredCar = new ArrayList<Car>();
	}

	// will be used to register a car, making sure capacity is not exceeded
	public void register(Car c) {
	}

	// will be used to make valid cars parked in the parking lot
	public boolean checkRegistration(Car c) {
		return false;
	}

	// if a car is parked and not registered, tow em!
	public void towCar(Car c) {
	}
}


// compact spot IS-A regular spot but for compact cars
public class CompactSpot extends RegularSpot {
	// type is set type to "ANY"
	// isOccupied will be used to check whether the spot is taken
	private Spot type;
	private boolean isOccupied;

	// constructor
	// when declaring type, we will use the SPOT enum
	public CompactSpot() {
		this.type = Spot.COMPACT;
		this.isOccupied = false;
	}

	// this will be used to check whether the car can park
	public boolean checkCar(Car c) {
		return false;
	}
}

// this enum will be used to classify parking spot type.
// will be used
public enum Spot {
	LARGE, DISABLE, EMERGENCY, SPECIAL, RESERVED, COMPACT, REGULAR
}


// regular spot is parking lot spot that can hold any car
public class RegularSpot {

	// type is set type to "ANY"
	// isOccupied will be used to check whether the spot is taken
	private Spot type;
	private boolean isOccupied;

	// constructor
	// when declaring type, we will use the SPOT enum
	public RegularSpot() {
		this.type = type.REGULAR;
		this.isOccupied = false;
	}

	// will be used to fill the spot
	public void fill() {
	}

	// will be used to unfill the spot
	public void unFill() {
	}
}
