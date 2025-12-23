class user:
    def __init__(self, userName):
        """Initializes a new user with a unique username."""
        self.userName = userName
    
    def join_room(self, room_obj):
        """Allows a user to enter a specific ChatRoom."""
        room_obj.addUser(self)

    def send_private_message(self, receiver, content):
        """Creates and displays a private message directly to another user."""
        pm1 = privateMessage(self, receiver, content)
        pm1.display()

class message:
    def __init__(self, sender, content):
        """Base class for all messages containing sender and text."""
        self.content = content
        self.sender = sender # Stores the User object

    def display(self):
        """Standard display format for public messages."""
        print(f"{self.sender.userName} sent: {self.content}")

class privateMessage(message):
    """Inherits from message, adding a specific receiver for DMs."""
    def __init__(self, sender, receiver, content):
        # super() calls the parent (message) constructor
        super().__init__(sender, content)
        self.receiver = receiver

    def display(self):
        """Polymorphic method: Overrides the parent display for private context."""
        print(f"🔒 [Private] {self.sender.userName} to {self.receiver.userName}: {self.content}")

class chatRoom:
    def __init__(self, room_name):
        """Manages users and stores the history of public conversations."""
        self.room_name = room_name
        self.membersList = set() # Ensures unique members
        self.history = list()    # Stores Message objects
    
    def addUser(self, user_obj):
        """Adds a User object to the room."""
        if user_obj not in self.membersList:
            self.membersList.add(user_obj)

    def removeUser(self, user_obj):
        """Removes a User object from the room."""
        if user_obj in self.membersList:
            self.membersList.remove(user_obj)
    
    def record_message(self, msg_obj):
        """Logs a message object into the room's history."""
        self.history.append(msg_obj)
    
    def show_history(self):
        """Iterates through history and triggers polymorphic display() calls."""
        print(f"\n--- History for {self.room_name} ---")
        for msg in self.history:
            msg.display()

    def send_broadcast(self, sender_object, text):
        """Creates a message and saves it if the sender is an authorized member."""
        if sender_object in self.membersList:
            m1 = message(sender_object, text)
            self.record_message(m1)
        else:
            print(f"⚠️ Access Denied: {sender_object.userName} is not in {self.room_name}")

# --- Demonstration Script ---
if __name__ == "__main__":
    alice = user("Alice")
    bob = user("Bob")
    general = chatRoom("General")

    alice.join_room(general)
    general.send_broadcast(alice, "Hello everyone! Happy coding!")
    
    # Private Message (Outside room history)
    alice.send_private_message(bob, "Hey Bob, check out this OOP project!")

    # Show History
    general.show_history()