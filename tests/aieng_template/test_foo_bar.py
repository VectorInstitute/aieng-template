"""Integration test example."""

import pytest

from aieng_template import foo, bar


@pytest.mark.integration_test()
def test_foo_bar() -> None:
    """Test foo and bar."""
    foobar = foo() + bar()
    assert foobar == "foobar"
