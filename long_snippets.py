LONG_QUESTIONS = [
    # ======================================
    # =============== PYTHON ===============
    # ======================================
    {
        "code": """import random
class Adventurer:
    def __init__(self, name):
        self.name = name
        self.inventory = []

    def collect_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} collected {item}!")

def random_event():
    events = ["find a hidden treasure", "fall into a trap", "meet a friendly merchant", "fight a wild beast"]
    return random.choice(events)

def main():
    player = Adventurer("Aria")
    for i in range(3):
        event = random_event()
        print(f"Event #{i+1}: You {event}.")
        if "treasure" in event:
            player.collect_item("Gold Coin")
    print(f"Final Inventory: {player.inventory}")

if __name__ == "__main__":
    main()
""",
        "language": "Python"
    },
    {
        "code": """class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

def load_books(filename):
    books = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 2:
                books.append(Book(parts[0], parts[1]))
    return books

def main():
    # Suppose we have a file called 'library.txt'
    books = load_books("library.txt")
    for b in books:
        print(b)
    uppercase_titles = [b.title.upper() for b in books]
    print("Titles in uppercase:", uppercase_titles)

if __name__ == "__main__":
    main()
""",
        "language": "Python"
    },

    # ======================================
    # ============ JAVASCRIPT =============
    # ======================================
    {
        "code": """class Chat {
  constructor(user) {
    this.user = user;
    this.messages = [];
  }

  sendMessage(msg) {
    const messageObj = {
      user: this.user,
      text: msg,
      time: new Date().toLocaleTimeString()
    };
    this.messages.push(messageObj);
  }

  displayMessages() {
    console.clear();
    console.log("----- Chat Messages -----");
    this.messages.forEach(m => {
      console.log(`[${m.time}] ${m.user}: ${m.text}`);
    });
  }
}

const myChat = new Chat("Alice");

// Mimic receiving messages over time
setInterval(() => {
  myChat.sendMessage("Hello from " + myChat.user);
  myChat.displayMessages();
}, 3000);
""",
        "language": "JavaScript"
    },
    {
        "code": """class TodoList {
  constructor() {
    this.todos = [];
  }

  async loadTodos(url) {
    try {
      const response = await fetch(url);
      this.todos = await response.json();
    } catch (error) {
      console.error("Failed to load todos:", error);
    }
  }

  addTodo(task) {
    this.todos.push({ title: task, completed: false });
  }

  completeTask(index) {
    if (this.todos[index]) {
      this.todos[index].completed = true;
    }
  }

  printTodos() {
    console.log("----- TODOS -----");
    this.todos.forEach((t, i) => {
      console.log(
        \`\${i + 1}: \${t.title} [\${t.completed ? "DONE" : "PENDING"}]\`
      );
    });
  }
}

(async function main() {
  const list = new TodoList();
  await list.loadTodos("https://jsonplaceholder.typicode.com/todos?_limit=5");
  list.printTodos();
  list.addTodo("Learn more about async/await");
  list.completeTask(0);
  list.printTodos();
})();
""",
        "language": "JavaScript"
    },

    # ======================================
    # ================ C++ ================
    # ======================================
    {
        "code": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Item {
    string name;
    int quantity;
};

int main() {
    vector<Item> inventory;
    inventory.push_back({"Potion", 5});
    inventory.push_back({"Elixir", 2});
    inventory.push_back({"Ether", 1});

    cout << "Current Inventory:" << endl;
    for (const auto &item : inventory) {
        cout << item.name << " x " << item.quantity << endl;
    }

    cout << "\\nAdding an item...\\n";
    inventory.push_back({"Phoenix Down", 1});

    cout << "Final Inventory:" << endl;
    for (const auto &item : inventory) {
        cout << item.name << " x " << item.quantity << endl;
    }

    return 0;
}
""",
        "language": "C++"
    },
    {
        "code": """#include <iostream>
#include <vector>
#include <memory>
using namespace std;

class Animal {
public:
    virtual void makeSound() {
        cout << "Generic animal sound..." << endl;
    }
    virtual ~Animal() {}
};

class Dog : public Animal {
public:
    void makeSound() override {
        cout << "Woof!" << endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        cout << "Meow!" << endl;
    }
};

int main() {
    vector<unique_ptr<Animal>> animals;
    animals.push_back(make_unique<Dog>());
    animals.push_back(make_unique<Cat>());

    for (auto &a : animals) {
        a->makeSound();
    }
    return 0;
}
""",
        "language": "C++"
    },

    # ======================================
    # =============== RUBY ================
    # ======================================
    {
        "code": """module Greetings
  def greet(name)
    puts "Hello, \#{@name}! - from Greetings module"
  end
end

class Wizard
  include Greetings

  attr_reader :mana

  def initialize(name, mana)
    @name = name
    @mana = mana
  end

  def cast_spell(spell)
    if @mana > 0
      puts "\#{@name} casts \#{spell}!"
      @mana -= 1
    else
      puts "\#{@name} is out of mana!"
    end
  end
end

if __FILE__ == $0
  merlin = Wizard.new("Merlin", 3)
  merlin.greet("Arthur")
  4.times { merlin.cast_spell("Fireball") }
end
""",
        "language": "Ruby"
    },
    {
        "code": """require 'csv'

class Customer
  attr_reader :first_name, :last_name, :email

  def initialize(first, last, email)
    @first_name = first
    @last_name = last
    @email = email
  end

  def full_name
    "\#{@first_name} \#{@last_name}"
  end
end

def load_customers(csv_file)
  customers = []
  CSV.foreach(csv_file, headers: true) do |row|
    customers << Customer.new(row["First"], row["Last"], row["Email"])
  end
  customers
end

if __FILE__ == $0
  list = load_customers("customers.csv")
  list.each do |c|
    puts "\#{c.full_name} <\#{c.email}>"
  end
end
""",
        "language": "Ruby"
    },

    # ======================================
    # =============== JAVA ================
    # ======================================
    {
        "code": """import java.util.ArrayList;
import java.util.List;

class Employee {
    private String name;
    private int id;
    
    public Employee(String n, int i) {
        this.name = n;
        this.id = i;
    }
    
    public String getName() {
        return name;
    }
    
    public int getId() {
        return id;
    }
}

public class Company {
    public static void main(String[] args) {
        List<Employee> staff = new ArrayList<>();
        staff.add(new Employee("Alice", 101));
        staff.add(new Employee("Bob", 102));
        staff.add(new Employee("Charlie", 103));
        
        System.out.println("Employee List:");
        for (Employee e : staff) {
            System.out.println(e.getName() + " (ID: " + e.getId() + ")");
        }
    }
}
""",
        "language": "Java"
    },
    {
        "code": """import java.util.Scanner;

public class MenuDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("----- MENU -----");
            System.out.println("1) Greet");
            System.out.println("2) Add Numbers");
            System.out.println("3) Quit");
            System.out.print("Choose an option: ");

            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter your name: ");
                    String name = sc.next();
                    System.out.println("Hello, " + name + "!");
                    break;
                case 2:
                    System.out.print("Enter first number: ");
                    int a = sc.nextInt();
                    System.out.print("Enter second number: ");
                    int b = sc.nextInt();
                    System.out.println("Sum = " + (a + b));
                    break;
                case 3:
                    System.out.println("Goodbye!");
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
            System.out.println();
        }
        sc.close();
    }
}
""",
        "language": "Java"
    },

    # ======================================
    # =============== LUA ==================
    # ======================================
    {
        "code": """local function taskA()
    for i = 1, 3 do
        print("Task A - step " .. i)
        coroutine.yield()
    end
