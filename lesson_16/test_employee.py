import pytest
from lesson_16.homework_16_1 import Employee, Manager, Developer, TeamLead

def test_team_lead_has_attributes():
    tl = TeamLead("Alex", 5000, "IT", "Python", 5)

    # из Employee
    assert hasattr(tl, "name")
    assert hasattr(tl, "salary")

    # из Manager
    assert hasattr(tl, "department")

    # из Developer
    assert hasattr(tl, "programming_language")

    # свой собственный
    assert hasattr(tl, "team_size")