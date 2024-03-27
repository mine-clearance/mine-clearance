// mod control;
// mod drone;
// mod fields;
// mod communication;

// // main.rs
// //
// // This is the entry point of the drone control software. It initializes the system components
// // and contains the main event loop. This file orchestrates the high-level flow of the program
// // by coordinating with other modules like control, drone, fields, and communication.
// //
// // main.rs is responsible for:
// // - Initializing system components (e.g., DroneControl).
// // - Running the main event loop where the system state is continuously updated.


// // Prevents additional console window on Windows in release, DO NOT REMOVE!!
// #![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]



// fn main() {
//     let mut drone_control = control::DroneControl::new();
    
//     // Example of main loop
//     loop {
//         drone_control.update();
//         // Include additional logic as needed
//     }
// }

#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

fn main() {
tauri::Builder::default()
   .run(tauri::generate_context!())
   .expect("error while running tauri application");
}