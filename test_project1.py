import unittest
import unittest.mock
import project1 as pj
import Device as dc
from pathlib import Path

class propagate(unittest.TestCase):

    def test_device_list(self):
        lis = ['PROPAGATE 1 2 750', 'PROPAGATE 2 3 1250', 'PROPAGATE 3 4 500', 'PROPAGATE 4 1 1000']
        self.assertListEqual(dc.device_list('../samples/sample_input.txt'), lis)
    def test_alert_list(self):
        lis = [("ALERT 1 Trouble 0"), ('ALERT 1 rip 100'), ('CANCEL 1 Trouble 2200'), ('CANCEL 3 rip 2300')]
        self.assertListEqual(dc.alert_lis('../samples/sample_input.txt'), lis)


    def test_store_alert(self):
        lis = [("ALERT 1 Trouble 0"), ('ALERT 1 rip 100'), ('CANCEL 1 Trouble 2200'), ('CANCEL 3 rip 2300')]
        lis2 = [("ALERT", "0", "1", "Trouble"), ('ALERT', '100', '1',  'rip'), ('CANCEL', '2200', '1', 'Trouble'), ('CANCEL', '2300', '3', 'rip')]
        self.assertListEqual(dc.store_alert(lis), lis2)

    def test_store_device(self):
        dic = {'1': [('2', '750')], '2': [('3', '1250')], '3': [('4', '500')], '4': [('1', '1000')]}
        lis = dc.device_list('../samples/sample_input.txt')
        self.assertDictEqual(dc.store_device(lis), dic)

    def test_store_device2(self):
        dic ={'1': [('2', '750'), ('6', '750')], '2': [('3', '1250')], '3': [('4', '500')], '4': [('1', '1000'), ('5', '1000')]}
        lis = dc.device_list("../samples/test_input.txt ")
        self.assertDictEqual(dc.store_device(lis), dic)

    def test_sorted_alert_lis(self):
        lis = [("ALERT", "300", "3", "Trouble"), ('ALERT', '400', '4',  'Trouble'), ('ALERT', '200', '1', 'Trouble'), ('ALERT', '200', '2', 'Trouble')]
        sorted_lis = [("ALERT", "200", "1", "Trouble"), ('ALERT', '200', '2',  'Trouble'), ('ALERT', '300', '3', 'Trouble'), ('ALERT', '400', '4', 'Trouble')]
        self.assertListEqual(dc.sorted_alert_lis(lis), sorted_lis)

    def test_check_file(self):
        test = '../samples/sample_input.txt'
        test2 = "hello"
        self.assertTrue(pj.check_file(Path(test)))
        self.assertFalse(pj.check_file(Path(test2)))


    def test_Path_input(self):
        with unittest.mock.patch('builtins.input', return_value="../sample_input.txt"):
            self.assertEqual(pj._read_input_file_path(), Path("../sample_input.txt"))

    def test_main(self):
        output_str = '@0 #1 SENT ALERT TO #2: Trouble\n@750 #2 RECEIVED ALERT FROM #1: Trouble\n@750 #2 SENT ALERT TO #3: Trouble\n@2000 #3 RECEIVED ALERT FROM #2: Trouble\n@2000 #3 SENT ALERT TO #4: Trouble\n@2200 #1 SENT CANCELLATION TO #2: Trouble\n@2500 #4 RECEIVED ALERT FROM #3: Trouble\n@2500 #4 SENT ALERT TO #1: Trouble\n@2950 #2 RECEIVED CANCELLATION FROM #1: Trouble\n@2950 #2 SENT CANCELLATION TO #3: Trouble\n@3500 #1 RECEIVED ALERT FROM #4: Trouble\n@4200 #3 RECEIVED CANCELLATION FROM #2: Trouble\n@4200 #3 SENT CANCELLATION TO #4: Trouble\n@4700 #4 RECEIVED CANCELLATION FROM #3: Trouble\n@4700 #4 SENT CANCELLATION TO #1: Trouble\n@5700 #1 RECEIVED CANCELLATION FROM #4: Trouble\n'
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()) as output:
            with unittest.mock.patch('builtins.input', return_value="../samples/sample_input2.txt"):
                pj.main()
        self.assertEqual(output.getvalue(), output_str)

    def test_main2(self):
        output_str = "FILE NOT FOUND\n"
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()) as output:
            with unittest.mock.patch('builtins.input', return_value="dne"):
                pj.main()
        self.assertEqual(output.getvalue(), output_str)

    def test_main3(self):
        output_str = '@0 #1 SENT ALERT TO #2: Trouble\n@0 #1 SENT ALERT TO #5: Trouble\n@750 #2 RECEIVED ALERT FROM #1: Trouble\n@750 #5 RECEIVED ALERT FROM #1: Trouble\n@750 #2 SENT ALERT TO #3: Trouble\n@750 #2 SENT ALERT TO #6: Trouble\n@2000 #3 RECEIVED ALERT FROM #2: Trouble\n@2000 #3 SENT ALERT TO #4: Trouble\n@2200 #1 SENT CANCELLATION TO #2: Trouble\n@2200 #1 SENT CANCELLATION TO #5: Trouble\n@2250 #6 RECEIVED ALERT FROM #2: Trouble\n@2500 #4 RECEIVED ALERT FROM #3: Trouble\n@2500 #4 SENT ALERT TO #1: Trouble\n@2950 #2 RECEIVED CANCELLATION FROM #1: Trouble\n@2950 #5 RECEIVED CANCELLATION FROM #1: Trouble\n@2950 #2 SENT CANCELLATION TO #3: Trouble\n@2950 #2 SENT CANCELLATION TO #6: Trouble\n@3500 #1 RECEIVED ALERT FROM #4: Trouble\n@4200 #3 RECEIVED CANCELLATION FROM #2: Trouble\n@4200 #3 SENT CANCELLATION TO #4: Trouble\n@4450 #6 RECEIVED CANCELLATION FROM #2: Trouble\n@4700 #4 RECEIVED CANCELLATION FROM #3: Trouble\n@4700 #4 SENT CANCELLATION TO #1: Trouble\n@5700 #1 RECEIVED CANCELLATION FROM #4: Trouble\n'
        import contextlib
        import io
        with contextlib.redirect_stdout(io.StringIO()) as output:
            with unittest.mock.patch('builtins.input', return_value="../samples/test_input2.txt"):
                pj.main()
        self.assertEqual(output.getvalue(), output_str)
if __name__ == '__main__':
    unittest.main()
