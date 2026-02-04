##Live Link

https://sgpa-calculator-fyit-sxc.onrender.com/

# SGPA Calculator Web App
---

## 📌 Problem Statement
We received a soft copy of the Semester 1 marksheet from college, but the **SGPA was not provided** because one of the exams was not conducted.

To estimate my academic performance accurately, I decided to **build my own SGPA calculator**, initially as a **Python program**, and later converted it into a **full-stack web application**.

---

## 🧠 Core Logic (Python Backend)

The backend is written in **Python using Flask** and follows these steps:

1. **Accepts subject-wise marks** sent from the frontend in JSON format
2. **Converts marks to percentages** based on maximum marks for each subject
3. **Maps percentages to grade points** using predefined grading rules
4. **Calculates SGPA** using the standard credit-weighted formula:
   SGPA = Σ (Grade Point × Subject Credit) / Total Credits
5. Returns the final SGPA to the frontend, where it is displayed instantly
6. Considered that percentage scored in the missing subject to be 60%(8 Grade Points) for statistical justice

All calculation logic is handled on the server to ensure **accuracy and consistency**.

## 🛠 Tech Stack

### Frontend
- HTML  
- CSS  
- JavaScript  

### Backend
- Python  
- Flask  

### Deployment
- Render  
