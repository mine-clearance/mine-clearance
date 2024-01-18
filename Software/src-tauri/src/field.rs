// fields.rs
//
// The fields module is responsible for managing information about the operational field or area
// where the drone is operating. This includes details like terrain coordinates and marked mines.
//
// Key functionalities:
// - Storing and managing the field's terrain coordinates and marked mines.
// - Providing methods to access and update field-related information, such as adding new marked mines.

use std::collections::HashSet;

/// Represents a coordinate on the field.
pub type Coordinate = (f64, f64);
/// Represents a set of coordinates marking mines.
pub type MineField = HashSet<Coordinate>;

/// The `Field` struct holds terrain information, including locations of potential mines.
pub struct Field {
    terrain_coordinates: Vec<Coordinate>,
    mine_field: MineField,
}

impl Field {
    /// Creates a new `Field` with no terrain data or mine markings.
    pub fn new() -> Self {
        Self {
            terrain_coordinates: Vec::new(),
            mine_field: MineField::new(),
        }
    }

    /// Adds a new terrain coordinate to the field.
    pub fn add_terrain_coordinate(&mut self, coord: Coordinate) {
        self.terrain_coordinates.push(coord);
    }

    /// Returns a reference to the terrain coordinates.
    pub fn terrain_coordinates(&self) -> &Vec<Coordinate> {
        &self.terrain_coordinates
    }

    /// Marks a potential mine location on the field.
    pub fn mark_mine(&mut self, mine_coord: Coordinate) -> bool {
        self.mine_field.insert(mine_coord)
    }

    /// Returns a reference to the marked mines.
    pub fn marked_mines(&self) -> &MineField {
        &self.mine_field
    }

    /// Checks if a given coordinate is marked as a mine.
    pub fn is_mine_marked(&self, coord: &Coordinate) -> bool {
        self.mine_field.contains(coord)
    }
    
    // Additional functionality can be added to handle areas of the field such as regions to avoid,
    // generating pathfinding graphs, and other analyses pertinent to the drone’s operation.

    // The following functions are placeholders for potential future features related to field analysis
    // and drone navigation aid:
    //
    // fn generate_pathfinding_graph(&self) { ... }
    // fn analyze_terrain(&self) { ... }
}