end

local function taskB()
    for i = 1, 5 do
        print("Task B - step " .. i)
        coroutine.yield()
    end
end

local coA = coroutine.create(taskA)
local coB = coroutine.create(taskB)

while coroutine.status(coA) ~= "dead" or coroutine.status(coB) ~= "dead" do
    if coroutine.status(coA) ~= "dead" then
        coroutine.resume(coA)
    end
    if coroutine.status(coB) ~= "dead" then
        coroutine.resume(coB)
    end
end

print("All tasks finished!")
""",
        "language": "Lua"
    },
    {
        "code": """local inventory = {}

local function addItem(item, qty)
    if inventory[item] then
        inventory[item] = inventory[item] + qty
    else
        inventory[item] = qty
    end
end

local function removeItem(item, qty)
    if inventory[item] then
        inventory[item] = inventory[item] - qty
        if inventory[item] <= 0 then
            inventory[item] = nil
        end
    end
end

local function printInventory()
    print("----- Inventory -----")
    for item, count in pairs(inventory) do
        print(item .. ": " .. count)
    end
end

-- Test usage
addItem("Potion", 3)
addItem("Elixir", 1)
addItem("Potion", 2)
removeItem("Potion", 4)
printInventory()
""",
        "language": "Lua"
    },

    # ======================================
    # ============== HOLYC ===============
    # ======================================
    {
        "code": """#include "Bios.inc"

