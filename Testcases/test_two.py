import pytest

from pkg_resources import iter_entry_points
class TestApi:
    def test_one(self,test_fixture):
        print("one")
    def test_two(self,test_fixture):
        print("two")
    def test_three(self):
        print("three")
@pytest.mark.usefixtures("sql_fix")
class TestApione:
    def test_four(self):
        print("杀杀杀")