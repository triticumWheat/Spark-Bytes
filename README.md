# Spark! Bytes Project Plan

## Part 1: Requirements

### 1. Project Overview

* __Project Name:__ Spark! Bytes
* __Date:__ Oct 17, 2024
* __Author:__ Shangmin Chen, Shaozhe Zhang, Mingyuan Sun, Christian Kraus, Zander Reid
* __Purpose:__ Spark Bytes is a web application designed for Boston University students and faculty to post events that offer free food or snacks. The goal is to minimize food waste by making surplus food from events more accessible to the BU community. This initiative not only helps students find free food but also promotes sustainability by reducing the waste generated from over-purchasing food for campus events.
* __Stakeholders:__ BU Students, BU Event organizers.

### 2. Scope of Work

* __Problem/Opportunity:__ High-level description of the problem or opportunity the software addresses.
* __Use Cases:__ One or two simple user stories for critical features (e.g., "As a user, I want to [do X] so I can [achieve Y]").

### 3. Functional Requirements

* **Key Features:**
  * **Login Authentication:**  
    Restricts access to BU students and faculty through BU Kerberos login to ensure only authorized users can claim food.
  
  * **One-Time Claim System:**  
    Implements a boolean flag initialized as True, allowing each student ID to claim food once per event. After claiming, the flag is set to False to prevent multiple claims.
  
  * **Event Posting Form:**  
    Allows faculty and students to post events with details on leftover food, including time, location, and type of food.
  
  * **Event Browser:**  
    Enables users to browse through events offering leftover food or upcoming events that will have food available.
  
  * **Search Functionality:**  
    Users can search for events by food type, location, and time.

* **Additional Features:**
  * **Notifications:**  
    Sends real-time alerts to users when new events with available food are posted.
  
  * **Event Expiration:**  
    Automatically removes events from the browse and search sections once the specified time frame expires.
  
  * **Edit/Delete Posting:**  
    Event organizers can edit the event details or delete posts once the food is fully claimed.
  
  * **Map Integration:**  
    Uses the Google Maps API to display event locations based on the user’s current location.

  * **Security:**
    * **CSRF Protection:** Prevents cross-site request forgery (CSRF) attacks by using secure tokens.
    * **Input Filtering:** Prevents SQL injection and cross-site scripting (XSS) attacks by filtering user inputs.
 
### 4. Non-Functional Requirements

* __Usability:__ The interface should be intuitive, user-friendly, and accessible across devices, including desktops and mobile platforms. The design should prioritize ease of use for all types of users.
* __Performance:__ Spark Bytes should have minimal downtime and be capable of handling high traffic. Updates and data synchronization must happen in real-time to ensure accuracy for users looking for events with available food.
* __Security:__ Only BU students and faculty with valid BU Kerberos authentication will have access. All data exchanges must be encrypted via HTTPS, and user information should be securely stored in a protected database.

### 5. Technical Requirements

* __Platform(s):__ The app will be available via a webpage, and accessible for both iPhone and Android.
* __Integrations:__ Google Maps for map integration.

### 6. Constraints and Assumptions

* __Constraints:__ Time constraint, development time limited by time within the fall 2024 semester.
* __Assumptions:__ Assuming all BU students have BU Kerberos login and BU students have a computer or phone.

### 7. Risks

* __Risks:__
  * Low postings for leftover food.  
    **Mitigation:** Utilize social media to spread awareness of the app.
  * Inaccurate posting/abuse.  
    **Mitigation:** Utilize a reporting system that flags users who are using the app inappropriately.

---

## Part 2: Resources

### Role/resource assignment:
This is an example that your team should fill in with the specifics about your plan.

| Name         | Roles                                                       |
|--------------|-------------------------------------------------------------|
| Shangmin     | Developer or Develops Module n                              |
| Name         | Designer, Frontend, Assets                                  |

---
