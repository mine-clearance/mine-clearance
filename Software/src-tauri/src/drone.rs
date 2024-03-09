// drone.rs
//
// This module defines the Drone struct and its associated methods. It represents the state
// and behavior of the drone, including its telemetry data like position, battery level, and speed.
//
// Responsibilities of the drone module:
// - Maintaining and updating the state of the drone.
// - Providing methods to access and modify drone attributes.

pub struct Drone {
    position: (f64, f64),
    battery: f32,
    height: f32,
    current_speed: f32,
    obstacle_detected: bool,
}

impl Drone {
    pub fn new() -> Self {
        Self {
            position: (0.0, 0.0),
            battery: 100.0,
            height: 0.0,
            current_speed: 0.0,
            obstacle_detected: false,   
        }
    }

    /// Retrieves the drone's battery level.
    pub fn get_battery_level(&self) -> f32 {
        self.battery
    }

    /// Determines if the drone has sufficient battery to continue operation.
    pub fn has_sufficient_battery(&self) -> bool {
        self.battery > 10.0 // Example threshold
    }

    /// Retrieves the current position of the drone.
    pub fn get_position(&self) -> (f64, f64) {
        self.position
    }

    /// Retrieves the drone's current speed.
    pub fn get_speed(&self) -> f32 {
        self.current_speed
    }

    /// Checks if the drone has detected an obstacle.
    pub fn obstacle_detected(&self) -> bool {
        self.obstacle_detected
    }
}