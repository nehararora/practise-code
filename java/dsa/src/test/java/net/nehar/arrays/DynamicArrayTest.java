package net.nehar.arrays;

/**
 * Dynamic Array test cases.
 *
 * Created by nehar on 11/29/15.
 */

// test imports
import org.junit.Test;
import org.junit.Before;
import org.junit.After;
import static org.junit.Assert.*;
import static org.hamcrest.CoreMatchers.*;

// use spring to verify internals match expectations as well.
import org.springframework.test.util.ReflectionTestUtils;

// logging imports
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class DynamicArrayTest {

    private Logger logger = LogManager.getLogger(DynamicArrayTest.class);

    @Before public void setUp(){
    }

    @After public void tearDown(){

    }

    @Test public void testArrayCreation(){
        logger.debug("testArrayCreation...");
        DynamicArray<String> a = new DynamicArray<String>();

        // verify size
        assertThat(a.size(), is(equalTo(0)));

        // verify internals
        assertThat((Integer)ReflectionTestUtils.getField(a, "capacity"),
                is(equalTo(1)));

        logger.debug("...Done.");
    }

    @Test public void testAdd(){
        logger.debug("testAdd...");
        DynamicArray<Integer> a = new DynamicArray<Integer>();
        a.add(1);
        // verify size
        assertThat(a.size(), is(equalTo(1)));

        // verify internals
        assertThat((Integer)ReflectionTestUtils.getField(a, "capacity"),
                is(equalTo(1)));

        // verify dynamic resize...
        a.add(2);
        assertThat(a.size(), is(equalTo(2)));
        assertThat((Integer)ReflectionTestUtils.getField(a, "capacity"),
                is(equalTo(2)));

        // capacity should double again - current:2, adding element goes past.
        a.add(3);
        assertThat(a.size(), is(equalTo(3)));
        assertThat((Integer)ReflectionTestUtils.getField(a, "capacity"),
                is(equalTo(4)));

        // capacity stays the same item count goes up.
        a.add(4);
        assertThat(a.size(), is(equalTo(4)));
        assertThat((Integer)ReflectionTestUtils.getField(a, "capacity"),
                is(equalTo(4)));

        // at max capacity - should double again.
        a.add(5);
        assertThat(a.size(), is(equalTo(5)));
        assertThat((Integer)ReflectionTestUtils.getField(a, "capacity"),
                is(equalTo(8)));

        logger.debug("...Done.");
    }

    @Test public void testAddAt() {

        logger.debug("testAddAt...");

        DynamicArray<String> s = new DynamicArray<String>();
        s.add(0, "1");
        assertThat(s.get(0), is(equalTo("1")));
        assertThat(s.size(), is(equalTo(1)));
        assertThat((Integer)ReflectionTestUtils.getField(s, "capacity"),
                is(equalTo(1)));

        s.add(1, "3");
        assertThat(s.get(1), is(equalTo("3")));
        assertThat(s.size(), is(equalTo(2)));
        assertThat((Integer)ReflectionTestUtils.getField(s, "capacity"),
                is(equalTo(2)));

        s.add(1, "2");
        assertThat(s.get(1), is(equalTo("2")));
        assertThat(s.size(), is(equalTo(3)));
        assertThat((Integer)ReflectionTestUtils.getField(s, "capacity"),
                is(equalTo(4)));

        assertThat(s.get(0), is(equalTo("1")));
        assertThat(s.get(1), is(equalTo("2")));
        assertThat(s.get(2), is(equalTo("3")));

        logger.debug("...Done.");
    }

    @Test public void testGet(){
        logger.debug("testGet...");
        DynamicArray<String> s = new DynamicArray<String>();

        s.add("1");
        s.add("2");
        s.add("3");

        assertThat(s.get(0), is(equalTo("1")));
        assertThat(s.get(1), is(equalTo("2")));
        assertThat(s.get(2), is(equalTo("3")));

        logger.debug("...Done.");
    }

    @Test public void testContains(){
        logger.debug("testContains...");
        DynamicArray<String> f = new DynamicArray<String>();
        f.add("a");
        f.add("b");
        f.add("c");
        f.add(1, "z");
        assertThat(f.get(1), is(equalTo("z")));
        assertThat(f.contains("z"), is(true));
        assertThat(f.contains("e"), is(false));
        logger.debug("...Done testContains.");
    }

    @Test public void testRemove(){
        logger.debug("testRemove...");
        DynamicArray<Character> c = new DynamicArray<>();
        c.add(0, 'a');
        c.add(1, 'b');
        c.add(2, 'c');
        assertThat(c.get(0), is(equalTo('a')));
        assertThat(c.get(1), is(equalTo('b')));
        assertThat(c.get(2), is(equalTo('c')));
        logger.debug("...Done testRemove.");
    }
}  //  end class
