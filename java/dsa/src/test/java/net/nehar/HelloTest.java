package net.nehar;

import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

public class HelloTest{

    private static final Logger logger = LogManager.getLogger(HelloTest.class.getName());

    @Before public void setUp(){

    }

    @Test public void testHelloWorld(){
        logger.debug("testHelloWorld...");
        Hello hello = new Hello();
        assertThat(hello.world("Nehar"), is(equalTo("Hello Nehar")));
        logger.debug("...done.");
    }

    @After public void tearDown(){

    }
}