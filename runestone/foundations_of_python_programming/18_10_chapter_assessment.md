# 18.10. Chapter Assessment

The function _mySum_ is supposed to return the sum of a list of numbers
(and 0 if that list is empty), but it has one or more errors in it.
Use this space to write test cases to determine what errors there are.
You will be using this information to answer the next set of multiple
choice questions.
```python
import unittest


class Test(unittest.TestCase):
    
    def test_mySum_sum(self):
        self.assertEqual(mySum([1, 2]), 3)
        
    def test_mySum_none(self):
        self.assertEqual(mySum([]), 0)
       
    def test_mySum_one_element(self):
        self.assertEqual(mySum([1]), 1)


if __name__ == "__main__":
    unittest.main()

```

    Fail: Expected None to equal 0
    Tests failed in test_mySum_none 
    Fail: Expected None to equal 3
    Tests failed in test_mySum_sum 
    Ran 3 tests, passed: 1 failed: 2

Which of the following cases fail for the mySum function?

- [X] A. an empty list
- [ ] B. a list with one item
- [X] C. a list with more than one item

> ✔️\
> Correct, 0 is not returned if the function is given an empty list.\
> Correct, a list with more than one item does not provide the correct response.

Are there any other cases, that we can determine based on the current
structure of the function, that also fail for the mySum function?

- [ ] A. Yes
- [X] B. No

> ✔️ Correct. At the moment we can't tell if other cases would fail
> (such as combining integers and floats), but it is possible that 
> he function could have more issues once the current issues are fixed.

---

**The class Student is supposed to accept two arguments in its constructor**:
  - A name string
  - An optional integer representing the number of years the student has been at Michigan (default:1)

**Every student has three instance variables**:
  - _self.name_ (set to the name provided)
  - _self.years_UM_ (set to the number of years the student has been at Michigan)
  - _self.knowledge_ (initialized to 0)

**There are three methods**:
  - _.study()_ should increase self.knowledge by 1 and return None
  - _.getKnowledge()_ should return the value of self.knowledge
  - _.year_at_umich()_ should return the value of self.years_UM

There are one or more errors in the class. Use this space to write test cases
to determine what errors there are. You will be using this information to
answer the next set of multiple choice questions.
```python
import unittest


class Test(unittest.TestCase):
    
    def setUp(self):
        self.student = Student("John", 3)
    
    def test_init(self):
        self.assertEqual(self.student.name, "John")
        self.assertEqual(self.student.years_UM, 3)
        self.assertEqual(self.student.knowledge, 0)
    
    def test_study(self):
        self.student.study()
        self.assertEqual(self.student.knowledge, 1)
    
    def test_get_knowledge(self):
        self.assertEqual(self.student.getKnowledge(), 0)
    
    def test_year_at_umich(self):
        self.assertEqual(self.student.year_at_umich(), 1)


if __name__ == "__main__":
    unittest.main()

```

    Fail: Expected None to equal 0
    Tests failed in test_get_knowledge 
    Fail: Expected 1 to equal 3
    Tests failed in test_init 
    Fail: Expected 0 to equal 1
    Tests failed in test_study 
    Ran 4 tests, passed: 1 failed: 3

Which of the following cases fail for the Student class?
- [ ] A. the method study does not return None
- [ ] B. the optional integer in the constructor is not optional
- [X] C. the attributes/instance variables are not correctly assigned in the constructor
- [X] D. the method study does not increase self.knowledge
- [ ] E. the method year_at_umich does not return the value of self.years_UM

> ✔️\
> Correct! The constructor does not actually use the optional integer
> that is provided. Instead it sticks with using the default value.
> Correct! Study does not increase the self.knowledge.

Are there any other cases, that we can determine based on the current
structure of the class, that also fail for the Student class?

- [X] A. Yes 
- [ ] B. No

> ✔️ Correct! There is an issue with the getKnowledge method because
> it returns None when self.knowledge is 0, even though it returns
> the correct value when self.knowledge is non-zero.
