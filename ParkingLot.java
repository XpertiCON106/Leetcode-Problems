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
