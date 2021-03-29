import pytest
from django.test import TransactionTestCase
from django.core.exceptions import ValidationError
from restoration.apps.furniture.models import Legs, Feet, Tables


class TablesTest(TransactionTestCase):
    def test_create(self):
        l1 = Legs(pk=1, name='Leg1', size=4)
        l1.save()
        f1 = Feet(pk=1, radius=1, name='Feet12')
        f1.save()
        Tables(pk=1, name="Table1", legs=l1, leg_count=4, feet=f1, feet_count=4).save()
        Tables(pk=2, name="Table2", legs=l1, leg_count=3, feet=f1, feet_count=3).save()
        assert Tables.objects.count() == 2
        assert Tables.objects.get(pk=1).name == "Table1"

    def test_list(self):
        l1 = Legs(pk=1, name='Leg1', size=4)
        l1.save()
        f1 = Feet(pk=1, radius=1, name='Feet12')
        f1.save()
        Tables(pk=1, name="Table1", legs=l1, leg_count=4, feet=f1, feet_count=4).save()
        Tables(pk=2, name="Table2", legs=l1, leg_count=3, feet=f1, feet_count=3).save()
        assert Tables.objects.count() == 2

    def test_detail(self):
        l1 = Legs(pk=1, name='Leg1', size=4)
        l1.save()
        f1 = Feet(pk=1, radius=1, name='Feet12')
        f1.save()
        Tables(pk=1, name="Table1", legs=l1, leg_count=4, feet=f1, feet_count=4).save()
        Tables(pk=2, name="Table2", legs=l1, leg_count=3, feet=f1, feet_count=3).save()
        assert Tables.objects.get(pk=2).name == "Table2"

    def test_update(self):
        l1 = Legs(pk=1, name='Leg1', size=4)
        l1.save()
        f1 = Feet(pk=1, radius=1, name='Feet12')
        f1.save()
        t1 = Tables(pk=1, name="Table1", legs=l1, leg_count=4, feet=f1, feet_count=4)
        t1.save()
        t2 = Tables(pk=2, name="Table2", legs=l1, leg_count=3, feet=f1, feet_count=3)
        t2.save()
        t2.name = "Updated Table2"
        t2.save()
        assert Tables.objects.get(pk=2).name == "Updated Table2"

    def test_delete(self):
        l1 = Legs(pk=1, name='Leg1', size=4)
        l1.save()
        f1 = Feet(pk=1, radius=1, name='Feet1')
        f1.save()
        Tables(pk=1, name="Table1", legs=l1, leg_count=4, feet=f1, feet_count=4).save()
        Tables(pk=2, name="Table2", legs=l1, leg_count=3, feet=f1, feet_count=3).save()
        t3 = Tables(pk=3, name="Table3", legs=l1, leg_count=5, feet=f1, feet_count=5)
        t3.save()
        Tables.objects.get(pk=3).delete()
        assert Tables.objects.count() == 2


class LegsTest(TransactionTestCase):

    def test_create(self):
        l1 = Legs(pk=1, name='Leg1', size=4)
        l1.save()
        assert Legs.objects.count() == 1

    def test_list(self):
        Legs(pk=1, name='Leg1', size=4).save()
        Legs(pk=2, name='Leg2', size=10).save()

        assert Legs.objects.count() == 2

    def test_detail(self):
        Legs(pk=1, name='Leg1', size=4).save()
        Legs(pk=2, name='Leg2', size=10).save()
        assert Legs.objects.get(pk=1).name == 'Leg1'

    def test_update(self):
        l1 = Legs(pk=1, name='Leg1', size=4)
        l1.save()
        l1.name = 'Updated Leg1'
        l1.save()
        assert Legs.objects.get(pk=1).name == 'Updated Leg1'

    def test_delete(self):
        l1 = Legs(pk=1, name='Leg1', size=4)
        l1.save()
        l2 = Legs(pk=2, name='Leg2', size=10)
        l2.save()
        assert Legs.objects.count() == 2
        Legs.objects.get(pk=1).delete()
        assert Legs.objects.count() == 1


class FeetTest(TransactionTestCase):
    def test_create_circle(self):
        f1 = Feet(pk=5, radius=1, name='Feet12')
        f1.save()
        assert Feet.objects.count() == 1

    def test_create_rectangle(self):
        f2 = Feet(pk=2, length=15, width=2.7, name='Feet13')
        f2.save()
        assert Feet.objects.count() == 1

    def test_invalid_data(self):
        with pytest.raises(ValidationError) as excinfo:
            f3 = Feet(pk=3, radius=1, length=3.5)
            f3.save()
        assert "ValidationError" in str(excinfo)

    def test_list(self):
        f1 = Feet(pk=5, radius=1, name='Feet12')
        f1.save()
        f2 = Feet(pk=2, length=15, width=2.7, name='Feet13')
        f2.save()
        assert Feet.objects.count() == 2

    def test_detail(self):
        f2 = Feet(pk=2, length=15, width=2.7, name='Feet13')
        f2.save()
        assert Feet.objects.get(pk=2).name == f2.name

    def test_update(self):
        f1 = Feet(pk=5, radius=1, name='Feet12')
        f1.save()
        f1.name = 'Updated Feet12'
        f1.save()
        assert Feet.objects.get(pk=5).name == 'Updated Feet12'

    def test_delete(self):
        f1 = Feet(pk=5, radius=1, name='Feet12')
        f1.save()
        f2 = Feet(pk=2, length=15, width=2.7, name='Feet13')
        f2.save()
        assert Feet.objects.count() == 2
        Feet.objects.get(pk=2).delete()
        assert Feet.objects.count() == 1
