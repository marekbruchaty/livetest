package test;


import com.google.gson.Gson;
import enums.LivetestErrorCode;
import exceptions.LivetestException;
import model.CoverageMapping;
import model.TestCaseCoverage;
import org.apache.commons.lang.StringUtils;
import org.apache.xmlbeans.impl.xb.ltgfmt.TestCase;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import resources.DataStore;
import utils.FileUtils;

import javax.xml.bind.SchemaOutputResolver;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class SimpleTest {

    @Test
    public void test() {
        ArrayList<String> list = new ArrayList<>();
        list.add("foo");
        list.add("bar");

        Assertions.assertTrue(list.contains("foo"));
    }

    @Test void testPythonScriptExecution() {
        try {
            Process p = Runtime.getRuntime().exec("pytest /work/priv/python/python-tests");
//            Process p = Runtime.getRuntime().exec("pytest ./test/test_wallet_unittest.py::TestWallet::test_wallet_spend_cash");
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
                //TODO throw new error ...
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @Test void testPythonScriptCheckErrors() {
        try {
            String filePath = "/work/priv/pytest-livetest/example_project/account/wallet.py";
            Process p = Runtime.getRuntime().exec("python -m py_compile "  + filePath);

            InputStream errorStream = p.getErrorStream();

            Scanner scannerError = new Scanner(errorStream).useDelimiter("\\A");

            if (scannerError.hasNext()) {
                String resultError = scannerError.hasNext() ? scannerError.next() : "";
                System.out.println(resultError);
                //TODO throw new error ...
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }


    @Test void testLineResolver() {
        String fileContent = "import pytest\n"
            + "from account.wallet import Wallet, InsufficientAmount\n" + "\n" + "\n"
            + "def test_default_initial_amount():\n" + "    account = Wallet()\n"
            + "    assert account.balance == 0\n" + "\n" + "\n"
            + "def test_setting_initial_amount():\n" + "    account = Wallet(100)\n"
            + "    assert account.balance == 100\n" + "\n" + "\n" + "def test_wallet_add_cash():\n"
            + "    account = Wallet(10)\n" + "    account.add_cash(90)\n"
            + "    assert account.balance == 100\n" + "\n" + " \n"
            + "def test_wallet_spend_cash():\n" + "    account = Wallet(20)\n"
            + "    account.spend_cash(10)\n" + "    assert account.balance == 10\n" + "\n" + "\n"
            + "def test_wallet_spend_cash_raises_exception_on_insufficient_amount():\n"
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
//            lines = FileUtils.readLines(
//                DataStore.getInstance().getActiveProject().getBasePath()
//                    + "/.livetest-coverage.json");
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
}
