import pytest

def test_foo():
    from ghfailwx import foo
    assert foo() is None

@pytest.mark.skip("Avoiding wxPython")
def test_import_wx():
    import wx
