# JuniorEx

Dan Aronson's Junior Developer home task

### Installation

Make sure Python3 is installed on your machine and create a dedicated virtual environment.
Than run the following commands:

```sh
$ cd <virtual environment location>
$ pip install -r requirements.txt
```
The above commands will make sure all of the required dependencies are met

### Question 1

#### Solution description:

In order to meet the requested requirements, i decided to implement a hierarchical tree with nodes that holds data objects.
The solution is a generic and can represent any kind of hierarchical tree by defining new objects and assigning its data with minor neccessary code changes
In our case the tree will represent a company structure with hirarchy relationships between employees.

#### בהנחה שפעולה 4 נקראת הרבה, איך זה ישפיע על מבנה הנתונים?

The tree data structure makes it relatively easy to perform search operations.
For future improbvements especialy in case of production, i would consider caching the method results in order to enhance performance.

#### Solution objects:
  - Employee - An objects that holds all of the required employee data.
  - Node - An object that represents a node within the company tree and holds the following attributes:
    1. data - holds an Employee object and its data (can be used with all kinds of objects)
    2. parent_node - in case its not None, holds a Node objects that contains the data of the manager
    3. child_nodes - an array that holds nodes that represents employees of the current node
  - HierarchicalTree - the actual tree that holds the company structure.
    The HierarchicalTree object holds only one attribute which is a reference to the root of the tree
    The following methods are implemented within the HierarchicalTree object:
    1. add_employee - A function that adds a new employee to the organizational structure
    2. delete_employee - A function which deletes an employee from the organizational structure
    3. get_employee - A function which returns the requested employee by employee id
    4. get_first_shared_manager - A function which returns the first manager who manages the two requested employees
    5. get_node - A search method that runs through the nodes of the tree and finds an employee by the employee ID

##### solution tests:

The solution was tested using the build in unittest library
Within "question_1" directory you will be able to find:
1. test_node - a test case to test all of the Node object functionalities
2. test_heirarchical_tree - a test case to test all of the HeirarchicalTree object functionalities


### Question 2

#### Solution description:
The solution was met by implementing a class with abstract methods which all of the other objects will inherent from. in other words, the base class will act as an interface and in case a new template will be required a new object will be defined and will an implementation of the base class.
The HTML parsing framework that was chosen for the given solution is
[beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
 


#### Solution objects:
  - ProfileExtractor - The base object from which all template objects are inhereting
  - ProfileExtractorLinkedIn - A LinkedIn implementation of the ProfileExtractor object
  - ProfileExtractorBackstage - A Backstage implementation of the ProfileExtractor object
  - ProfileExtractorIndeed - A Indeed implementation of the ProfileExtractor object
##### solution tests:

The solution was tested using the build in unittest library
Within "question_2" directory you will be able to find:
1. test_profileExtractorBackstage - a test case to test all of the profileExtractorBackstage object functionalities
2. test_profileExtractorLinkedIn - a test case to test all of the profileExtractorBackstage object functionalities
3. test_profileExtractorIndeed - a test case to test all of the profileExtractorBackstage object functionalities

