
[📄 Course Syllabus](https://cdn.sanity.io/files/tlr8oxjg/production/8f97c1ba0a177b52227fed6d0fa36b2a9296ddc2.pdf)

# Self-Driving Car Engineer Nanodegree

## Course 1: Computer Vision

In this course, learners develop critical machine learning skills commonly leveraged in autonomous vehicle engineering. Topics include:

- ML project lifecycle: framing problems, selecting metrics, training/improving models
- Working with camera sensors and digital image processing
- Building CNNs using TensorFlow
- Image classification and object detection

### 📌 Project: Object Detection in an Urban Environment

Create a CNN to detect and classify objects using the Waymo Open Dataset.

- Analyze urban environment images (cyclists, pedestrians, vehicles)
- Perform data augmentation
- Train and monitor the model using TensorBoard
- Experiment with hyperparameters for performance improvement

### 🧠 Lessons

#### Lesson 1: The Machine Learning Workflow

- Identify ML stakeholders
- Frame ML problems and choose appropriate metrics
- Perform EDA and visualize image data

#### Lesson 2: Sensor & Camera Calibration

- Calibrate images using checkerboard patterns
- Apply geometric and pixel-level transformations

#### Lesson 3: From Linear Regression to Feedforward Neural Networks

- Implement logistic regression and backpropagation in TensorFlow
- Build custom neural networks

#### Lesson 4: Image Classification with CNNs

- Design custom CNN architectures
- Apply augmentations and regularization
- Calculate output shape and parameter count

#### Lesson 5: Object Detection in Images

- Use TensorFlow Object Detection API
- Choose models and optimize training
- Implement non-max suppression and mAP calculation

---

## Course 2: Sensor Fusion

Learn about sensor fusion, a key enabler for robust and reliable self-driving technology.

- Understand lidar sensors and data processing
- Perform 3D object detection with deep learning
- Fuse camera and lidar data
- Implement multi-target tracking with an Extended Kalman Filter

### 📌 Project 1: 3D Object Detection

- Load and preprocess 3D lidar point clouds
- Detect and classify vehicles and pedestrians
- Evaluate performance using key metrics

### 📌 Project 2: Sensor Fusion

- Fuse lidar and camera data for multi-target tracking
- Implement Extended Kalman Filter with track management and data association
- Use a real-world dataset for evaluation and visualization

### 🧠 Lessons

#### Lesson 1: Introduction to Sensor Fusion & Perception

- Compare sensor strengths and weaknesses

#### Lesson 2: The Lidar Sensor

- Extract and visualize lidar data from the Waymo dataset

#### Lesson 3: Detecting Objects in Lidar

- Transform point clouds to BEV images
- Run inference and evaluate performance

#### Lesson 4: Kalman Filters

- Track objects over time using linear Kalman filters

#### Lesson 5: Extended Kalman Filters

- Derive Jacobians and implement measurement models
- Fuse camera and lidar data

#### Lesson 6: Multi-Target Tracking

- Track management and association using gating methods
- Evaluate using RMSE and detection probability

---

## Course 3: Localization

Learn how to estimate vehicle position using motion models and lidar-based point clouds.

- Understand the bicycle motion model
- Implement Markov Localization
- Use scan matching techniques (ICP, NDT) with PCL
- Localize vehicles in CARLA simulator

### 📌 Project: Scan Matching Localization

- Recover a simulated car's position using ICP or NDT
- Maintain accurate location tracking in a simulated drive

### 🧠 Lessons

#### Lesson 1: Introduction to Localization

- Use GPS or detected objects to estimate location
- Predict location with motion models

#### Lesson 2: Markov Localization

- Apply Bayes/Markov filters in 1D using C++

#### Lesson 3: Creating Scan Matching Algorithms

- Implement ICP and NDT for 2D localization in C++

#### Lesson 4: Utilizing Scan Matching in 3D

- Align 3D point clouds and create maps in CARLA

---

## Course 4: Planning

Learn path planning from point A to B, including emergency reactions and urban navigation.

- Predict behaviors using model-driven/data-driven approaches
- Implement behavior planners using finite state machines
- Generate collision-free, optimal paths

### 📌 Project: Motion Planning & Decision Making

- Implement behavior and motion planners
- Avoid static objects and navigate intersections
- Execute maneuvers like lane change or nudge

### 🧠 Lessons

#### Lesson 1: Behavior Planning

- High-level planning for autonomous vehicles

#### Lesson 2: Trajectory Generation

- Use C++ and Eigen to build candidate trajectories

#### Lesson 3: Motion Planning

- Plan motion in urban environments with constraints
- Navigate safely and human-like in simulations

---

## Course 5: Control

Control the vehicle to follow a planned trajectory using feedback control techniques.

- Understand and implement PID controllers
- Compare with advanced controllers like MPC

### 📌 Project: Control & Trajectory Tracking

- Implement a PID controller in C++ to track a vehicle’s trajectory
- Test in the CARLA simulator
- Understand control limitations and robustness

### 🧠 Lessons

#### Lesson 1: PID Control

- Design PID and MPC controllers
- Choose parameters for stability and performance
- Evaluate robustness in real-world scenarios

---

## 🛠️ Tools & Frameworks Used

- TensorFlow
- CARLA Simulator
- C++
- Eigen
- PCL (Point Cloud Library)
- Waymo Open Dataset

---

## 🎓 Outcome

By completing this program, learners will be equipped to work as autonomous systems engineers, specializing in areas such as computer vision, sensor fusion, localization, planning, and control.

