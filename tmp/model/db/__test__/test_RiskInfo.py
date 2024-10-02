import unittest
from unittest.mock import MagicMock, patch
from model.db.RiskInfo import RiskInfo
from model.schema.RiskInfo import RiskInfoDBType

class TestRiskInfo(unittest.TestCase):

    @patch('model.db.RiskInfo.Pgsql')
    def setUp(self, MockPgsql):
        self.mock_pgsql_instance = MockPgsql.return_value
        self.mock_pgsql_instance.connect.return_value = self.mock_pgsql_instance
        self.risk_info = RiskInfo(DB=self.mock_pgsql_instance)

    def test_insert_record(self):
        data = RiskInfoDBType(
            company_code='1234',
            audit_risk=1,
            board_risk=2,
            compensation_risk=3,
            shareholder_rights_risk=4,
            overall_risk=5,
            governance_epoch_date='2023-01-01',
            compensation_as_of_epoch_date='2023-01-01',
            max_age=10
        )
        self.risk_info.insert_record(data)
        self.mock_pgsql_instance.execute.assert_called_once()

    def test_update_record(self):
        self.risk_info.update_record('1', company_code='1234', audit_risk=1)
        self.mock_pgsql_instance.execute.assert_called_once()

    def test_delete_record(self):
        self.risk_info.delete_record('1')
        self.mock_pgsql_instance.execute.assert_called_once_with("DELETE FROM risk_info WHERE id = %s", ('1',))

    def test_get_record_by_id(self):
        self.mock_pgsql_instance.execute.return_value = [{'id': '1'}]
        record = self.risk_info.get_record_by_id('1')
        self.mock_pgsql_instance.execute.assert_called_once_with("SELECT * FROM risk_info WHERE id = %s", ('1',))
        self.assertEqual(record, [{'id': '1'}])

    def test_get_latest_10_records_by_company_code(self):
        self.mock_pgsql_instance.execute.return_value = [{'company_code': '1234'}]
        records = self.risk_info.get_latest_10_records_by_company_code('1234')
        self.mock_pgsql_instance.execute.assert_called_once_with("""
        SELECT * FROM
            risk_info
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT 10
        """, ('1234',))
        self.assertEqual(records, [{'company_code': '1234'}])

    def test_get_latest_record_by_company_code(self):
        self.mock_pgsql_instance.execute.return_value = [{'company_code': '1234'}]
        record = self.risk_info.get_latest_record_by_company_code('1234')
        self.mock_pgsql_instance.execute.assert_called_once_with("""
        SELECT * FROM
            risk_info
        WHERE
            company_code = %s
        ORDER BY
            createdAt DESC
        LIMIT 1
        """, ('1234',))
        self.assertEqual(record, [{'company_code': '1234'}])

if __name__ == '__main__':
    unittest.main()