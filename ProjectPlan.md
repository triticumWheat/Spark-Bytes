# Spark! Bytes Project Plan

## Part 1: Requirements

### 1. Project Overview

* __Project Name:__ Spark! Bytes
* __Date:__ Oct 17, 2024
* __Author:__ Shangmin Chen, Shaozhe Zhang, Mingyuan Sun, Christian Kraus, Zander Reid
* __Purpose:__ Spark Bytes is a web application designed for Boston University students and faculty to post events that offer free food or snacks. The goal is to minimize food waste by making surplus food from events more accessible to the BU community. This initiative not only helps students find free food but also promotes sustainability by reducing the waste generated from over-purchasing food for campus events.
* __Stakeholders:__ BU Students, BU Event Organizers, BU Sustainability Office.

### 2. Scope of Work

* __Problem/Opportunity:__ Leftover food from on-campus events is a problem for event organizers, resulting in unnecessary waste that could otherwise be used to feed students. Spark Bytes offers a solution by helping event organizers feed hungry students by post event details, such as the type of food available, how much is left, and how long it will be accessible for. Spark Bytes is an opportunity to improve campus suitability, waste, and most importantly, it helps feed hungry stomachs!
* __Use Cases:__ As a student, I want to find leftover food from events so that I can have a free meal. As an event organizer, I want to post leftover food from my event so that it doesn’t go to waste.

### 3. Functional Requirements

* **Key Features:**
  * **Login Authentication:**  
    Restricts access to BU students and faculty through BU Kerberos login to ensure only authorized users can claim food.
  
  * **One-Time Claim System (Optional):**  
    Implements a boolean flag initialized as True, allowing each student ID to claim food once per event. After claiming, the flag is set to False to prevent multiple claims.
  
  * **Event Posting Form:**  
    Allows faculty and students to post events with details on leftover food, including time, location, type of food, and quantity estimate.
    Fields include:
             * Event Title
             * Description
             * Food Type
             * Quantity Estimate
             * Location (with map integration)
             * Time Available (start and end times)
             * Optional Contact Information
  
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
    Shows user's current location for proximity awareness.
    Provides directions to event locations.

  * **Security:**
    * **CSRF Protection:** Prevents cross-site request forgery (CSRF) attacks by using secure tokens.
    * **Input Filtering:** Prevents SQL injection and cross-site scripting (XSS) attacks by filtering user inputs.
    * **Data Encryption:** All data exchanges are encrypted via HTTPS.
 
### 4. Non-Functional Requirements

* __Usability:__ The interface should be intuitive, user-friendly, and accessible across devices, including desktops and mobile platforms. The design should prioritize ease of use for all types of users.
* __Performance:__ Spark Bytes should have minimal downtime and be capable of handling high traffic. Updates and data synchronization must happen in real-time to ensure accuracy for users looking for events with available food.
* __Security:__ Only BU students and faculty with valid BU Kerberos authentication will have access. All data exchanges must be encrypted via HTTPS, and user information should be securely stored in a protected database.

### 5. Technical Requirements

* __Platform(s):__ The app will be available via a webpage, and accessible for both iPhone and Android.
* __Technology Stack:__
   * Front-End: React.js for building a dynamic and responsive user interface.
   * Back-End: Node.js with Express.js or Python with Django for server-side logic.
   * Database: PostgreSQL or MongoDB for data storage.
   * Authentication: Integration with BU's Kerberos authentication system.
   * APIs: Google Maps API for map functionalities.
                        
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
| Shangmin, Shaozhe     | Front & Backend, Tester                                                |
| Zander, Christian     | Frontend, Assets     		                             |
| Mingyuan     | Backend, Serverside, Tester							     |
| Everyone     | Team							     |

---

## Part 3: Tasks

### High-Level Project Plan Details
Expand this and add your details.

| Phase      | Deliverables                             | Tasks                                      | Timeline                                      | Resources               |
|------------|------------------------------------------|--------------------------------------------|-----------------------------------------------|-------------------------|
| Planning   | - Requirements & Scope Document          | - Define project goals, requirements, and stakeholders | Sprint 1 (Week 1)		     | Team                    |
|            | - Work Breakdown Structure (WBS)         | - Create WBS                               | Sprint 1	(Week 1)	  	  	     | Team                    |
| Design     | - System Design Document                 | - Conduct requirements gathering           | Sprint 2 (Week 2 - 3)			     | Team		       |
|            | - User Interface Prototypes              | - Create design specifications             | Sprint 2	(Week 2 - 3)	  		     | Team                    |
|            |                                          | - Develop prototypes                       | Sprint 3 - 5 (Week 4 - 6)    		     | Designers               |

