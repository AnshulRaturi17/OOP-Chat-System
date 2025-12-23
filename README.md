💬 OOP Chat System 🚀
A Python-based chat simulation built to demonstrate mastery of Object-Oriented Programming (OOP) principles. This project moves beyond simple scripting to create a scalable, modular architecture for digital communication.

🧠 Key OOP Concepts Implemented
1. Encapsulation 🛡️
Data and behaviors are bundled within classes. For example, the user class manages its own name and actions (joining rooms), while the chatRoom encapsulates the logic for member management and history tracking.

2. Composition 🧩
The chatRoom doesn't inherit from users; it has users. By using a set() for members and a list() for history, the system manages relationships between different objects efficiently.

3. Inheritance 🧬
The privateMessage class inherits from the base message class. It reuses the logic for sender and content while adding its own unique attribute: receiver.

Example: class privateMessage(message):

4. Polymorphism 🎭
One of the most powerful features! The show_history() method calls .display() on every message in its list. Python automatically decides whether to use the standard display or the private display based on the object's type at runtime.

🛠️ Features
Public Broadcasting: Only authorized members of a room can send messages.

Private Messaging: Direct communication between users that remains outside public logs.

Member Management: Prevent duplicate entries using Python Sets.

History Tracking: A persistent log of all public interactions within a room.

🚀 How to Run
Clone the repo.

Run python chat_system.py.

Watch the objects interact in the console!
