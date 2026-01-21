# Assignment_1_PWM
Assignment 1: GPIO-Based PWM on the PYNQ-Z2

Author: Anthony Betancourt
Lab Group: 3
Platform: PYNQ-Z2

1. Purpose

This repository contains the implementation for Assignment 1, which introduces GPIO control, software-based Pulse Width Modulation (PWM), and asynchronous programming on the PYNQ-Z2 platform. The work establishes foundational skills required for subsequent laboratory assignments.

2. System Description

The PYNQ-Z2 board integrates a Zynq Processing System (PS) with Programmable Logic (PL). Peripheral devices (LEDs, buttons, PMOD headers) are controlled via GPIO IP blocks defined in the FPGA overlay. The base overlay is used throughout this assignment to provide GPIO access.

3. PWM Implementation

PWM is implemented in software by toggling a GPIO pin at a fixed frequency while varying the duty cycle. This approach emulates analog voltage behavior using digital outputs.

PWM frequency was experimentally selected to eliminate visually perceptible flicker

Duty cycle was varied to control LED brightness

Edge cases at 0% and 100% duty cycle were handled explicitly

A conceptual illustration of PWM duty cycle variation is shown in Figure 1 of the report.

4. Brightness Perception Analysis

The perceived brightness of an RGB LED was evaluated as a function of PWM duty cycle. Due to the non-linear response of human vision, perceived brightness does not scale linearly with duty cycle.

Experimental brightness estimates are summarized in Table 1 of the report

The relationship between perceived brightness and duty cycle is shown in Figure 2

Results are discussed using the Weber–Fechner law

5. Asynchronous Control and Button Interface

Asynchronous programming (asyncio) was used to allow concurrent LED blinking and button monitoring.

LED blinking at 1-second intervals using a fixed duty cycle

Button-based color selection (Red, Green, Blue)

Button-based termination of blinking behavior

A functional demonstration is provided in the accompanying video and referenced in Figure 3 of the report.

6. Repository Structure
.
├── notebooks/
│   └── Assignment1.ipynb
├── src/
│   ├── gpio_reset.c
│   └── pwm_control.py
├── report/
│   └── Assignment_1_Report.pdf
├── video/
│   └── demo_link.txt
└── README.md

7. Execution Notes

The FPGA bitstream is loaded using the base overlay prior to GPIO operation. Notebook cells should be executed sequentially to ensure proper initialization.

8. References

DeepBlue Embedded, Pulse Width Modulation (PWM) Tutorial.

Acuity Brands, Why You Need Dimming Curves.