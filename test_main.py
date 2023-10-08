"""Testing main.py functionality"""

import pytest
from unittest.mock import patch, call
from main import main

def test_main_functionality():
    with patch('builtins.print') as mock_print, \
         patch('main.extract') as mock_extract, \
         patch('main.load') as mock_load, \
         patch('main.query') as mock_query, \
         patch('main.process_cli_args') as mock_cli_args:

        # Test extract functionality
        mock_cli_args.return_value = lambda: None
        mock_cli_args.return_value.task = 'data_extraction'
        main()
        mock_extract.assert_called_once()
        mock_print.assert_has_calls([
            call('Initiating data extraction...'),
            call('Extraction successful. Data saved at None\n')
        ])

        # Reset mocks
        mock_extract.reset_mock()
        mock_print.reset_mock()

        # Test transform_load functionality
        mock_cli_args.return_value.task = 'data_loading'
        main()
        mock_load.assert_called_once_with('cars.csv')
        mock_print.assert_has_calls([
            call('Initiating data transformation and loading...'),
            call('Transformation and loading completed.\n')
        ])

        # Reset mocks
        mock_load.reset_mock()
        mock_print.reset_mock()

        # Test data_query functionality
        mock_cli_args.return_value.task = 'data_query'
        main()
        mock_query.assert_called_once()
        mock_print.assert_has_calls([
            call('Initiating data querying...'),
            call('Querying process completed.\n')
        ])

        # Reset mocks
        mock_query.reset_mock()
        mock_print.reset_mock()

        # Test complete_etl functionality
        mock_cli_args.return_value.task = 'complete_etl'
        main()
        mock_extract.assert_called_once()
        mock_load.assert_called_once_with(None)
        mock_query.assert_called_once()
        mock_print.assert_has_calls([
            call('Starting the full ETL process...'),
            call('Extraction successful. Data saved at None\n'),
            call('Transformation and loading completed.\n'),
            call('Querying process completed.\n')
        ])

if __name__ == "__main__":
    pytest.main()