U0 MyRandom(U8 seed)
{
   RSeed(seed);
   Print("Random number is: %d\\n", RNum());
   Print("Another random number: %d\\n", RNum());
}

U0 main()
{
   Print("Welcome to !\\n");
   MyRandom(42);
   Print("Done.\\n");
}
""",
        "language": "HolyC"
    },
    {
        "code": """#include "Bios.inc"

U0 Hello()
{
   Print("Hello from TempleOS ()!\\n");
}

U0 main()
{
   Hello();
   I32 i;
   for (i = 0; i < 5; i++)
   {
      Print("i = %d\\n", i);
   }
   Print("End of snippet.\\n");
}
""",
        "language": "HolyC"
    },

    # ======================================
    # ================ C# =================
    # ======================================
    {
        "code": """using System;
using System.Collections.Generic;
using System.Linq;

public abstract class Vehicle {
    public string Model { get; set; }
    public int Year { get; set; }
    public Vehicle(string model, int year) {
        Model = model;
        Year = year;
    }
    public abstract void Drive();
}

public class Car : Vehicle {
    public Car(string model, int year) : base(model, year) {}
    public override void Drive() {
        Console.WriteLine($"Driving car {Model} ({Year}).");
    }
}

class Program {
    static void Main(string[] args) {
        List<Vehicle> garage = new List<Vehicle>() {
            new Car("Sedan", 2018),
            new Car("Coupe", 2020),
            new Car("Hatchback", 2015),
        };
        var recentCars = garage.Where(v => v.Year >= 2018);
        foreach (var car in recentCars) {
            car.Drive();
        }
    }
}
""",
        "language": "C#"
    },
    {
        "code": """using System;
using System.Threading.Tasks;

class Demo {
    static async Task Main(string[] args) {
        Console.WriteLine("Starting async demo...");

        string data = await LoadDataAsync();
        Console.WriteLine($"Received data: {data}");

        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
    }

    static async Task<string> LoadDataAsync() {
        await Task.Delay(1000); // simulate I/O delay
        return "Sample Data from C# Async Method";
    }
}
""",
        "language": "C#"
    },

    # ======================================
    # =============== REACT ===============
    # ======================================
    {
        "code": """import React, { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([]);

  useEffect(() => {
    console.log('Component mounted, fetching data...');
    // Faking an API call
    setTimeout(() => {
      setItems(['Apple', 'Banana', 'Cherry']);
    }, 1000);
  }, []);

  return (
    <div>
      <h1>React Counter</h1>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>

      <h2>Items</h2>
      <ul>
        {items.map((x, i) => <li key={i}>{x}</li>)}
      </ul>
    </div>
  );
}

