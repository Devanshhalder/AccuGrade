# AccuGrade

### AI-Assisted Examination & On-Screen Marking Platform

AccuGrade is an AI-assisted digital evaluation platform designed to modernize **On-Screen Marking (OSM)** for university examinations.

It helps examiners evaluate handwritten answer sheets digitally while providing AI-assisted insights, rubric-based marking support, evaluation quality checks, and analytics.

> **AI assists the examiner. The examiner makes the final decision.**

---

## 🎯 Problem

Large-scale university examinations involve:

* Time-consuming manual evaluation
* Delays in result processing
* Unchecked answers and marking inconsistencies
* Difficulties in maintaining evaluation quality at scale
* Limited visibility into examiner workload and evaluation patterns
* Manual moderation and quality-control processes

AccuGrade addresses these challenges through a centralized digital evaluation workflow with AI-assisted support.

---

## 💡 Solution

AccuGrade provides a unified platform for:

**Digitize → Understand → Evaluate → Verify → Moderate → Analyze**

The system allows examiners to view digital answer sheets, evaluate individual questions, receive AI-assisted marking suggestions, and make the final marking decision.

---

## ✨ Key Features

### AI-Assisted Evaluation

* Analyzes student responses against questions and marking rubrics
* Provides suggested marks
* Highlights concepts identified in the answer
* Provides an explanation for the suggested evaluation

### On-Screen Marking

* Digital answer-sheet viewing
* Question-wise navigation
* Direct mark entry
* Accept / Edit / Override AI suggestions
* Evaluation progress tracking

### Evaluation Quality Checks

* Detection of potentially unchecked questions
* Identification of unusual scoring patterns
* Flagging of scripts requiring additional review

### Examiner Analytics

* Evaluation progress
* Workload monitoring
* Average evaluation time
* AI suggestion acceptance/modification indicators

### Moderation

* Centralized moderation queue
* Priority-based review
* Visibility into flagged scripts and evaluation issues

---

## 🧠 Human-in-the-Loop AI

AccuGrade does **not** replace examiners.

The AI provides recommendations that can be:

**Accept → Modify → Override**

The examiner retains complete control over the final awarded marks.

This human-in-the-loop approach is designed to combine AI-assisted efficiency with human academic judgment.

---

## 🏗️ System Architecture

```text
                    EXAMINER / ADMIN
                           │
                           ▼
                 ┌───────────────────┐
                 │     FRONTEND      │
                 │   HTML / CSS / JS │
                 └─────────┬─────────┘
                           │
                           ▼
                 ┌───────────────────┐
                 │   FASTAPI BACKEND │
                 │      Python       │
                 └───────┬─────┬─────┘
                         │     │
                ┌────────▼─┐ ┌─▼────────────┐
                │PostgreSQL│ │  AI / ML     │
                │ Database │ │ OCR + LLM    │
                └──────────┘ └──────────────┘
                         │
                         ▼
                  ANSWER SHEET
                   FILE STORAGE
```

---

## 🛠️ Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Chart.js / dashboard visualizations

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic

### Database

* PostgreSQL

### AI / ML

* Multimodal AI / LLM
* OCR / handwriting recognition
* Python-based anomaly detection

### Deployment

* Vercel
* Railway / Render
* Cloud storage

---

## 🔄 Evaluation Workflow

```text
Answer Sheet Upload
        ↓
Digitization / OCR
        ↓
Question & Answer Identification
        ↓
Rubric-Based AI Analysis
        ↓
Suggested Marks + Explanation
        ↓
Examiner Review
        ↓
Accept / Edit / Override
        ↓
Quality Checks
        ↓
Moderation
        ↓
Validated Results
```

---

## 📊 Prototype

The current prototype demonstrates the core examination workflow:

* Examiner login
* Examiner dashboard
* On-screen marking workspace
* Digital answer-sheet interface
* AI evaluation assistant
* Rubric coverage
* Suggested marks
* Examiner override controls
* Evaluation quality alerts
* Moderation queue
* Administrative analytics

The prototype uses demonstration data to showcase the intended workflow and system experience.

---

## 🔐 Design Principles

AccuGrade is designed around four principles:

**Human Control**
Final marks remain under examiner control.

**Explainability**
AI suggestions are accompanied by identifiable rubric coverage and reasoning.

**Quality Assurance**
Potential evaluation issues are surfaced for human review.

**Scalability**
The architecture separates the presentation, backend, database, AI, and storage layers.

---

## 🚀 Future Scope

Future development can extend AccuGrade with:

* Advanced handwriting recognition
* Multilingual answer evaluation
* More sophisticated rubric-based assessment
* Advanced anomaly detection
* Examiner calibration tools
* Institution-wide analytics
* Mobile examiner support
* Secure integration with university examination systems
* Automated result-generation workflows

---

## 👥 Team

**Team ZERO LATENCY**

Developed for the **MPOnline Limited – Idea & Innovation Hackathon 2026**

### Challenge 3

**AI-Driven Examination & On-Screen Marking Transformation**

---

## 📌 Project Status

**Prototype / Hackathon Demonstration**

AccuGrade is currently focused on demonstrating the core OSM workflow and AI-assisted examiner experience. Production deployment would require further validation, security hardening, institutional integration, and evaluation against real examination datasets.

