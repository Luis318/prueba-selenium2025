import unittest
import HtmlTestRunner
from test.Test1 import Test1

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(Test1)
    unittest.TextTestRunner().run(suite)
    
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(
            output="reportes",
            report_title='Reporte de Pruebas automatizadas',
            report_name='Reporte de Pruebas',            
        )
    )