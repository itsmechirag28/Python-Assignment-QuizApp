# Basic database for users
users_db = {}
result = {"DSA":0,"DBMS":0,"Python":0}

# Quiz questions organized by topics
quizzes = {
    "DSA": [
        {
            "question": "What is the time complexity of searching for an element in a balanced binary search tree (BST)?",
            "options": ["A) O(n)", "B) O(logn)", "C) O(1)", "D) O(nlogn)"],
            "answer": "D"
        },
        {
            "question": "Which data structure is used to implement recursion?",
            "options": ["A) Queue", "B) Array", "C) Stack", "D) Linked List"],
            "answer": "C"
        },
        {
            "question": "Which algorithm is used for finding the shortest path in a weighted graph with non-negative weights?",
            "options": ["A) Breadth-First Search (BFS) ", "B) Depth-First Search (DFS) ", "C) Kruskal's Algorithm", "D) Dijkstra's Algorithm"],
            "answer": "D"
        }
    ],
    "DBMS": [
        {
            "question": "What is the purpose of a primary key in a relational database?",
            "options": ["A) To ensure that all records in a table are unique", "B) To link two tables together", "C) To allow NULL values in the table", "D) To index the data in the table"],
            "answer": "A"
        },
        {
            "question": "Which SQL statement is used to extract data from a database?",
            "options": ["A) GET", "B) SELECT", "C) EXTRACT", "D) OPEN"],
            "answer": "B"
        },
        {
            "question": "Which of the following is NOT a DDL command?",
            "options": ["A) CREATE", "B) DROP", "C) SELECT", "D) ALTER"],
            "answer": "C"
        }
    ],
    "Python": [
        {
            "question": "Which of the following is a mutable data type in Python?",
            "options": ["A) String", "B) Tuple", "C) List", "D) Integer"],
            "answer": "C"
        },
        {
            "question": "What is the role of indentation in Python?",
            "options": ["A) To declare variables", "B) To mark the end of a statement", "C) To define the scope of loops, conditionals, and functions", "D) To create comments "],
            "answer": "C"
        },
        {
            "question": "Which of the following is the correct way to declare a variable in Python?",
            "options": ["A) int x = 10", "B) x = 10", "C) variable x = 10", "D) declare x = 10"],
            "answer": "B"
        }
    ]
}

# Function to register a new user
def register():
    print("\n--- Register ---")
    username = input("Enter a username: ")
    if username in users_db:
        print("Username already exists. Please choose a different one.")
    else:
        password = input("Enter a password: ")
        users_db[username] = password
        print("Registration successful!")

# Function to log in an existing user
def login():
    print("\n--- Login ---")
    username = input("Enter your username: ")
    if username in users_db:
        password = input("Enter your password: ")
        if users_db[username] == password:
            print("Login successful!")
            return username
        else:
            print("Incorrect password.")
            return None
    else:
        print("Username not found.")
        return None

# Function to take a quiz
def attempt_quiz(username):
    
    print("\n--- Choose a topic ---")
    topics = list(quizzes.keys())
    for i, topic in enumerate(topics,start=1):
        print(f"{i}) {topic}")
    
    choice = int(input("Enter the number of the topic you want to take: "))
    selected_topic = topics[choice - 1]

    print(f"\nStarting the quiz on {selected_topic}!")
    score = 0
    for i, question in enumerate(quizzes[selected_topic], start=1):
        print(f"\nQuestion {i}: {question['question']}")
        for option in question['options']:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        if user_answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}")
    
    print(f"\n{username}, your final score for the {selected_topic} quiz is {score} out of {len(quizzes[selected_topic])}")
    result[selected_topic] += score

    

# Main program loop
def main():
    while True:
        print("\n--- Quiz Application ---")
        print("1) Register")
        print("2) Login")
        print("3) Attempt Quiz")
        print("4) Show result")
        print("5) Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            user = login()
        elif choice =='3':
            if user:
                attempt_quiz(user)
        elif choice == '4':
            for key,value in result.items():
                print(f"{key}:{value}")
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
