package net.nehar.arrays;

/**
 * Dynamic Array Implementation backed by raw array.
 * <p>
 * Underlying array capacity is doubled on additions beyond current capacity.
 * Capacity is shrunk by half any time the elements go below n/4.
 * </p>
 *
 * Created by nehar on 11/29/15.
 *
 */

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class DynamicArray<T> implements IDynamicArray<T>{

    private final static Logger logger = LogManager.getLogger(DynamicArray.class);

    // number of elements or size of dynamic array
    private int itemCount;

    // allocated capacity
    private int capacity;
    private T[] array;

    public DynamicArray(){

        // initialize backing array to empty.
        this.itemCount = 0;
        // start with an array of size 1.
        this.capacity = 1;
        // can safely cast here as the backing array is internal.

        array = (T[]) new Object[1];

    }

    /**
     * Adds object at end of array.
     *
     * Array capacity is doubled if internal array is at max.
     *
     * @param element    Object to append
     */
    @Override
    public void add(T element) {

        // increase current array size if needed
        if (this.itemCount == this.capacity){
            this.resize(2 * this.capacity);
        }

        // add element at end
        this.array[this.itemCount] = element;
        this.itemCount++;
    }

    /**
     * Adds object at specified index.
     *
     * Array capacity is doubled if internal array is at max.
     * Existing elements are moved to make room for element.
     *
     * @param index
     * @param element
     */
    @Override
    public void add(int index, T element) {

        // increase capacity if needed
        if(this.itemCount == this.capacity){
            this.resize(2 * this.capacity);
        }

        // shift elements to make room for new object
        for(int i=this.itemCount; i > index; i--){
            this.array[i] = this.array[i-1];
        }
        // insert element at index
        this.array[index] = element;
        this.itemCount++;
    }

    @Override
    public T get(int index) {
        return this.array[index];
    }

    @Override
    public int indexOf(T o) {
        //TODO: indexOf
        return 0;
    }

    /**
     * Checks if the dynamic array contains the specified element.
     *
     * @param element    object to search.
     * @return true if array contains element, false otherwise.
     */
    @Override
    public boolean contains(T element) {
        for(T item: this.array){
            if(item == element)
                return true;
        }

        return false;
    }

    @Override
    public T remove(int index) {
        //TODO: remove
        return null;
    }

    @Override
    public void removeAll() {
        //TODO: removeAll
    }

    @Override
    public void ensureCapacity(int minCapacity) {
        //TODO: ensure capacity
    }

    @Override
    public int size() {
        return this.itemCount;
    }

    @Override
    public void clear() {
        //TODO: clear
    }

    /**
     * Internal method to resize backing array to capacity.
     * <p>
     * Creates a new array of double current capacity and copies existing
     * elements over.
     * </p>
     *
     * @param capacity    size to increase to.
     */
    private void resize(int capacity){
        logger.debug("Resizing to capacity: "+ capacity);
        // instantiate new backing array
        T[] a = (T[]) new Object[capacity];

        // copy existing elements over...
        for(int i=0, j=0; i<this.itemCount; i++, j++){

            a[j] = this.array[i];
        }

        // set new backing array and capacity.
        this.array = a;
        this.capacity = capacity;
    }
}
