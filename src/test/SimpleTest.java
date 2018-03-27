package test;


import org.apache.commons.lang.StringUtils;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class SimpleTest {
//
//    @Test
//    public void test() {
//        ArrayList<String> list = new ArrayList<>();
//        list.add("foo");
//        list.add("bar");
//
//        Assertions.assertTrue(list.contains("foo"));
//    }
//
//    @Test void testPythonScriptExecution() {
//        try {
////            Process p = Runtime.getRuntime().exec("pwd");
////            Process p = Runtime.getRuntime().exec("pytest /work/priv/python/python-tests");
////            Process p = Runtime.getRuntime().exec("pytest ./");
//            Process p = Runtime.getRuntime().exec("pytest ./test/test_wallet_unittest.py::TestWallet::test_wallet_spend_cash");
//            InputStream inputStream = p.getInputStream();
//            OutputStream outputStream = p.getOutputStream();
//            InputStream errorStream = p.getErrorStream();
//
//            new InputStreamReader(inputStream);
////            new OutputStreamRe(outputStream);
//            new InputStreamReader(errorStream);
//
////            System.out.println("stdin: " + inputStream);
////            System.out.println("stdout: " + outputStream.toString());
////            System.out.println("stderr: " + errorStream.toString());
//
//            Scanner scanner = new Scanner(inputStream).useDelimiter("\\A");
//            String result = scanner.hasNext() ? scanner.next() : "";
//
//
//            System.out.println(result);
//
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }


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
}
