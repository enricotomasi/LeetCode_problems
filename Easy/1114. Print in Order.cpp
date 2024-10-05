class Foo
{
public:
    promise<void> two;
    promise<void> three;

    Foo()
    {
        
    }

    void first(function<void()> printFirst)
    {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();

        two.set_value();
    }

    void second(function<void()> printSecond)
    {
        two.get_future().wait();

        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        
        three.set_value();
    }

    void third(function<void()> printThird)
    {
        three.get_future().wait();

        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};