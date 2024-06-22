# TailscaleNetBox
TailscaleNetBox is a Windows application designed to manage multiple Tailscale VPN networks in isolated environments. It allows you to connect to and manage routers using WinBox from anywhere in the world.

## Features
Add and connect to multiple Tailscale VPN networks.
Launch WinBox to manage routers in each Tailscale network.
Simple and intuitive GUI for network and WinBox management.

## Installation
Clone the repository:
git clone https://github.com/StaticTesseract07/TailscaleNetBox.git
cd TailscaleNetBox

### Install dependencies:
pip install -r requirements.txt

## Requirements
Python 3.x
PyQt5
Tailscale
WinBox

## Usage

### Run the application:
python main.py

### Adding a Tailscale Network:
Enter the Tailscale network key in the provided input field.
Click on “Add Tailscale Network” to add the network.
Connecting to a Tailscale Network:
Select a network from the list.
Click on “Connect Selected Network” to establish the VPN connection.
### Managing with WinBox:
After connecting to a Tailscale network, select it from the list.
Click on “Launch WinBox” to open WinBox for managing routers in the selected network.

## Screenshots

### About the Author
This project is developed by Mihir Parmar
