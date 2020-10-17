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
