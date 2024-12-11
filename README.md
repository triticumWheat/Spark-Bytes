# Spark! Bytes

## Overview
Spark Bytes is a web application designed for Boston University students and faculty to post events that offer free food or snacks. The goal is to minimize food waste by making surplus food from events more accessible to the BU community. This initiative not only helps students find free food but also promotes sustainability by reducing the waste generated from over-purchasing food for campus events.

## Features
- **User Authentication**  
  Users can register, log in, and manage their profiles. In addition to traditional email and password authentication, the application integrates with **Auth0** for secure and seamless third-party authentication. This allows users to log in using services like Google, Facebook, or other supported providers.

- **Event Posting and Allergy Information**  
  Organizers can create event posts with details like time, location, type of food, and any additional information such as allergy warnings or dietary options (e.g., nut-free, gluten-free, vegan). This ensures attendees are informed and can choose events that suit their dietary needs.

- **Event Discovery**  
  Students and faculty can browse upcoming events offering free food using an intuitive interface.

- **Registration and QR Codes**  
  When users sign up for an event, they receive an email confirmation that includes a QR code. This QR code can be scanned at the event for easy check-in and tracking attendance.

- **Interactive Map**  
  Users can view events on an integrated map, making it easy to locate nearby events and navigate to them.

- **Sustainability Focus**  
  Designed to help minimize food waste by ensuring leftover food is consumed rather than discarded.


## Prerequisites
python 3.10

## Installation

1. Clone the repository:
    To clone the repository, replace `<USERNAME>` with your GitHub username:

    ```bash
    git clone https://github.com/<USERNAME>/Spark-Bytes.git
    cd Spark-Bytes

2. Create Venv (Optional):
    ```bash
    python3.10 -m venv venv
    source venv/bin/activate 

3. Install Depdencies:
    ```bash
    pip install -r requirements.txt

## Running the application

1. Run the application:
    ```bash
    python3 manage.py runserver

2. Open web browser
    Visit: http://127.0.0.1:8000/

## Deployment

visit https://sparkbytes-cbcb12916fe3.herokuapp.com/

## Presentation link
https://docs.google.com/presentation/d/1WUJ4NKX85KHb8Ybb-ZKkAWRyvcUgOTfjAsP78a053Vw/edit?usp=sharing

## Future Enhancements
- **Enhanced Authentication Options**  
  Expanding the use of **Auth0** to include additional third-party providers and multi-factor authentication (MFA) for improved security.

- **Mobile App Integration**  
  Developing a dedicated mobile app for iOS and Android to enhance accessibility and user experience.

- **Real-Time Event Updates**  
  Adding real-time notifications for new or nearby events, dynamically updating event details and availability.

- **Personalized Recommendations**  
  Implementing machine learning to suggest events based on user preferences, location, and past activity.

- **Gamification Features**  
  Introducing a rewards system for users who frequently attend events or post events, fostering greater engagement.

- **Food Analytics Dashboard**  
  Providing organizers with insights into food waste reduction, attendance statistics, and feedback to improve future events.

- **Community Collaboration**  
  Allowing users to collaborate by pooling leftover food from smaller events or individual contributions, expanding the reach of the platform.
