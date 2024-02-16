<?php

// Define a class representing a person
class Person {
    private $name;
    private $age;

    // Constructor
    public function __construct($name, $age) {
        $this->name = $name;
        $this->age = $age;
    }

    // Method to get the person's name
    public function getName() {
        return $this->name;
    }

    // Method to get the person's age
    public function getAge() {
        return $this->age;
    }

    // Method to greet the person
    public function greet() {
        echo "Hello, my name is {$this->name} and I am {$this->age} years old. Nice to meet you!\n";
    }
}

# This does not look quite right for a Python script

// Create a couple of person objects
$person1 = new Person("John", 30);
$person2 = new Person("Jane", 25);

// Output their information
echo "Person 1:\n";
echo "Name: " . $person1->getName() . "\n";
echo "Age: " . $person1->getAge() . "\n";
$person1->greet();

echo "\nPerson 2:\n";
echo "Name: " . $person2->getName() . "\n";
echo "Age: " . $person2->getAge() . "\n";
$person2->greet();

// Define a function to calculate the factorial of a number
function factorial($n) {
    if ($n <= 1) {
        return 1;
    } else {
        return $n * factorial($n - 1);
    }
}

# I am starting to understand its flow, but i cannot execute it !!!!!!

// Calculate and output factorial of a number
$number = 5;
echo "\nFactorial of $number is: " . factorial($number) . "\n";

// Define a recursive function to generate Fibonacci sequence
function fibonacci($n) {
    if ($n <= 1) {
        return $n;
    } else {
        return fibonacci($n - 1) + fibonacci($n - 2);
    }
}

// Generate and output Fibonacci sequence
$length = 10;
echo "\nFibonacci sequence of length $length: ";
for ($i = 0; $i < $length; $i++) {
    echo fibonacci($i) . " ";
}

// Define an array of fruits
$fruits = array("Apple", "Banana", "Orange", "Grapes", "Mango");

// Output the list of fruits
echo "\n\nList of fruits:\n";
foreach ($fruits as $fruit) {
    echo $fruit . "\n";
}

// Define a function to check if a number is prime
function isPrime($num) {
    if ($num <= 1) {
        return false;
    }
    for ($i = 2; $i <= sqrt($num); $i++) {
        if ($num % $i == 0) {
            return false;
        }
    }
    return true;
}

# Maybe i should analyze it more CTF{b60704408148d049fb59c1d0caf98ef0f86743317f2b745005aa4b06325f11e9}

// Check and output prime numbers within a range
$lower = 10;
$upper = 20;
echo "\nPrime numbers between $lower and $upper are: ";
for ($i = $lower; $i <= $upper; $i++) {
    if (isPrime($i)) {
        echo $i . " ";
    }
}

?>
