

# 🏢 Python Attendance Management System (Punch Time)

A simple office attendance system built using Python.
The program evaluates employee **In-Time** and **Out-Time** and automatically assigns attendance status based on predefined office rules.

---

## 📌 Features

* ✅ Present
* ⏰ Late
* 🕒 Half Day
* 🔹 Short Day
* ❌ Absent
* Time-based automatic status calculation
* Uses 24-hour time format

---

## 🛠️ Technologies Used

* Python 3
* `datetime` module
* Conditional statements

---

## 🧠 Office Timings (24-Hour Format)

* Office Start Time → **08:00**
* Late After → **08:15**
* Half Day After → **11:00**
* Office End Time → **17:00**
* Short Day → Leaving before **17:00**

> Note: These timings can be modified in the code as per requirement.

---

## 📂 Project Structure

```
python-attendance-system/
│
├── attendance.py
└── README.md
```

---

## ▶️ How to Run

1. Install Python (if not installed).
2. Clone the repository:

```bash
git clone https://github.com/your-username/python-attendance-system.git
```

3. Navigate to the project folder:

```bash
cd python-attendance-system
```

4. Run the program:

```bash
python attendance.py
```

---

## 💻 Example Usage

```
Enter In Time (HH:MM) or type 'absent': 08:05
Enter Out Time (HH:MM): 17:00
Status: Present
```

```
Enter In Time (HH:MM) or type 'absent': 09:20
Enter Out Time (HH:MM): 16:30
Status: Late + Short Day
```

```
Enter In Time (HH:MM) or type 'absent': absent
Status: Absent
```

---

## 📚 Learning Outcomes

* Working with Python `datetime`
* Implementing real-world attendance logic
* Time comparison using conditions
* Building a mini HR automation system

---

## 🚀 Future Improvements

* Support for multiple employees
* Store attendance data in CSV/Excel
* Generate monthly reports
* Add GUI or Web interface

---

## 👩‍💻 Author

Lucky Sachdeva
Aspiring Data Scientist 🚀
