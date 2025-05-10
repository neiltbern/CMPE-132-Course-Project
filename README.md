# CMPE-132-Course-Project

This project implements a Machine Learning-based Intrusion Detection System (IDS) using the **TON_IoT Weather dataset**. Our system is designed to detect common cybersecurity threats targeting IoT environments, such as DDoS, Backdoor, Injection, and Ransomware attacks, using telemetry data collected from weather sensors. The goal of our project is to design and implement a lightweight IDS that generalizes and detects certain attack patterns.

## Dataset Overview

The following features and descriptions are included in the TON_IoT Weather activity dataset used for training and evaluation:

### Dataset Features

| Feature                         | Description                                                                 |
|----------------------------------|-----------------------------------------------------------------------------|
| date                            | Date of logging IoT telemetry data                                          |
| time                            | Time of logging IoT telemetry data                                          |
| temperature                     | Temperature measurements of a weather sensor linked to the network                                 |
| pressure                        | Pressure readings of a weather sensor linked to the network                                |
| humidity                        | Humidity readings of a weather sensor linked to the network                                         |
| label                           | Tag normal and attack records, where 0 indicates normal and 1 indicates attacks    |
| type                            | Tag attack categories, such as normal DoS, DDoS, and backdoor attacks, and normal records        |

### Dataset Class Distribuition

| No of rows            | Type                             |
|-----------------------|----------------------------------|
| 35000                 | normal                           |
| 5000                  | password                         |
| 5000                  | ddos                             |
| 2865                  | ransomware                       |
| 5000                  | injection                        |
| 5000                  | backdoor                         |

> Note: 'xss' and 'scanning' attack types were excluded due to insufficient sample size.
