package test;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;

public class SimpleTest {

    @Test
    public void test() {
        ArrayList<String> list = new ArrayList<>();
        list.add("foo");
        list.add("bar");

        Assertions.assertTrue(list.contains("foo"));
    }

}
