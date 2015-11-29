package net.nehar;

import org.junit.Test;
import org.junit.Before;
import org.junit.After;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

public class HelloTest{

    @Before public void setUp(){

    }

    @Test public void testHelloWorld(){
        Hello hello = new Hello();
        assertThat("Hello Nehar", is(equalTo(hello.world("Nehar"))));

    }

    @After public void tearDown(){

    }
}