### Further Details on Project Plan using an Agile Development Methodology

| Phase        | Deliverables                        | Tasks                                      | Timeline                                      | Resources               |
|--------------|-------------------------------------|--------------------------------------------|-----------------------------------------------|-------------------------|
| Development  | - Code Modules                      | - Write code                               | Sprint 3 - 6 (Week 4 - 7)		          | Developers, Testers     |
|              | - Unit Tests of Each Module         | - Conduct unit testing                     | Sprint 4 - 6 (Week 5 - 7)		          |                         |
|              |                                     | - Integrate modules                        | Sprint 6 (Week 7)			          |                         |
| Testing      | - Test Cases                        | - Develop test cases                       | Sprint 7 (Week 8)		         	  | Testers                 |
|              | - Test Reports                      | - Execute testing                          | Sprint 7 (Week 8 - 9)		          |                         |
|              | - Fixed Testing Problems            | - Analyze results and remediate problems   | Sprint 8 (Week 9)			          |                         |
| Deployment   | - Completed Web Application         | - Prepare deployment environment           | Sprint 10 (Week 10)			          | System Administrators   |
|              | - Deployment Plan                   | - Deploy software                          | Sprint 10 (Week 10)			          |                         |
|              | - User Manual, System Design, and Other Documentation | - Create documentation | Sprint 10 (Week 10)				  |                         |

---

### Tasks Assigned to Backlog
Create this specific to your project plan.

| ID  | Task                       | Description                                               | Sprint   | Status        |
|-----|----------------------------|-----------------------------------------------------------|----------|---------------|
| 1   | Create User Registration    | Design and implement a form for new users to sign up.      | 2        | Started   |
| 2   | Implement Login Functionality | Develop a login system for existing users.                | 3        | Started   |
| 3   | Integrate Food Registry     | Connect the platform to a payment processor.               | 4        | Not Started   |
| 4   | Design Dashboard Layout     | Create a visually appealing dashboard for users to view their data. | 4 | Not Started   |
| 5   | Develop Email Notifications | Set up email notifications for various events (e.g., new orders, password resets). | 5 | Not Started |
| 6   | Test User Interface         | Conduct usability testing on the user interface.           | 6        | Not Started   |
| 7   | Optimize Database Queries   | Improve the performance of database queries.               | 7        | Not Started   |
| 8   | Add Social Media Integration | Allow users to sign up or log in using social media accounts. | 8      | Not Started   |

---

## Part 4: Schedule

### Tasks in Backlog Assigned to Sprints

You should include in the backlog the planned Sprint(s) to do each task. Or this could be in a separate schedule.

### Sprint Plan

By following a structured sprint plan, teams can improve their productivity, reduce risk, and deliver higher-quality software. For every sprint, lay out the following in a short document:

**Sprint Goals (example):**
* Complete user registration and login.
* Create a basic user dashboard.
* Implement email notifications for password resets.

**Sprint Tasks from Backlog:**
List the tasks from the backlog to be implemented and by WHOM. Add columns as needed to help you manage this. Make sure to do this as a team and have each team member pick up and agree to their tasks.

### Additional Schedule Considerations:
1. **Sprint Length:** For the Spark!Bytes project, we use 1-week sprints. Industry-typical sprints can last from 1-4 weeks.
2. **Velocity:** The amount of work the team can consistently deliver in a sprint.
3. **Status Column:** Often included in what is called a Kanban Board, this is representative of the workflow, with statuses for "To Do," "In Progress," "Done," and others as needed.

---

## Part 5: Communications Plan

As a team, negotiate and agree on how you will communicate with each other.

### Regular Stand-ups:

Team members meet at a schedule you define to discuss their progress, blockers, and plans for the day. This helps identify issues early on so you can address them before they become too large. Often, there are daily standups, but since your project team is not full-time, you likely only want to do one to three per sprint.

### Sprint Planning & Retrospective:

At the end of the sprint, the team will review the completed work and gather feedback from team members and stakeholders as needed. The team will reflect on the sprint, identifying what went well and what could be improved. This is a really important step that helps improve team communication and dynamics. In this same meeting, the team will refine and adjust the plan for remaining sprints to address any issues and manage the project to on-time completion.

| Purpose          | Location       | Address       |
|------------------|----------------|---------------|
| Weekly Meeting   | CAS Building   | B20 Thursday  |
| Standups         | Messages       | CS391 Group    |

---

