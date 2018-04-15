package tests;


import com.google.gson.Gson;
import enums.LivetestErrorCode;
import exceptions.LivetestException;
import model.TestCaseCoverage;
import org.apache.commons.lang.StringUtils;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import subproc.PytestReportProcesor;
import utils.FileUtils;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class SimpleTest {

    @Test void testPythonScriptExecution() {
        try {
            Process p = Runtime.getRuntime().exec(
                "pytest /work/priv/python/python-tests/tests/test_wallet_pytest.py::test_wallet_spend_cash\n");
            InputStream inputStream = p.getInputStream();
            InputStream errorStream = p.getErrorStream();

            new InputStreamReader(inputStream);
            new InputStreamReader(errorStream);

            //            Scanner scannerInput = new Scanner(inputStream).useDelimiter("\\A");
            //            String resultInput = scannerInput.hasNext() ? scannerInput.next() : "";

            Scanner scannerError = new Scanner(inputStream).useDelimiter("\\A");
            if (scannerError.hasNext()) {
                String resultError = scannerError.hasNext() ? scannerError.next() : "";
                System.out.println(resultError);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Test void testPythonScriptCheckErrors() {
        try {
            String filePath = "/work/priv/python/python-tests/account/wallet.py";
            Process p = Runtime.getRuntime().exec("python -m py_compile " + filePath);

            InputStream errorStream = p.getErrorStream();

            Scanner scannerError = new Scanner(errorStream).useDelimiter("\\A");

            if (scannerError.hasNext()) {
                String resultError = scannerError.hasNext() ? scannerError.next() : "";
                System.out.println(resultError);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    @Test void testLineResolver() {
        String fileContent =
            "import pytest\n" + "from account.wallet import Wallet, InsufficientAmount\n" + "\n"
                + "\n" + "def test_default_initial_amount():\n" + "    account = Wallet()\n"
                + "    assert account.balance == 0\n" + "\n" + "\n"
                + "def test_setting_initial_amount():\n" + "    account = Wallet(100)\n"
                + "    assert account.balance == 100\n" + "\n" + "\n"
                + "def test_wallet_add_cash():\n" + "    account = Wallet(10)\n"
                + "    account.add_cash(90)\n" + "    assert account.balance == 100\n" + "\n"
                + " \n" + "def test_wallet_spend_cash():\n" + "    account = Wallet(20)\n"
                + "    account.spend_cash(10)\n" + "    assert account.balance == 10\n" + "\n"
                + "\n" + "def test_wallet_spend_cash_raises_exception_on_insufficient_amount():\n"
                + "    account = Wallet()\n" + "    with pytest.raises(InsufficientAmount):\n"
                + "        account.spend_cash(100)\n" + "\n" + "\n" + "def test_foo():\n"
                + "    print(\"hi\")";
        int offset = 372; // Line 20
        int line = StringUtils.countMatches(fileContent.substring(0, offset), "\n") + 1;
        Assertions.assertEquals(line, 20);
    }

    @Test void testCoverageInfoReady() {
        List<String> lines;
        try {
            lines = FileUtils.readLines("/work/priv/python/python-tests/.livetest-coverage.json");
        } catch (IOException e) {
            throw new LivetestException(LivetestErrorCode.NO_COVERAGE_FILE_AVAILABLE);
        }


        Gson gson = new Gson();
        List<TestCaseCoverage> coverages = new ArrayList<>();

        for (String line : lines) {
            coverages.add(gson.fromJson(line, TestCaseCoverage.class));
        }

        System.out.println("Number of loaded test case coverages: " + coverages.size());
    }

    @Test void pytestToTestNamePathMapTest() {
        String report =
            "============================= test session starts ==============================\n"
                + "platform darwin -- Python 3.6.5, pytest-3.5.0, py-1.5.3, pluggy-0.6.0 -- /usr/local/opt/python/bin/python3.6\n"
                + "cachedir: ../../../../work/priv/python/python-tests/.pytest_cache\n"
                + "Livetest plugin running...\n"
                + "rootdir: /work/priv/python/python-tests, inifile:\n" + "plugins: cov-2.5.1\n"
                + "collecting ... collected 5 items\n" + "\n"
                + "../../../../work/priv/python/python-tests/tests/test_wallet_pytest.py::test_default_initial_amount PASSED [ 20%]\n"
                + "../../../../work/priv/python/python-tests/tests/test_wallet_pytest.py::test_setting_initial_amount PASSED [ 40%]\n"
                + "../../../../work/priv/python/python-tests/tests/test_wallet_pytest.py::test_wallet_add_cash PASSED [ 60%]\n"
                + "../../../../work/priv/python/python-tests/tests/test_wallet_pytest.py::test_wallet_spend_cash PASSED [ 80%]\n"
                + "../../../../work/priv/python/python-tests/tests/test_wallet_pytest.py::test_wallet_spend_cash_raises_exception_on_insufficient_amount PASSED [100%]\n"
                + "\n"
                + "=========================== 5 passed in 0.45 seconds ===========================\n";

        Map<String, String> map = PytestReportProcesor.getTestNamePathMapping(report);

        Assertions.assertTrue(map.get("test_default_initial_amount")
            .equalsIgnoreCase("/work/priv/python/python-tests/tests/test_wallet_pytest.py"));
        Assertions.assertTrue(map.get("test_wallet_add_cash")
            .equalsIgnoreCase("/work/priv/python/python-tests/tests/test_wallet_pytest.py"));
        Assertions.assertTrue(map.keySet().size() == 5);
    }
}
