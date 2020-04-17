from pathlib import Path
from unittest.mock import mock_open, patch

import pytest
from file import File


class TestFile:
    def setup_method(self):
        self.fake_csv = f"{Path(__file__).parent}/test_data.csv"
        self.fake_json = f"{Path(__file__).parent}/test_data.json"
        self.test_file = File()

    def test_export_json(self):
        test_file_import = self.test_file.import_csv_as_json(self.fake_csv)
        with patch("builtins.open", mock_open()) as m:
            self.test_file.export_json(self.fake_json, test_file_import)

        assert m.called is True

    def test_import_json(self):
        test_file_import = self.test_file.import_csv_as_json(self.fake_csv)

        assert len(test_file_import) == 18

    def test_import_csv_as_json(self):
        test_file_import = self.test_file.import_csv_as_json(self.fake_csv)

        assert len(test_file_import) == 18


if __name__ == "__main__":
    pytest.main()
