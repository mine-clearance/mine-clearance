// communication.rs
//
// This module handles the communication between the software and the drone
// including sending commands to the drone and receiving telemetry data from it.
//
// The communication module's main responsibilities are:
// - Managing the transmission of commands from the software to the drone.
// - Receiving and processing data sent from the drone back to the software.
// - Ensuring reliable and efficient communication protocols are used.

use std::io::{self,BufReader,BufRead, Write};
use std::net::{TcpStream, ToSocketAddrs};

pub struct Communication {
    stream: TcpStream,
}

impl Communication {
    pub fn new<A: ToSocketAddrs>(addr: A) -> std::io::Result<Self> {
        let stream = TcpStream::connect(addr)?;
        Ok(Self { stream }) // testing if the variable exists with the right type
    }

    pub fn send_command(&mut self, command: &str) -> std::io::Result<()> {
        let message = format!("{}\n", command); // Append delimiter to denote message end
        self.stream.write_all(message.as_bytes()) // Send the command as bytes
    }

    pub fn receive_data(&mut self) -> std::io::Result<String> {
        let mut reader = BufReader::new(&mut self.stream);
        let mut message = String::new();
        reader.read_line(&mut message)?;
        Ok(message.trim_end().to_string()) // Remove trailing newline and test if the variable exists with the right type
    }
}