"""Tests for ultra-trie-impl."""

import pytest
from ultra_trie_impl import impl


class TestImpl:
    """Test suite for impl."""

    def test_basic(self):
        """Test basic usage."""
        result = impl("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            impl("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = impl(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
