# Python 60 Day Challenge

Welcome to my Python 60 Day Challenge repository! This is a daily log of solved Python programming challenges.

## 📅 Progress Tracker

| Day | Challenge | Status |
|-----|-----------|--------|
| 1   | [User Profile Validation System](./Day_1/) | ✅ Complete |
| 2   | [Smart ID & Credential Validator](./Day_2/) | ✅ Complete |
| 3   | [Student Performance Analyzer](./Day_3/) | ✅ Complete |
| 4   | [Cyber Activity Risk Analyzer](./Day_4/) | ✅ Complete |
| 5   | [Emergency Resource Dispatch Analyzer](./Day_5/) | ✅ Complete |
| 6   | [Smart Transaction Risk Detector](./Day_6/) | ✅ Complete |
| 7   | Day 7 Challenge | ✅ Complete |
| 8   | [Multi-Dimensional Academic Intelligence System](./Day-8.py) | ✅ Complete |

## 📚 Structure

Each day's solution includes:
- **Problem Statement**: Description of the challenge
- **Solution**: Python code implementation
- **Concepts**: Key programming concepts used

## 🎯 Goals

- Solve one Python challenge daily
- Improve problem-solving skills
- Master Python fundamentals and advanced concepts

## 📝 How to Use

1. Check the daily challenge folder
2. Review the problem statement
3. Study the solution code
4. Run and test locally

## 🔧 Technologies

- Python 3.x
- Standard libraries

---

**Start Date**: 28 Jan 2026  
**Target Completion**: Day 60

## 📝 Daily Challenges

| Day | Challenge | Status |
|-----|-----------|--------|
| 1   | [User Profile Validation System](./Day_1/) | ✅ Complete |
| 2   | [Smart ID & Credential Validator](./Day_2/) | ✅ Complete |
| 3   | [Student Performance Analyzer](./Day_3/) | ✅ Complete |
| 4   | [Cyber Activity Risk Analyzer](./Day_4/) | ✅ Complete |
| 5   | [Emergency Resource Dispatch Analyzer](./Day_5/) | ✅ Complete |

| 6   | [Smart Transaction Risk Detector](./Day_6/) | ✅ Complete |
| 7   | Day 7 Challenge | ✅ Complete |
| 8   | [Multi-Dimensional Academic Intelligence System](./Day-8.py) | ✅ Complete |

---

## 📖 Concepts Used (Day-wise)

### Day 1 – User Profile Validation System
- Input handling and string processing
- Conditional statements for validation checks
- Basic data validation logic
- Structured output formatting

### Day 2 – Smart ID & Credential Validator
- Lists for storing credentials
- for loops for validation
- Conditional checks for ID rules
- Logical filtering and error handling

### Day 3 – Student Performance Analyzer
- Lists for storing marks
- for loops for processing data
- Conditional statements for grade classification
- Basic performance analysis logic
- Personalized bonuses based on name length (4-letter bonus)
- Lucky 7 bonus if roll number contains digit 7
- Special topper logic for specific name and roll–mark match condition

### Day 4 – Cyber Activity Risk Analyzer
- Lists for activity logs
- Loop-based validation
- Conditional risk categorization (Low/Medium/High)
- Logical filtering techniques
- Personalization based on last digit of Register Number (D)
- If D is even → Removed Low Risk entries
- If D is odd → Removed Critical Risk entries
- Counted entries removed due to personalization rule

### Day 5 – Emergency Resource Dispatch Analyzer
- Lists for categorizing requests
- for loops for classification
- Conditional statements for demand levels
- Counting valid and removed requests
- Personalized filtering using PLI (L % 3 rule)
- Calculated L (length of full name excluding spaces)
- Computed PLI = L % 3 and applied Rule A/B/C accordingly

### Day 6 – Smart Transaction Risk Detector
- Manual input parsing without using split()
- Lists for storing transactions
- Dictionary-based categorization (normal, large, high_risk, invalid)
- Conditional statements for classification
- List comprehension for filtering valid transactions
- Aggregation using sum() and len()
- Multi-condition risk evaluation (frequency, total spending, high-risk count)
- Final risk classification based on combined conditions

### Day 8 – Multi-Dimensional Academic Intelligence System
- Data generation using random module with seed
- Lists, Tuples, Sets, and Dictionary for structured data storage
- Pandas DataFrame for tabular data management
- NumPy for mean, std deviation, max, and correlation computation
- Manual median calculation (without .describe())
- math.log() for performance_index feature engineering
- performance_index = (marks×0.6 + assignment×0.4) × log(attendance+1)
- Normalization using min-max scaling
- Student classification into At Risk / Average / Good / Top Performer
- List comprehension for filtering above-average performance index
- Pattern detection: consistency, attendance risk, high achievement
- Personalization: last digit of register number (8) → 18 students generated
