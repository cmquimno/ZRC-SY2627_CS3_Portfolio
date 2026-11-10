# Activity 3: Spot the Error! (Session 2 Warm-up)

**Goal:** Understand that `@abstractmethod` is a strict, non-negotiable contract enforced by Python.

---

### 🔍 The Verdict: **Snippet B is the Only Legal Code!**

Here is the breakdown of why Snippet B works perfectly and why the other two crash immediately:

| Snippet | Status | What Python Does / Why it Fails |
| :--- | :--- | :--- |
| **Snippet A** | ❌ **Crashes** | **`TypeError`:** `TempSensor` forgot to implement `get_data`. Even though it added a new `calibrate` method, it failed to fulfill the core blueprint contract required by the parent class. |
| **Snippet B** |  **Success!** | **Runs perfectly.** `PHMeter` correctly overrides and implements the `get_data` method, satisfying the abstract method requirement. |
| **Snippet C** | ❌ **Crashes** | **`TypeError`:** Attempts to directly instantiate the abstract base class `Sensor()`. Python strictly blocks this to prevent incomplete blueprints from being turned into real objects. |

---

### 🚨 What the Errors Look Like Under the Hood

If you try to run **Snippet A** or **Snippet C**, Python stops execution and spits out these exact error messages:

* **Snippet A Error:**
  ```text
  TypeError: Can't instantiate abstract class TempSensor without an implementation for abstract method 'get_data'
  ```
* **Snippet C Error:**
  ```text
  TypeError: Can't instantiate abstract class Sensor without an implementation for abstract method 'get_data'
  ```