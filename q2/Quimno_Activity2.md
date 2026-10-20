# Activity 2: Inheritance Class Diagrams
**Name:** Castor Troy M. Quimno

## 1. Single Inheritance Model

### Structural Proof
* **Attributes:** Both classes leave their data attribute blocks empty because neither class defines a constructor (`__init__`) or stores instance variables.
* **Methods:** `Parent` exposes the behavior `func1()`. `Child` inherits `func1()` and introduces its unique behavior `func2()`.

## 2. Multilevel Inheritance Model
### Structural Proof
* **Attributes:** Each class initializes and encapsulates unique state data. `Grandfather` stores `grandfathername`, `Father` tracks `fathername`, and `Son` tracks `sonname`.
* **Methods:** Each class provides an active initialization hook (`__init__`). The terminal leaf class, `Son`, implements a specialized behavior method named `print_name()` which extracts and prints ancestral data strings up the pipeline.

## 3. Hierarchical Inheritance Model
### Structural Proof
* **Attributes:** No local or shared variables are tracked across this module, rendering the attribute blocks empty.
* **Methods:** A single root base class (`Parent`) shares `func1()` downward simultaneously. `Child1` and `Child2` branch into isolated pathways, implementing `func2()` and `func3()` respectively without knowing or accessing each other's specialized methods.