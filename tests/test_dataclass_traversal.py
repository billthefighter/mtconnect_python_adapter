import pytest
from dataclasses import dataclass
from typing import List
from mtconnect.mtstream import find_dataclasses  # Replace 'your_module' with the actual module name

# Example dataclass structures
@dataclass
class Child:
    name: str
    age: int

@dataclass
class Parent:
    child: Child
    job: str

@dataclass
class Family:
    parent: Parent
    last_name: str = "Smith"

# Test data
family_instance = Family(parent=Parent(child=Child(name="John", age=12), job="Engineer"))

# Test cases
def test_find_by_type():
    """Test finding dataclasses by type."""
    result = find_dataclasses(family_instance, target_type=Child)
    assert len(result) == 1
    assert isinstance(result[0], Child)
    assert result[0].name == "John"

def test_find_by_attribute_name():
    """Test finding dataclasses by attribute name."""
    result = find_dataclasses(family_instance, attribute_name="name")
    assert len(result) == 1
    assert hasattr(result[0], "name")
    assert result[0].name == "John"

def test_find_by_attribute_value():
    """Test finding dataclasses by attribute value."""
    result = find_dataclasses(family_instance, attribute_value="Smith")
    assert len(result) == 1
    assert hasattr(result[0], "last_name")
    assert result[0].last_name == "Smith"

def test_find_by_attribute_name_and_value():
    """Test finding dataclasses by both attribute name and value."""
    result = find_dataclasses(family_instance, attribute_name="last_name", attribute_value="Smith")
    assert len(result) == 1
    assert result[0].last_name == "Smith"

def test_find_by_type_and_attribute_value():
    """Test finding dataclasses by type and attribute value."""
    result = find_dataclasses(family_instance, target_type=Parent, attribute_value="Engineer")
    assert len(result) == 1
    assert isinstance(result[0], Parent)
    assert result[0].job == "Engineer"

def test_no_criteria_error():
    """Test that ValueError is raised when no criteria is provided."""
    with pytest.raises(ValueError):
        find_dataclasses(family_instance)

def test_recursion_limit():
    """Test that the recursion limit is respected."""
    result = find_dataclasses(family_instance, target_type=Child, max_depth=1)
    assert len(result) == 0  # Shouldn't find anything because depth is limited to 1

def test_deep_nested_match():
    """Test finding a dataclass deeply nested."""
    result = find_dataclasses(family_instance, attribute_name="job", attribute_value="Engineer")
    assert len(result) == 1
    assert result[0].job == "Engineer"

def test_find_by_all_criteria():
    """Test finding dataclasses by type, attribute name, and value."""
    result = find_dataclasses(family_instance, target_type=Family, attribute_name="last_name", attribute_value="Smith")
    assert len(result) == 1
    assert isinstance(result[0], Family)
    assert result[0].last_name == "Smith"

