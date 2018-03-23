package test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.util.ArrayList;
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
//            Process p = Runtime.getRuntime().exec("pwd");
//            Process p = Runtime.getRuntime().exec("pytest /work/priv/python/python-tests");
//            Process p = Runtime.getRuntime().exec("pytest ./");
            Process p = Runtime.getRuntime().exec("pytest ./test/test_wallet_unittest.py::TestWallet::test_wallet_spend_cash");
            InputStream inputStream = p.getInputStream();
            OutputStream outputStream = p.getOutputStream();
            InputStream errorStream = p.getErrorStream();

            new InputStreamReader(inputStream);
//            new OutputStreamRe(outputStream);
            new InputStreamReader(errorStream);

//            System.out.println("stdin: " + inputStream);
//            System.out.println("stdout: " + outputStream.toString());
//            System.out.println("stderr: " + errorStream.toString());

            Scanner scanner = new Scanner(inputStream).useDelimiter("\\A");
            String result = scanner.hasNext() ? scanner.next() : "";


            System.out.println(result);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
