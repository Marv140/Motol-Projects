LONG_QUESTIONS = [
    {
"code": """
import math
import random

class Shape:
    \"\"\"A generic shape class\"\"\"
    def __init__(self, name):
        self.name = name
    
    def area(self):
        return 0

class Circle(Shape):
    \"\"\"Circle subclass that calculates area\"\"\"
    def __init__(self, radius):
        super().__init__(\"Circle\")
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

def random_circles(num_circles=3):
    \"\"\"Generate a list of circles with random radii\"\"\"
    circles = []
    for _ in range(num_circles):
        r = random.randint(1, 10)
        circles.append(Circle(r))
    return circles

if __name__ == \"__main__\":
    circles = random_circles(5)
    for c in circles:
        print(f\"A {c.name} with radius {c.radius} has area ~ {c.area():.2f}\")
""",
        "language": "Python"
    },
    {
"code": """
class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }
}

function fetchData(url) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (url === 'fakeapi.com/data') {
        resolve({ data: [1, 2, 3, 4, 5] });
      } else {
        reject(new Error('Invalid URL'));
      }
    }, 1000);
  });
}

async function main() {
  try {
    const person = new Person('Alice', 30);
    person.greet();

    const response = await fetchData('fakeapi.com/data');
    console.log('Fetched data:', response.data);

    const anotherResponse = await fetchData('invalidurl');
    console.log(anotherResponse.data);
  } catch (err) {
    console.error('An error occurred:', err.message);
  }
}

main();""",
        "language": "JavaScript"
    },
    {
"code": """#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;


class Book {
private:
    string title;
    int pages;

public:
    Book(const string &t, int p) : title(t), pages(p) {}
    int getPages() const { return pages; }
    string getTitle() const { return title; }
};

int main() {
    vector<Book> library;
    library.emplace_back(\"C++ Primer\", 1000);
    library.emplace_back(\"Effective C++\", 300);
    library.emplace_back(\"The C++ Programming Language\", 1366);
    library.emplace_back(\"Clean Code\", 464);

    // Sort books by number of pages
    sort(library.begin(), library.end(), [](const Book &a, const Book &b) {
        return a.getPages() < b.getPages();
    });

    cout << \"Books in ascending order of pages:\" << endl;
    for (auto &book : library) {
        cout << book.getTitle() << \" (\" << book.getPages() << \" pages)\" << endl;
    }

    return 0;
}""",
        "language": "C++"
    },
    {
"code": """

module Greetings
  def say_hello
    puts \"Hello from the Greetings module!\"
  end
end

class Animal
  include Greetings

  attr_reader :name

  def initialize(name)
    @name = name
  end

  def speak
    puts \"Generic animal sound...\"
  end
end

class Dog < Animal
  def speak
    puts \"Woof! My name is #{name}.\"
  end
end

class Cat < Animal
  def speak
    puts \"Meow! My name is #{name}.\"
  end
end

if __FILE__ == $0
  animals = [Dog.new(\"Rex\"), Cat.new(\"Misty\")]
  animals.each do |animal|
    animal.say_hello
    animal.speak
    puts \"----\"
  end
end
""",
        "language": "Ruby"
    },
    {
        "code": """
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

abstract class Animal {
    protected String name;
    public Animal(String name) {
        this.name = name;
    }
    public abstract void makeSound();
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }
    @Override
    public void makeSound() {
        System.out.println(name + \" says: Woof!\");
    }
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }
    @Override
    public void makeSound() {
        System.out.println(name + \" says: Meow!\");
    }
}

public class Main {
    public static void main(String[] args) {
        List<Animal> animals = new ArrayList<>();
        animals.add(new Dog(\"Rover\"));
        animals.add(new Cat(\"Whiskers\"));
        animals.add(new Dog(\"Buddy\"));

        // Shuffle them just for fun
        Collections.shuffle(animals);

        for (Animal a : animals) {
            a.makeSound();
        }
    }
}
""",
        "language": "Java"
    }
]
