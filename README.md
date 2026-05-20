# Health Record Symmetry Checker

## Introduction

This project analyzes a patient’s health record using a singly linked list.

Each node in the linked list represents a health metric recorded over time, such as blood sugar levels or heart rate measurements.

The goal of this project is to determine whether the sequence of health metrics is symmetric (a palindrome).

A symmetric sequence reads the same forward and backward.

Example:

80 → 90 → 100 → 90 → 80

This sequence is symmetric because both directions are identical.

The solution uses the fast and slow pointer technique along with reversing the second half of the linked list to achieve an efficient solution.

---

# Clarifying Questions

1. Can the linked list be empty?

Yes. An empty list is considered symmetric.

2. Can the linked list contain one node?

Yes. A single node is symmetric.

3. Are health metric values integers?

Yes.

4. Can duplicate values exist?

Yes.

5. Should the solution be optimized?

Yes. The target complexity is O(n) time and O(1) space.

---

# Assumptions

- The linked list is singly linked.
- Each node contains one health metric value.
- The input list is valid.
- Values may repeat.
- The function returns:
  - True if the sequence is symmetric
  - False otherwise

---

# Diagram

        head
          ↓
     [80] → [90] → [100] → [90] → [80] → None

Forward:
80 90 100 90 80

Backward:
80 90 100 90 80

Result:
Symmetric

---

# Flowchart

START
   ↓
Find Middle of Linked List
   ↓
Reverse Second Half
   ↓
Compare Both Halves
   ↓
All Values Match?
   ↓ YES        ↓ NO
Return True   Return False

---

# Solution Explanation

Step 1:

Use two pointers called slow and fast to find the middle of the linked list.

- The slow pointer moves one node at a time.
- The fast pointer moves two nodes at a time.

When the fast pointer reaches the end, the slow pointer will be at the middle.

Step 2:

Reverse the second half of the linked list in place.

This avoids using extra memory and improves space efficiency.

Step 3:

Compare the first half of the linked list with the reversed second half.

- If all values match, return True.
- If any values differ, return False.

---

# Time Complexity

O(n)

- Finding the middle takes O(n)
- Reversing the second half takes O(n)
- Comparing both halves takes O(n)

Overall:
O(n)

---

# Space Complexity

O(1)

The algorithm only uses pointers and does not create extra arrays or stacks.

---

# Test Cases

## Normal Cases

1. Odd-length palindrome

80 → 90 → 100 → 90 → 80

Expected Output:
True

2. Even-length palindrome

70 → 85 → 85 → 70

Expected Output:
True

3. Non-palindrome

60 → 70 → 80

Expected Output:
False

---

## Edge Cases

1. Empty linked list

Expected Output:
True

2. Single node

100

Expected Output:
True

3. Two different nodes

90 → 100

Expected Output:
False

---

# How to Run Tests

Run the following command in the terminal:

python3 -m unittest test_solution.py

---

# Files Included

- main.py
- test_solution.py
- README.md
- diagram.png

---

# Video Presentation

The video presentation explains:

- Problem understanding
- Clarifying questions
- Diagram walkthrough
- Code explanation
- Test case demonstration
- Time and space complexity
