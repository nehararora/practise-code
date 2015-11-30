package net.nehar.arrays;

/**
 * Dynamic Array Interface.
 *
 * @author nehar

 */
public interface IDynamicArray <E>{
    void add(E element);
    void add(int index, E element);
    E get(int index);
    int indexOf(E element);
    boolean contains(E o);
    E remove(int index);
    void removeAll();
    void ensureCapacity(int minCapacity);
    int size();
    void clear();
}
