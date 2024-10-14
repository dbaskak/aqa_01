from aqa_01.lesson_16.homework_16_1 import TeamLead

def test_teamlead_attributes():
    lead = TeamLead("Jack Black", 200000, "AQA", "Python", 7)

    assert hasattr(lead, "name"), "Attribute 'name' missing"
    assert hasattr(lead, "salary"), "Attribute 'salary' missing"
    assert hasattr(lead, "department"), "Attribute 'department' missing"
    assert hasattr(lead, "programming_language"), "Attribute 'programming_language' missing"
    assert hasattr(lead, "team_size"), "Attribute 'team_size' missing"

    print("All attributes are present and correct.")