export default App;
""",
        "language": "React"
    },
    {
        "code": """import React, { useState } from 'react';

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [task, setTask] = useState('');

  const addTodo = () => {
    if (task.trim()) {
      setTodos([...todos, { text: task, done: false }]);
      setTask('');
    }
  };

  const toggleTodo = (index) => {
    const newTodos = [...todos];
    newTodos[index].done = !newTodos[index].done;
    setTodos(newTodos);
  };

  return (
    <div>
      <h1>React Todo List</h1>
      <input value={task} onChange={(e) => setTask(e.target.value)} />
      <button onClick={addTodo}>Add Todo</button>
      <ul>
        {todos.map((t, i) => (
          <li 
            key={i}
            style={{ textDecoration: t.done ? 'line-through' : 'none' }}
            onClick={() => toggleTodo(i)}
          >
            {t.text}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
""",
        "language": "React"
    },

    # ======================================
    # ============== NEXTJS ===============
    # ======================================
{
    "code": """import React from 'react';

export default function Home({ message, timestamp }) {
  return (
    <div style={{ margin: '1rem' }}>
      <h1>Home Page</h1>
      <p>{message}</p>
      <hr />
      <section>
        <h2>Extra Content</h2>
        <ul>
          <li>This is a Next.js example page.</li>
          <li>We can fetch data on the server side.</li>
          <li>Timestamp: {timestamp}</li>
          <li>Feel free to scroll around!</li>
        </ul>
      </section>
    </div>
  );
}

export async function getServerSideProps() {
  // Simulate a data fetch
  const message = 'Hello from the server side!';
  const timestamp = new Date().toLocaleString();

  // Return these props to the React component
  return {
    props: {
      message,
      timestamp
    }
  };
}
""",
    "language": "NextJS"
},
{
    "code": """export default async function handler(req, res) {
  if (req.method === 'GET') {
    // If there's a "name" query param, include it in the greeting
    const { name = 'stranger' } = req.query;
    res.status(200).json({
      greeting: `Hello, ${name} from the Next.js API!`,
      note: 'Feel free to scroll through this snippet.'
    });
  } else if (req.method === 'POST') {
    // In a real app, you might parse JSON or perform DB operations
    const body = req.body || {};
    res.status(201).json({
      success: true,
      dataReceived: body,
      message: 'POST data created successfully!'
    });
  } else {
    // Return 405 for other HTTP methods
    res.setHeader('Allow', ['GET', 'POST']);
    res.status(405).json({ error: 'Method Not Allowed' });
  }
}
""",
    "language": "NextJS"
},    {
        "code": """class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

def load_books(filename):
    books = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split("|")
            if len(parts) == 2:
                books.append(Book(parts[0], parts[1]))
    return books

def main():
    # Suppose we have a file called 'library.txt'
    books = load_books("library.txt")
    for b in books:
        print(b)
    uppercase_titles = [b.title.upper() for b in books]
    print("Titles in uppercase:", uppercase_titles)

if __name__ == "__main__":
    main()
""",
        "language": "Python"
    },

    # ======================================
    # ============ JAVASCRIPT =============
    # ======================================
    {
        "code": """class Chat {
  constructor(user) {
    this.user = user;
    this.messages = [];
  }

  sendMessage(msg) {
    const messageObj = {
      user: this.user,
      text: msg,
      time: new Date().toLocaleTimeString()
    };
    this.messages.push(messageObj);
  }

  displayMessages() {
    console.clear();
    console.log("----- Chat Messages -----");
    this.messages.forEach(m => {
      console.log(`[${m.time}] ${m.user}: ${m.text}`);
    });
  }
}

const myChat = new Chat("Alice");

// Mimic receiving messages over time
setInterval(() => {
  myChat.sendMessage("Hello from " + myChat.user);
  myChat.displayMessages();
}, 3000);
""",
        "language": "JavaScript"
    },
    {
        "code": """class TodoList {
  constructor() {
    this.todos = [];
  }

  async loadTodos(url) {
    try {
      const response = await fetch(url);
      this.todos = await response.json();
    } catch (error) {
      console.error("Failed to load todos:", error);
    }
  }

  addTodo(task) {
    this.todos.push({ title: task, completed: false });
  }

  completeTask(index) {
    if (this.todos[index]) {
      this.todos[index].completed = true;
    }
  }

  printTodos() {
    console.log("----- TODOS -----");
    this.todos.forEach((t, i) => {
      console.log(
        \`\${i + 1}: \${t.title} [\${t.completed ? "DONE" : "PENDING"}]\`
      );
    });
  }
}

(async function main() {
  const list = new TodoList();
  await list.loadTodos("https://jsonplaceholder.typicode.com/todos?_limit=5");
  list.printTodos();
  list.addTodo("Learn more about async/await");
  list.completeTask(0);
  list.printTodos();
})();
""",
        "language": "JavaScript"
    },

    # ======================================
    # ================ C++ ================
    # ======================================
    {
        "code": """#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Item {
    string name;
    int quantity;
};

int main() {
    vector<Item> inventory;
    inventory.push_back({"Potion", 5});
    inventory.push_back({"Elixir", 2});
    inventory.push_back({"Ether", 1});

    cout << "Current Inventory:" << endl;
    for (const auto &item : inventory) {
        cout << item.name << " x " << item.quantity << endl;
    }

    cout << "\\nAdding an item...\\n";
    inventory.push_back({"Phoenix Down", 1});

    cout << "Final Inventory:" << endl;
    for (const auto &item : inventory) {
        cout << item.name << " x " << item.quantity << endl;
    }

    return 0;
}
""",
        "language": "C++"
    },
    {
        "code": """#include <iostream>
#include <vector>
#include <memory>
using namespace std;

class Animal {
public:
    virtual void makeSound() {
        cout << "Generic animal sound..." << endl;
    }
    virtual ~Animal() {}
};

class Dog : public Animal {
public:
    void makeSound() override {
        cout << "Woof!" << endl;
    }
};

class Cat : public Animal {
public:
    void makeSound() override {
        cout << "Meow!" << endl;
    }
};

int main() {
    vector<unique_ptr<Animal>> animals;
    animals.push_back(make_unique<Dog>());
    animals.push_back(make_unique<Cat>());

    for (auto &a : animals) {
        a->makeSound();
    }
    return 0;
}
""",
        "language": "C++"
    },

    # ======================================
    # =============== RUBY ================
    # ======================================
    {
        "code": """module Greetings
  def greet(name)
    puts "Hello, \#{@name}! - from Greetings module"
  end
end

class Wizard
  include Greetings

  attr_reader :mana

  def initialize(name, mana)
    @name = name
    @mana = mana
  end

  def cast_spell(spell)
    if @mana > 0
      puts "\#{@name} casts \#{spell}!"
      @mana -= 1
    else
      puts "\#{@name} is out of mana!"
    end
  end
end

if __FILE__ == $0
  merlin = Wizard.new("Merlin", 3)
  merlin.greet("Arthur")
  4.times { merlin.cast_spell("Fireball") }
end
""",
        "language": "Ruby"
    },
    {
        "code": """require 'csv'

class Customer
  attr_reader :first_name, :last_name, :email

  def initialize(first, last, email)
    @first_name = first
    @last_name = last
    @email = email
  end

  def full_name
    "\#{@first_name} \#{@last_name}"
  end
end

def load_customers(csv_file)
  customers = []
  CSV.foreach(csv_file, headers: true) do |row|
    customers << Customer.new(row["First"], row["Last"], row["Email"])
  end
  customers
end

if __FILE__ == $0
  list = load_customers("customers.csv")
  list.each do |c|
    puts "\#{c.full_name} <\#{c.email}>"
  end
end
""",
        "language": "Ruby"
    },

    # ======================================
    # =============== JAVA ================
    # ======================================
    {
        "code": """import java.util.ArrayList;
import java.util.List;

class Employee {
    private String name;
    private int id;

    public Employee(String n, int i) {
        this.name = n;
        this.id = i;
    }

    public String getName() {
        return name;
    }

    public int getId() {
        return id;
    }
}

public class Company {
    public static void main(String[] args) {
        List<Employee> staff = new ArrayList<>();
        staff.add(new Employee("Alice", 101));
        staff.add(new Employee("Bob", 102));
        staff.add(new Employee("Charlie", 103));

        System.out.println("Employee List:");
        for (Employee e : staff) {
            System.out.println(e.getName() + " (ID: " + e.getId() + ")");
        }
    }
}
""",
        "language": "Java"
    },
    {
        "code": """import java.util.Scanner;

public class MenuDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean running = true;

        while (running) {
            System.out.println("----- MENU -----");
            System.out.println("1) Greet");
            System.out.println("2) Add Numbers");
            System.out.println("3) Quit");
            System.out.print("Choose an option: ");

            int choice = sc.nextInt();
            switch (choice) {
                case 1:
                    System.out.print("Enter your name: ");
                    String name = sc.next();
                    System.out.println("Hello, " + name + "!");
                    break;
                case 2:
                    System.out.print("Enter first number: ");
                    int a = sc.nextInt();
                    System.out.print("Enter second number: ");
                    int b = sc.nextInt();
                    System.out.println("Sum = " + (a + b));
                    break;
                case 3:
                    System.out.println("Goodbye!");
                    running = false;
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
            System.out.println();
        }
        sc.close();
    }
}
""",
        "language": "Java"
    },

    # ======================================
    # =============== LUA ==================
    # ======================================
    {
        "code": """local function taskA()
    for i = 1, 3 do
        print("Task A - step " .. i)
        coroutine.yield()
    end
end

local function taskB()
    for i = 1, 5 do
        print("Task B - step " .. i)
        coroutine.yield()
    end
end

local coA = coroutine.create(taskA)
local coB = coroutine.create(taskB)

while coroutine.status(coA) ~= "dead" or coroutine.status(coB) ~= "dead" do
    if coroutine.status(coA) ~= "dead" then
        coroutine.resume(coA)
    end
    if coroutine.status(coB) ~= "dead" then
        coroutine.resume(coB)
    end
end

print("All tasks finished!")
""",
        "language": "Lua"
    },
    {
        "code": """local inventory = {}

local function addItem(item, qty)
    if inventory[item] then
        inventory[item] = inventory[item] + qty
    else
        inventory[item] = qty
    end
end

local function removeItem(item, qty)
    if inventory[item] then
        inventory[item] = inventory[item] - qty
        if inventory[item] <= 0 then
            inventory[item] = nil
        end
    end
end

local function printInventory()
    print("----- Inventory -----")
    for item, count in pairs(inventory) do
        print(item .. ": " .. count)
    end
end

-- Test usage
addItem("Potion", 3)
addItem("Elixir", 1)
addItem("Potion", 2)
removeItem("Potion", 4)
printInventory()
""",
        "language": "Lua"
    },

    # ======================================
    # ============== HOLYC ===============
    # ======================================
    {
        "code": """#include "Bios.inc"

U0 MyRandom(U8 seed)
{
   RSeed(seed);
   Print("Random number is: %d\\n", RNum());
   Print("Another random number: %d\\n", RNum());
}

U0 main()
{
   Print("Welcome to !\\n");
   MyRandom(42);
   Print("Done.\\n");
}
""",
        "language": "HolyC"
    },
    {
        "code": """#include "Bios.inc"

U0 Hello()
{
   Print("Hello from TempleOS ()!\\n");
}

U0 main()
{
   Hello();
   I32 i;
   for (i = 0; i < 5; i++)
   {
      Print("i = %d\\n", i);
   }
   Print("End of snippet.\\n");
}
""",
        "language": "HolyC"
    },

    # ======================================
    # ================ C# =================
    # ======================================
    {
        "code": """using System;
using System.Collections.Generic;
using System.Linq;

public abstract class Vehicle {
    public string Model { get; set; }
    public int Year { get; set; }
    public Vehicle(string model, int year) {
        Model = model;
        Year = year;
    }
    public abstract void Drive();
}

public class Car : Vehicle {
    public Car(string model, int year) : base(model, year) {}
    public override void Drive() {
        Console.WriteLine($"Driving car {Model} ({Year}).");
    }
}

class Program {
    static void Main(string[] args) {
        List<Vehicle> garage = new List<Vehicle>() {
            new Car("Sedan", 2018),
            new Car("Coupe", 2020),
            new Car("Hatchback", 2015),
        };
        var recentCars = garage.Where(v => v.Year >= 2018);
        foreach (var car in recentCars) {
            car.Drive();
        }
    }
}
""",
        "language": "C#"
    },
    {
        "code": """using System;
using System.Threading.Tasks;

class Demo {
    static async Task Main(string[] args) {
        Console.WriteLine("Starting async demo...");

        string data = await LoadDataAsync();
        Console.WriteLine($"Received data: {data}");

        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
    }

    static async Task<string> LoadDataAsync() {
        await Task.Delay(1000); // simulate I/O delay
        return "Sample Data from C# Async Method";
    }
}
""",
        "language": "C#"
    },

    # ======================================
    # =============== REACT ===============
    # ======================================
    {
        "code": """import React, { useState, useEffect } from 'react';

function App() {
  const [count, setCount] = useState(0);
  const [items, setItems] = useState([]);

  useEffect(() => {
    console.log('Component mounted, fetching data...');
    // Faking an API call
    setTimeout(() => {
      setItems(['Apple', 'Banana', 'Cherry']);
    }, 1000);
  }, []);

  return (
    <div>
      <h1>React Counter</h1>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>

      <h2>Items</h2>
      <ul>
        {items.map((x, i) => <li key={i}>{x}</li>)}
      </ul>
    </div>
  );
}

export default App;
""",
        "language": "React"
    },
    {
        "code": """import React, { useState } from 'react';

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [task, setTask] = useState('');

  const addTodo = () => {
    if (task.trim()) {
      setTodos([...todos, { text: task, done: false }]);
      setTask('');
    }
  };

  const toggleTodo = (index) => {
    const newTodos = [...todos];
    newTodos[index].done = !newTodos[index].done;
    setTodos(newTodos);
  };

  return (
    <div>
      <h1>React Todo List</h1>
      <input value={task} onChange={(e) => setTask(e.target.value)} />
      <button onClick={addTodo}>Add Todo</button>
      <ul>
        {todos.map((t, i) => (
          <li
            key={i}
            style={{ textDecoration: t.done ? 'line-through' : 'none' }}
            onClick={() => toggleTodo(i)}
          >
            {t.text}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
""",
        "language": "React"
    },

    # ======================================
    # ============== NEXTJS ===============
    # ======================================
{
    "code": """import React from 'react';

export default function Home({ message, timestamp }) {
  return (
    <div style={{ margin: '1rem' }}>
      <h1>Home Page</h1>
      <p>{message}</p>
      <hr />
      <section>
        <h2>Extra Content</h2>
        <ul>
          <li>This is a Next.js example page.</li>
          <li>We can fetch data on the server side.</li>
          <li>Timestamp: {timestamp}</li>
          <li>Feel free to scroll around!</li>
        </ul>
      </section>
    </div>
  );
}

export async function getServerSideProps() {
  // Simulate a data fetch
  const message = 'Hello from the server side!';
  const timestamp = new Date().toLocaleString();

  // Return these props to the React component
  return {
    props: {
      message,
      timestamp
    }
  };
}
""",
    "language": "NextJS"
},
{
    "code": """export default async function handler(req, res) {
  if (req.method === 'GET') {
    // If there's a "name" query param, include it in the greeting
    const { name = 'stranger' } = req.query;
    res.status(200).json({
      greeting: `Hello, ${name} from the Next.js API!`,
      note: 'Feel free to scroll through this snippet.'
    });
  } else if (req.method === 'POST') {
    // In a real app, you might parse JSON or perform DB operations
    const body = req.body || {};
    res.status(201).json({
      success: true,
      dataReceived: body,
      message: 'POST data created successfully!'
    });
  } else {
    // Return 405 for other HTTP methods
    res.setHeader('Allow', ['GET', 'POST']);
    res.status(405).json({ error: 'Method Not Allowed' });
  }
}
""",
    "language": "NextJS"
},

]
