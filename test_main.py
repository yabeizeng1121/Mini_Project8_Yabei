"""
Test goes here

"""

import pytest
from unittest.mock import patch
from main import main

def test_main_function():
    with patch('builtins.input', return_value=''):  # Mocking user input
        with patch('main.extract') as mock_extract:
            with patch('main.load') as mock_load:
                with patch('main.query') as mock_query:
                    main()
                    mock_extract.assert_called_once()
                    mock_load.assert_called_once()
                    mock_query.assert_called_once()

if __name__ == "__main__":
    pytest.main()
